# 爬数据
import json
import os
import multiprocessing
import requests
from lxml import etree
from multiprocessing import Process, Lock, Queue
import time
import re
from modules.entity import *

news_path = 'datas/news'


############################################################
# 爬取 BBC 的新闻
# 文件以 json 格式保存到文件里, 命名方式是时间+序号
############################################################


# 获取已经爬到的文件
def read_exist_news():
    filenames = os.listdir(news_path)
    news_list = []
    for filename in filenames:
        path = f"{news_path}/{filename}"
        with open(path, 'r', encoding='utf8') as f:
            load_dict = json.loads(json.load(f))
        news = News.from_dict(load_dict)
        if news is not None:
            news_list.append(news)
        else:
            print(f"{timestrap()}# [WARN] 反序列化失败@{path}")
    return news_list


# 使用代理进行 get, 返回 response
def query(url):
    proxies = {"http": "socks5://127.0.0.1:10808", "https": "socks5://127.0.0.1:10808"}
    response = requests.get(url, proxies=proxies)
    return response


# 获取 BBC 各专栏页面
def get_newsdir_links(url):
    response = query(url)
    tree = etree.HTML(query(url).text)
    hrefs = tree.xpath(".//nav[@class='nw-c-nav__wide']//a/@href")
    dirs = [f"https://www.bbc.com{x}" for x in hrefs]
    return dirs


# 扫描 BBC 专栏, 获取里面的 url, 返回扫描到的所有 url
def get_news_links(url, arr=None, mutex=None):
    response = query(url)
    pattern = re.compile(r"(?<=href=\")(/news/[^/]*-\d+)(?=\")")
    hrefs = pattern.findall(response.text)
    links = [f"https://www.bbc.com{href}" for href in hrefs]
    if arr is not None:
        with mutex:
            arr.extend(links)
    return links


# 扫描 BBC 新闻页面, 保存新闻的文本信息
def get_article(url, arr=None, mutex=None):
    response = query(url)
    tree = etree.HTML(response.text)
    try:
        title = tree.xpath("//h1[@id='main-heading']/text()")[0]
        text_nodes = tree.xpath("//div[@data-component='text-block']")
        content = [''.join(x.xpath('.//text()')) for x in text_nodes]
        timestamp = tree.xpath(".//time[@data-testid='timestamp']/@datetime")[0][:len('xxxx-xx-xx')]
        url = response.url
        news = News(title, timestamp, '\n'.join(content), url)

        if arr is not None and len(content) > 0:
            with mutex:
                arr.append(news)
    except IndexError as e:
        print(e)
        print(f"{timestrap()}# 出错的 url = {url}")


# 时间戳工具
def timestrap():
    return f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}"


def start():
    # 获取分栏目录
    dirs = get_newsdir_links('https://www.bbc.com/news')

    # 获取新闻 url
    share_news = multiprocessing.Manager().list()
    share_lock = multiprocessing.Manager().Lock()
    threads = [Process(target=get_news_links, args=(dirs[i], share_news, share_lock)) for i in range(len(dirs))]
    print(f"{timestrap()}# 正在获取新闻 url...启动{len(threads)}个线程")
    for i in range(len(threads)):
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()
    print(f"{timestrap()}# 新闻 url 抓取完成, 共 {len(share_news)} 条")

    # url 去重
    exist_news_list = read_exist_news()
    md5_list = [x.md5sum() for x in exist_news_list]
    url_list = [x.url for x in exist_news_list]
    links = list(set(share_news))
    links = list(filter(lambda o: o not in url_list, links))
    print(f"{timestrap()}# 去重后剩下 {len(links)} 条")

    # 记录新闻
    once = 10
    # 每轮开辟 10 个线程, 多线程访问 ( 线程要是开多了电脑会死机 )
    share_articles = multiprocessing.Manager().list()
    threads = [Process(target=get_article, args=(links[i], share_articles, share_lock)) for i in range(len(links))]
    for i in range(0, len(links), once):
        print(f"{timestrap()}# 正在获取新闻内容...({i}~{min(i + once, len(links))})/{len(links)}")
        for j in range(i, min(i + once, len(links))):
            threads[j].start()
        for j in range(i, min(i + once, len(links))):
            threads[j].join()
    else:
        print(f"{timestrap()}# 新闻抓取完成, 共 {len(share_articles)} 条")

    # 文件去重
    new_news_list = []
    for news in share_articles:
        md5 = news.md5sum()
        if md5 not in md5_list:
            new_news_list.append(news)
            md5_list.append(md5)

    # 搜索重复编号,防止文件名重复
    exist_filenames = os.listdir(news_path)
    day = time.strftime("%Y-%m-%d", time.localtime())
    exists_number = [-1]
    for filename in exist_filenames:
        result = re.search(rf'(?<={day}-)\d+', filename)
        if result:
            exists_number.append(int(result.group(0)))

    # 输出到文件
    print(f"正在写文件....")
    for i, each in enumerate(new_news_list, start=max(exists_number) + 1):
        path = f'{news_path}/{day}-{i}.txt'
        with open(path, 'w', encoding='utf8') as f:
            each.to_file(f)

    print(f"写文件完成, 共写入{len(new_news_list)} 个文件")


if __name__ == '__main__':
    start()

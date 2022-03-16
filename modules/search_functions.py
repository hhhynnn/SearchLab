import math
import os
import re

from PySide6.QtGui import QIcon

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

import modules
from main import MainWindow
from modules.app_settings import *
from modules.entity import *
from modules.ui_functions import *
from collections import defaultdict
from sklearn.feature_extraction.text import CountVectorizer


######################################################################
# 数据显示相关函数
######################################################################
def v_mul(va, vb):
    """向量点乘"""
    dot = sum([va[i] * vb[i] for i in range(len(va))])
    len_a = math.sqrt(sum([va[i] ** 2 for i in range(len(va))]))
    len_b = math.sqrt(sum([vb[i] ** 2 for i in range(len(va))]))
    return dot / (len_a * len_b)


class SearchFunction(MainWindow):
    def __init__(self):
        super().__init__()
        self.news_results = None

    def valDefinitions(self):
        self.keyword = ''
        self.ui.mode = '新闻'
        # 记录全部文章
        self.news_list = []
        news_dir = './datas/news'
        news_filenames = os.listdir(news_dir)
        t = 0
        for filename in news_filenames:
            news_path = f"{news_dir}/{filename}"
            news = News.load_from_filepath(news_path)
            if news:
                news.num = t
                t += 1
                self.news_list.append(news)

        # 缓存最新的Results
        self.news_results = []

        ######################################################################
        # 检索用的定义: 词袋, 倒排索引等
        ######################################################################
        # 1. 构造词袋
        MIN_DF = 2
        MAX_DF = 0.8
        texts = [x.content for x in self.news_list]
        self.cv = CountVectorizer(min_df=MIN_DF, max_df=MAX_DF)
        self.count_vector = self.cv.fit_transform(texts)
        self.words = self.cv.get_feature_names_out()
        self.words_vector = self.count_vector.toarray()

        # 2. 构建倒排索引
        def generate_inverse_index(text_list, words_list, wordcount_vector):
            iv_index = defaultdict(list)
            for text_idx, text in enumerate(text_list):
                for word_idx, word in enumerate(words_list):
                    cnt = wordcount_vector[text_idx][word_idx]
                    if cnt != 0:
                        position_list = [m.span() for m in re.finditer(rf'{word}', text)]
                        iv_index[word].append((text_idx, cnt, position_list))
            return iv_index

        self.inverse_index = generate_inverse_index(texts, self.words, self.words_vector)

    def setNews(self, news: News):
        self.ui.label_title.setText(news.title)
        self.ui.label_time.setText(news.rtime)
        self.ui.label_url.setText(news.url)
        self.ui.plainText_content.setPlainText(news.content)

    def setNewsResults(self, results: list[NewsResult]):
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(len(results))
        for k, result in enumerate(results):
            self.ui.tableWidget.setItem(k, 0, QTableWidgetItem(result.title))
            self.ui.tableWidget.setItem(k, 1, QTableWidgetItem(result.rtime))
            self.ui.tableWidget.setItem(k, 2, QTableWidgetItem(result.cor))
            self.ui.tableWidget.setItem(k, 3, QTableWidgetItem(result.snippet))

    def saveEditText(self, text):
        self.keyword = text
        print(f"keyword:{text}")

    def saveSearchMode(self, mode):
        self.ui.mode = mode
        print(f"mode:{mode}")

    def doubleClickTableWidgets(self, r, c):
        """双击某一条新闻，跳转到该新闻页面"""
        # 事件识别
        print(f"table widgets cell clicked:{r}, {c}")
        if r > len(self.news_results):
            return
        # 设置新闻页
        # SearchFunction.setNewsResults(self, [self.news_results[r]])
        SearchFunction.setNews(self, self.news_results[r].origin)
        # 跳转
        self.ui.stackedWidget.setCurrentWidget(self.ui.widget_result)  # SET PAGE
        modules.ui_functions.UIFunctions.resetStyle(self, 'btn_new')  # RESET ANOTHERS BUTTONS SELECTED
        self.ui.btn_new.setStyleSheet(
            modules.ui_functions.UIFunctions.selectMenu(self.ui.btn_new.styleSheet()))  # SELECT MENU

    def startSearch(self):
        # todo:完成搜索算法
        # 1. 检索
        def search(any_str, index, article_list, cv_global, words_vector_):
            keywords = [s for s in any_str.split(' ') if re.match(r'\b\w+\b', s)]
            index_items = []
            freq = []
            for key in keywords:
                item = index[key].copy()  # 不会出现 keyError
                index_items.append(item)
                freq.append(0)
                if item:
                    for text_info in item:
                        # text_info 格式: (text_idx, cnt, position_list)
                        freq[-1] += text_info[1]
            result_dict = {}
            for idx, item in enumerate(index_items):
                if len(item) == 0:
                    continue
                for text_info in item:
                    text_idx = text_info[0]
                    if len(text_info[2]) == 0:
                        continue
                    if text_idx not in result_dict:
                        # todo: 添加该文章到结果中
                        # result_dict[text_idx] = ResultItem(text_idx, article_list[text_idx])
                        print(f"text_info:{text_info}")
                        result_dict[text_idx] = NewsResult(self.news_list[text_idx], 0, text_info[2][0][0])
                    # todo: 增加该文章的关联度
                    result_dict[text_idx].count += 1
                    result_dict[text_idx].freq += text_info[1]
                    result_dict[text_idx].rank += text_info[1] * 100 / freq[idx]  # TF-IDF 权重
                    # result_dict[text_idx].occurrence.extend(text_info[2])

            search_vec = CountVectorizer(vocabulary=cv_global.get_feature_names_out()).fit_transform(
                [any_str]).toarray()
            result_list = list(result_dict.values())
            for result in result_list:
                result.score = v_mul(search_vec[0], words_vector_[result.num])  # todo

            # 结果排序 todo: 使用高级算法
            result_list.sort(key=lambda x: x.rank * x.count, reverse=True)

            # 返回结果
            return result_list

        self.news_results = search(self.keyword, self.inverse_index, self.news_list, self.cv, self.words_vector)
        for result in self.news_results:
            result.cor = f" {result.rank * result.count:.3f}"

        # 2. 展示结果
        SearchFunction.setNewsResults(self, self.news_results)
        # SearchFunction.setNews(self, self.news_list[0])

    ######################################################################
    # 实现所有搜索函数的绑定
    ######################################################################
    def SearchDefinitions(self):
        SearchFunction.valDefinitions(self)

        # 记录输入的关键字
        self.ui.lineEdit.textEdited.connect(lambda x: SearchFunction.saveEditText(self, x))

        # 记录搜索模式
        self.ui.comboBox.currentTextChanged.connect(lambda x: SearchFunction.saveSearchMode(self, x))

        # 开启搜索
        self.ui.pushButton.clicked.connect(lambda: SearchFunction.startSearch(self))

        # 双击跳转
        self.ui.tableWidget.cellDoubleClicked.connect(lambda r, c: SearchFunction.doubleClickTableWidgets(self, r, c))

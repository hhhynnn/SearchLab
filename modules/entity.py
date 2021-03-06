import hashlib
import json
import os.path


class News:
    """展示新闻本身所需要的完整内容"""

    def __init__(self, title='文章标题', rtime='发布时间', content='正文内容', url='原文链接'):
        self.title = title
        self.rtime = rtime
        self.content = content
        self.url = url

    def __str__(self):
        return f"""标题: {self.title}
        发布时间: {self.title}
        正文内容: {self.content[:min(len(self.content), 50)]}
        原文链接: {self.url}"""

    @staticmethod
    def from_dict(d: dict):
        try:
            news = News(d['title'], d['rtime'], d['content'], d['url'])
        except KeyError:
            news = None
        return news

    def to_dict(self):
        return self.__dict__

    def to_file(self, file):
        json.dump(json.dumps(self, default=News.to_dict), file)

    @staticmethod
    def load_from_filepath(path):
        if not os.path.exists(path):
            return None
        try:
            with open(path, 'r', encoding='utf8') as f:
                load_dict = json.loads(json.load(f))
            news = News.from_dict(load_dict)
        except Exception as e:
            print(e)
            print(f"[WARN] 反序列化失败@{path}")
            return None
        return news

    def md5sum(self):
        txt = self.title + self.content
        m = hashlib.md5()
        m.update(txt.encode('utf-8'))
        return m.hexdigest()

    def __eq__(self, other):
        if type(other) == News:
            return self.md5sum() == other.md5sum()
        return False


class NewsResult:
    """展示页需要展示的内容"""

    def __init__(self, origin: News, cor=0, keyPos=0):
        self.origin = origin
        self.title = origin.title
        self.rtime = origin.rtime
        self.cor = f"{cor:.3f}"
        content = self.origin.content
        begin = max(0, keyPos - 20)
        snippet = f"{'...' if begin else ''}{content[begin:]}"
        self.snippet = snippet

        self.count = 0  # 关键词个数
        self.freq = 0  # 关键词出现次数
        self.rank = 0  # TF-IDF 权重和
        self.occurrence = list()  # 关键词出现位置
        self.score = 0
        self.num = origin.num

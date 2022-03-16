import os

from PySide6.QtGui import QIcon

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

from main import MainWindow
from modules.app_settings import *
from main import *
from modules.entity import *


######################################################################
# 数据显示相关函数
######################################################################

class SearchFunction(MainWindow):
    def valDefinitions(self):
        self.ui.keyword = ''
        self.ui.mode = '新闻'
        # 记录全部文章
        self.ui.news_list = []
        news_dir = './datas/news'
        news_filenames = os.listdir(news_dir)
        for filename in news_filenames:
            news_path = f"{news_dir}/{filename}"
            news = News.load_from_filepath(news_path)
            if news:
                self.ui.news_list.append(news)

    def displayNews(self, news: News):
        self.ui.label_title.setText(news.title)
        self.ui.label_time.setText(news.rtime)
        self.ui.label_url.setText(news.url)
        self.ui.text_content.setText(news.content)

    def saveEditText(self, text):
        self.ui.keyword = text
        print(f"keyword:{text}")

    def saveSearchMode(self, mode):
        self.ui.mode = mode
        print(f"mode:{mode}")

    def startSearch(self):
        # todo:完成搜索算法
        SearchFunction.displayNews(self, self.ui.news_list[0])
        pass

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

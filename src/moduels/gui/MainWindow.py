import os, sys, time

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 更改工作目录，指向正确的当前文件夹
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # 将当前目录导入 python 寻找 package 和 moduel 的变量

from PySide6.QtGui import *
from PySide6.QtCore import *

from PySide6.QtWidgets import *
from Combo_SearchMode import Combo_SearchMode


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # 总布局
        self.central_widget = QWidget()  # 主页面必须有 Widget, 否则不会显示任何东西
        self.central_layout = QVBoxLayout()

        # 搜索框
        self.search_box = QGroupBox("搜索框")
        self.search_layout = QHBoxLayout()
        self.input_text = QLineEdit()
        self.search_button = QPushButton("◎")
        self.mode_menu = Combo_SearchMode()

        # 结果框
        self.result_box = QGroupBox("结果框")
        self.result_layout = QHBoxLayout()
        self.result_scroll_area = QScrollArea()

        self.initLayout()

    def initLayout(self):
        # 整体框架
        self.setWindowTitle("Search Tool")
        self.resize(400, 300)
        self.setCentralWidget(self.central_widget)

        # 设置 layout 嵌套
        self.central_widget.setLayout(self.central_layout)
        self.central_layout.addWidget(self.search_box)
        self.central_layout.addWidget(self.result_box)

        # 搜索框
        self.search_box.setLayout(self.search_layout)
        self.search_layout.addWidget(self.input_text)
        self.search_layout.addWidget(self.search_button)
        self.search_layout.addWidget(self.mode_menu)

        # 展示框
        self.result_box.setLayout(self.result_layout)
        self.result_layout.addWidget(self.result_scroll_area)
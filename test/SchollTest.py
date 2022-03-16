import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 更改工作目录，指向正确的当前文件夹
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # 将当前目录导入 python 寻找 package 和 moduel 的变量

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class Scroll_Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)

        self.scroll_area = QScrollArea()
        self.scroll_area.setMinimumHeight(100)
        self.layout.addWidget(self.scroll_area)

        self.scroll_bar = QScrollBar()
        self.scroll_area.addScrollBarWidget(self.scroll_bar, Qt.AlignRight)

        self.scroll_widget = QWidget()
        self.scroll_area.setWidget(self.scroll_widget)

        self.scroll_layout = QVBoxLayout()
        self.scroll_widget.setLayout(self.scroll_layout)

        for _ in range(10):
            self.scroll_layout.addWidget(QPushButton(f"Button{_ + 1}"))

        self.show()


if __name__ == '__main__':
    app = QApplication()
    window = Scroll_Test()
    app.exec()

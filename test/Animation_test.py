import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 更改工作目录，指向正确的当前文件夹
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # 将当前目录导入 python 寻找 package 和 moduel 的变量

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class Animation_Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.button = QPushButton("点我")
        self.button.clicked.connect(self.doAnim)


        self.setGeometry(300, 300, 380, 300)
        self.setWindowTitle("Animation")

        self.setCentralWidget(self.widget)
        self.widget.setLayout(self.layout)
        self.layout.addWidget(self.button)

        self.show()

    def doAnim(self):
        self.anim = QPropertyAnimation(self.button, b"geometry")  # b?u?
        self.anim.setDuration(1000)
        self.anim.setStartValue(QRect(150, 30, 100, 100))
        self.anim.setEndValue(QRect(150, 30, 200, 200))
        # self.anim.setEasingCurve(QEasingCurve.InOutQuart)
        self.anim.start()


if __name__ == '__main__':
    app = QApplication()
    window = Animation_Test()
    app.exec()

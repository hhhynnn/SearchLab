from test import Ui_MainWindow

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    app.exec()

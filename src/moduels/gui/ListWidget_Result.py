from PySide6.QtWidgets import *
from PySide6.QtCore import *


class ListWidget_Result(QListWidget):
    def __init__(self):
        super().__init__()
        self.addItem(QListWidgetItem("hh", self))

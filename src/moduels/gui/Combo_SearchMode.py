from PySide6.QtWidgets import QComboBox


class Combo_SearchMode(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItems(['News', 'Image'])

        self.initSlot()

    def initSlot(self):
        self.currentTextChanged.connect(self.text_changed)

    def text_changed(self, s):
        print(s)

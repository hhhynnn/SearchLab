import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from moduels.gui.MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

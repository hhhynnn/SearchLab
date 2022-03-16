# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(755, 522)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 735, 460))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(600, 400))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)

        # self.verticalLayout_3 = QVBoxLayout()
        # self.scrollAreaWidgetContents.setLayout(self.verticalLayout_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_6 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_8 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_5 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 755, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi


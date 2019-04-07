# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'go.ui',
# licensing of 'go.ui' applies.
#
# Created: Sun Mar 17 18:40:52 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!
import random

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QFont, QPainter


# from eee import example


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 591)
        appStyle = """
        QMainWindow{
        background-color: #1ECAEB;
        }
        """
        MainWindow.setStyleSheet(appStyle)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 210, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton:pressed { background-color: yellow }")
        self.pushButton.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 300, 151, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton:pressed { background-color: yellow }")
        self.pushButton_2.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 300, 151, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("QPushButton:pressed { background-color: yellow }")
        self.pushButton_3.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 210, 151, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("QPushButton:hover { background-color: yellow }")
        self.pushButton_4.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(127, 60, 521, 51))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        DEFAULT_STYLE = """
        QProgressBar{
            border: 2px solid grey;
            border-radius: 5px;
            text-align: center
        }

        QProgressBar::chunk {
            background-color: lightgreen;
            width: 10px;
            margin: 1px;
        }
        """

        self.progressBar.setStyleSheet(DEFAULT_STYLE)
        self.progressBar2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar2.setGeometry(QtCore.QRect(127, 451, 521, 51))
        self.progressBar2.setProperty("value", 0)
        self.progressBar2.setObjectName("progressBar2")


        DEFAULT_STYLE2 = """
        QProgressBar{
            border: 2px solid grey;
            border-radius: 5px;
            text-align: center
        }

        QProgressBar::chunk {
            background-color: #EB1E7A;
            width: 10px;
            margin: 1px;
        }
        """
        r = 'background-image: url(https://bipbap.ru/wp-content/uploads/2017/10/0_8eb56_842bba74_XL-640x400.jpg)'
        self.progressBar2.setStyleSheet(DEFAULT_STYLE2)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(240, 210, 271, 141))
        self.textEdit.setObjectName('TEXT')
        self.textEdit.setFont(QtGui.QFont("Times", 45, QtGui.QFont.Bold))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "СТАРТ", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", ":)", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", ":)", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("MainWindow", ":)", None, -1))

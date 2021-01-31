# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RTCIS.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

import Img1
import bts
import date_time
import datetime

from Future_Info import Ui_FutureInfo
from Op import Ui_Operating_Hours
from Todays_Stalls import Ui_CurrentlyOpenStalls
from Waiting_Time import Ui_Waiting_Time


class Ui_RTCIS(object):
    def setupUi(self, RTCIS):
        RTCIS.setObjectName("RTCIS")
        RTCIS.resize(681, 451)
        RTCIS.setMaximumSize(QtCore.QSize(681, 451))
        self.centralwidget = QtWidgets.QWidget(RTCIS)
        self.centralwidget.setObjectName("centralwidget")
        self.Bg_Img = QtWidgets.QLabel(self.centralwidget)
        self.Bg_Img.setGeometry(QtCore.QRect(0, 0, 681, 451))
        self.Bg_Img.setMaximumSize(QtCore.QSize(681, 451))
        self.Bg_Img.setObjectName("Bg_Img")

        self.Current_Stall = QtWidgets.QPushButton(self.centralwidget)
        self.Current_Stall.setGeometry(QtCore.QRect(230, 230, 191, 42))
        self.Current_Stall.setMaximumSize(QtCore.QSize(211, 42))
        self.Current_Stall.setStyleSheet("background-image: url(:/bt1/button1.png);")
        self.Current_Stall.setText("")
        self.Current_Stall.setObjectName("Current_Stall")
        self.Current_Stall.clicked.connect(self.openTodayStalls)

        self.Future_info = QtWidgets.QPushButton(self.centralwidget)
        self.Future_info.setGeometry(QtCore.QRect(430, 230, 213, 41))
        self.Future_info.setMinimumSize(QtCore.QSize(0, 0))
        self.Future_info.setMaximumSize(QtCore.QSize(213, 42))
        self.Future_info.setStyleSheet("background-image: url(:/bt2/button2.png);")
        self.Future_info.setText("")
        self.Future_info.setObjectName("Future_info")
        self.Future_info.clicked.connect(self.openFutureInfo)

        self.Wait_time = QtWidgets.QPushButton(self.centralwidget)
        self.Wait_time.setGeometry(QtCore.QRect(230, 280, 191, 42))
        self.Wait_time.setMaximumSize(QtCore.QSize(213, 42))
        self.Wait_time.setStyleSheet("background-image: url(:/bt3/button3.png);")
        self.Wait_time.setText("")
        self.Wait_time.setObjectName("Wait_time")
        self.Wait_time.clicked.connect(self.openWaitingTime)

        self.DATE = QtWidgets.QTextBrowser(self.centralwidget)
        self.DATE.setGeometry(QtCore.QRect(520, 350, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.DATE.setFont(font)
        self.DATE.setFrameShape(QtWidgets.QFrame.Box)
        self.DATE.setLineWidth(3)
        self.DATE.setObjectName("DATE")
        self.DATE.setText(date_time.now.toString(Qt.DefaultLocaleLongDate))
        self.TIME = QtWidgets.QTextBrowser(self.centralwidget)
        self.TIME.setGeometry(QtCore.QRect(520, 380, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.TIME.setFont(font)
        self.TIME.setFrameShape(QtWidgets.QFrame.Box)
        self.TIME.setLineWidth(3)
        self.TIME.setObjectName("TIME")
        self.TIME.setText(date_time.time.toString(Qt.DefaultLocaleLongDate))

        self.Op_hrs = QtWidgets.QPushButton(self.centralwidget)
        self.Op_hrs.setGeometry(QtCore.QRect(430, 280, 213, 42))
        self.Op_hrs.setMaximumSize(QtCore.QSize(213, 42))
        self.Op_hrs.setStyleSheet("background-image: url(:/bt4/button4.png);")
        self.Op_hrs.setText("")
        self.Op_hrs.setObjectName("Op_hrs")
        self.Op_hrs.clicked.connect(self.openOperatingHours)

        RTCIS.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RTCIS)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 22))
        self.menubar.setObjectName("menubar")
        RTCIS.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RTCIS)
        self.statusbar.setObjectName("statusbar")
        RTCIS.setStatusBar(self.statusbar)

        self.retranslateUi(RTCIS)
        QtCore.QMetaObject.connectSlotsByName(RTCIS)

    def retranslateUi(self, RTCIS):
        _translate = QtCore.QCoreApplication.translate
        RTCIS.setWindowTitle(_translate("RTCIS", "MainWindow"))
        self.Bg_Img.setText(_translate("RTCIS", "<html><head/><body><p align=\"center\"><img src=\":/Img1/Logo1.jpg\"/></p></body></html>"))

    def openTodayStalls(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CurrentlyOpenStalls()
        self.ui.setupUi(self.window)
        self.window.show()

    def openOperatingHours(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Operating_Hours()
        self.ui.setupUi(self.window)
        self.window.show()

    def openFutureInfo(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FutureInfo()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWaitingTime(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Waiting_Time()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RTCIS = QtWidgets.QMainWindow()
    ui = Ui_RTCIS()
    ui.setupUi(RTCIS)
    RTCIS.show()
    sys.exit(app.exec_())

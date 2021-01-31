# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Waiting_Time.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import bg_img
import datetime
import stall_times
import wait_time


class Ui_Waiting_Time(object):
    def setupUi(self, Waiting_Time):
        Waiting_Time.setObjectName("CurrentlyOpenStalls")
        Waiting_Time.resize(908, 698)
        Waiting_Time.setMaximumSize(QtCore.QSize(908, 698))
        self.centralwidget = QtWidgets.QWidget(Waiting_Time)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 9, 908, 80))
        self.label.setMaximumSize(QtCore.QSize(908, 80))
        self.label.setStyleSheet("background-image: url(:/Heading_Label/FI_Heading.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 80, 908, 581))
        self.label_2.setMaximumSize(QtCore.QSize(908, 581))
        self.label_2.setStyleSheet("background-image: url(:/bgImg/today_stalls_wallpaper copy.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.McD_bt = QtWidgets.QPushButton(self.centralwidget)
        self.McD_bt.setGeometry(QtCore.QRect(0, 80, 372, 117))
        self.McD_bt.setMaximumSize(QtCore.QSize(372, 117))
        self.McD_bt.setStyleSheet("background-image: url(:/FINAL/MCD_FINAL.jpg);")
        self.McD_bt.setText("")
        self.McD_bt.setObjectName("McD_bt")
        self.McD_bt.clicked.connect(self.MD_bt1)

        self.WS_bt = QtWidgets.QPushButton(self.centralwidget)
        self.WS_bt.setGeometry(QtCore.QRect(0, 190, 372, 117))
        self.WS_bt.setMaximumSize(QtCore.QSize(372, 117))
        self.WS_bt.setStyleSheet("background-image: url(:/FINAL/WS_FINAL.jpg);")
        self.WS_bt.setText("")
        self.WS_bt.setObjectName("WS_bt")
        self.WS_bt.clicked.connect(self.WS_bt2)

        self.CR_bt = QtWidgets.QPushButton(self.centralwidget)
        self.CR_bt.setGeometry(QtCore.QRect(0, 300, 372, 117))
        self.CR_bt.setMaximumSize(QtCore.QSize(372, 117))
        self.CR_bt.setStyleSheet("background-image: url(:/FINAL/CR_FINAL.jpg);")
        self.CR_bt.setText("")
        self.CR_bt.setObjectName("CR_bt")
        self.CR_bt.clicked.connect(self.CR_bt3)

        self.NS_bt = QtWidgets.QPushButton(self.centralwidget)
        self.NS_bt.setGeometry(QtCore.QRect(0, 410, 372, 117))
        self.NS_bt.setMaximumSize(QtCore.QSize(372, 117))
        self.NS_bt.setStyleSheet("background-image: url(:/FINAL/NS_FINAL.jpg);")
        self.NS_bt.setText("")
        self.NS_bt.setObjectName("NS_bt")
        self.NS_bt.clicked.connect(self.NS_bt4)

        self.MS_bt = QtWidgets.QPushButton(self.centralwidget)
        self.MS_bt.setGeometry(QtCore.QRect(0, 530, 372, 117))
        self.MS_bt.setMaximumSize(QtCore.QSize(372, 117))
        self.MS_bt.setStyleSheet("background-image: url(:/FINAL/MS_FINAL.jpg);")
        self.MS_bt.setText("")
        self.MS_bt.setObjectName("MS_bt")
        self.MS_bt.clicked.connect(self.MS_bt5)

        self.Menu = QtWidgets.QLabel(self.centralwidget)
        self.Menu.setGeometry(QtCore.QRect(370, 210, 541, 441))
        self.Menu.setMaximumSize(QtCore.QSize(541, 451))
        self.Menu.setText("")
        self.Menu.setObjectName("Menu")

        self.People_num = QtWidgets.QLabel(self.centralwidget)
        self.People_num.setGeometry(QtCore.QRect(370, 140, 71, 31))
        self.People_num.setStyleSheet("font: 18pt \"Chalkduster\";\n"
                                     "color: rgb(0, 255, 255);")
        self.People_num.setObjectName("People_num")

        self.People_num_Heading = QtWidgets.QLabel(self.centralwidget)
        self.People_num_Heading.setGeometry(QtCore.QRect(370, 80, 251, 31))
        self.People_num_Heading.setStyleSheet("font: 15pt \"Chalkduster\";\n"
                                       "color: rgb(253, 139, 133);")
        self.People_num_Heading.setObjectName("People_num_Heading")

        self.People = QtWidgets.QTextEdit(self.centralwidget)
        self.People.setGeometry(QtCore.QRect(440, 140, 111, 31))
        self.People.setObjectName("DAY")

        Waiting_Time.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Waiting_Time)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 908, 22))
        self.menubar.setObjectName("menubar")
        Waiting_Time.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Waiting_Time)
        self.statusbar.setObjectName("statusbar")
        Waiting_Time.setStatusBar(self.statusbar)

        self.retranslateUi(Waiting_Time)
        QtCore.QMetaObject.connectSlotsByName(Waiting_Time)

    def retranslateUi(self, CurrentlyOpenStalls):
        _translate = QtCore.QCoreApplication.translate
        CurrentlyOpenStalls.setWindowTitle(_translate("FutureInfo", "MainWindow"))
        self.People_num.setText(_translate("FutureInfo", "Number of People: "))
        self.People_num_Heading.setText(_translate("FutureInfo", "Enter Number of People:"))

    def MD_bt1(self):
        ppl_num = self.People.toPlainText()
        self.Menu.setStyleSheet("font: 40pt \"Chalkduster\";\n"
                                    "color: rgb(0, 255, 255);")
        self.Menu.setText(wait_time.McD_time(ppl_num))

    def WS_bt2(self):
        ppl_num = self.People.toPlainText()
        self.Menu.setStyleSheet("font: 40pt \"Chalkduster\";\n"
                                    "color: rgb(0, 255, 255);")
        self.Menu.setText(wait_time.WS_time(ppl_num))

    def CR_bt3(self):
        ppl_num = self.People.toPlainText()
        self.Menu.setStyleSheet("font: 40pt \"Chalkduster\";\n"
                                    "color: rgb(0, 255, 255);")
        self.Menu.setText(wait_time.CR_time(ppl_num))

    def NS_bt4(self):
        ppl_num = self.People.toPlainText()
        self.Menu.setStyleSheet("font: 40pt \"Chalkduster\";\n"
                                    "color: rgb(0, 255, 255);")
        self.Menu.setText(wait_time.NS_time(ppl_num))

    def MS_bt5(self):
        ppl_num = self.People.toPlainText()
        self.Menu.setStyleSheet("font: 40pt \"Chalkduster\";\n"
                                    "color: rgb(0, 255, 255);")
        self.Menu.setText(wait_time.MS_time(ppl_num))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Waiting_Time = QtWidgets.QMainWindow()
    ui = Ui_Waiting_Time()
    ui.setupUi(Waiting_Time)
    Waiting_Time.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Future_Info.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import Error_Check_Function
import bg_img
import datetime
import stall_times


class Ui_FutureInfo(object):
    def setupUi(self, FutureInfo):
        FutureInfo.setObjectName("CurrentlyOpenStalls")
        FutureInfo.resize(908, 698)
        FutureInfo.setMaximumSize(QtCore.QSize(908, 698))
        self.centralwidget = QtWidgets.QWidget(FutureInfo)
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

        self.Day_Label = QtWidgets.QLabel(self.centralwidget)
        self.Day_Label.setGeometry(QtCore.QRect(370, 140, 71, 31))
        self.Day_Label.setStyleSheet("font: 18pt \"Chalkduster\";\n"
                                     "color: rgb(0, 255, 255);")
        self.Day_Label.setObjectName("Day_Label")

        self.Day_Heading = QtWidgets.QLabel(self.centralwidget)
        self.Day_Heading.setGeometry(QtCore.QRect(370, 80, 251, 31))
        self.Day_Heading.setStyleSheet("font: 20pt \"Chalkduster\";\n"
                                       "color: rgb(253, 139, 133);")
        self.Day_Heading.setObjectName("Day_Heading")

        self.Time_Heading = QtWidgets.QLabel(self.centralwidget)
        self.Time_Heading.setGeometry(QtCore.QRect(620, 80, 261, 31))
        self.Time_Heading.setStyleSheet("font: 18pt \"Chalkduster\";\n"
                                        "color: rgb(253, 139, 133);")
        self.Time_Heading.setObjectName("Time_Heading")

        self.Hour_Label = QtWidgets.QLabel(self.centralwidget)
        self.Hour_Label.setGeometry(QtCore.QRect(620, 110, 81, 21))
        self.Hour_Label.setStyleSheet("font: 16pt \"Chalkduster\";\n"
                                      "color: rgb(0, 255, 255);")
        self.Hour_Label.setObjectName("Hour_Label")

        self.Minute_Label = QtWidgets.QLabel(self.centralwidget)
        self.Minute_Label.setGeometry(QtCore.QRect(620, 140, 91, 31))
        self.Minute_Label.setStyleSheet("font: 18pt \"Chalkduster\";\n"
                                        "color: rgb(0, 255, 255);")
        self.Minute_Label.setObjectName("Minute_Label")

        self.DAY = QtWidgets.QTextEdit(self.centralwidget)
        self.DAY.setGeometry(QtCore.QRect(440, 140, 111, 31))
        self.DAY.setObjectName("DAY")

        self.HOUR = QtWidgets.QTextEdit(self.centralwidget)
        self.HOUR.setGeometry(QtCore.QRect(690, 110, 131, 31))
        self.HOUR.setObjectName("HOUR")

        self.MINUTE = QtWidgets.QTextEdit(self.centralwidget)
        self.MINUTE.setGeometry(QtCore.QRect(710, 140, 111, 31))
        self.MINUTE.setObjectName("MINUTE")

        FutureInfo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FutureInfo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 908, 22))
        self.menubar.setObjectName("menubar")
        FutureInfo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FutureInfo)
        self.statusbar.setObjectName("statusbar")
        FutureInfo.setStatusBar(self.statusbar)

        self.retranslateUi(FutureInfo)
        QtCore.QMetaObject.connectSlotsByName(FutureInfo)

    def retranslateUi(self, CurrentlyOpenStalls):
        _translate = QtCore.QCoreApplication.translate
        CurrentlyOpenStalls.setWindowTitle(_translate("FutureInfo", "MainWindow"))
        self.Day_Label.setText(_translate("FutureInfo", "Day: "))
        self.Day_Heading.setText(_translate("FutureInfo", "Enter Day:"))
        self.Time_Heading.setText(_translate("FutureInfo", "Enter Time(24Hr- HH:MM):"))
        self.Hour_Label.setText(_translate("FutureInfo", "Hour:"))
        self.Minute_Label.setText(_translate("FutureInfo", "Minute:"))

    def MD_bt1(self):
        day_val = self.DAY.toPlainText()
        hour_val = self.HOUR.toPlainText()
        minute_val = self.MINUTE.toPlainText()
        time_val = hour_val + ":" + minute_val

        if stall_times.morn_start_str <= time_val <= stall_times.morn_end_str:
            self.Menu.setStyleSheet("background-image: url(:/FINAL/FINAL_McD_MENU_BF.jpg);")
            self.Menu.setText("")

        elif stall_times.mcd_shift2_start_str <= time_val <= stall_times.mcd_shift2_end_str:
            self.Menu.setStyleSheet("background-image: url(:/FINAL/FINAL_McD_MENU_reg.jpg);")
            self.Menu.setText("")

        else:
            self.Menu.setStyleSheet("font: 40pt \"Chalkduster\";\n"
                                    "color: rgb(0, 255, 255);")
            self.Menu.setText("  SORRY, THE STORE IS\n     CLOSED AT THE \n     GIVEN TIME!")

    def WS_bt2(self):
        day_val = self.DAY.toPlainText()
        hour_val = self.HOUR.toPlainText()
        minute_val = self.MINUTE.toPlainText()
        time_val = hour_val + ":" + minute_val

        if stall_times.morn_start_str <= time_val <= stall_times.morn_end_str and day_val != "Saturday" and day_val != "Sunday":
            self.Menu.setStyleSheet("background-image: url(:/FINAL/FINAL_WS_MENU_1.jpg);")
            self.Menu.setText("")

        elif stall_times.shift2_start_str <= time_val <= stall_times.shift2_end_str and day_val != "Saturday" and day_val != "Sunday":
            self.Menu.setStyleSheet("background-image: url(:/FINAL/FINAL_WS_MENU_2.jpg);")
            self.Menu.setText("")

        else:
            self.Menu.setStyleSheet("font: 40pt \"Chalkduster\";\n"
                                    "color: rgb(0, 255, 255);")
            self.Menu.setText("  SORRY, THE STORE IS\n     CLOSED AT THE \n     GIVEN TIME!")

    def CR_bt3(self):
        day_val = self.DAY.toPlainText()
        hour_val = self.HOUR.toPlainText()
        minute_val = self.MINUTE.toPlainText()
        time_val = hour_val + ":" + minute_val

        if stall_times.morn_start_str <= time_val <= stall_times.shift2_end_str and day_val != "Saturday" and day_val != "Sunday":
            self.Menu.setStyleSheet("background-image: url(:/FINAL/FINAL_CR_MENU.jpg);")
            self.Menu.setText("")

        else:
            self.Menu.setStyleSheet("font: 40pt \"Chalkduster\";\n"
                                    "color: rgb(0, 255, 255);")
            self.Menu.setText("  SORRY, THE STORE IS\n     CLOSED AT THE \n     GIVEN TIME!")

    def NS_bt4(self):
        day_val = self.DAY.toPlainText()
        hour_val = self.HOUR.toPlainText()
        minute_val = self.MINUTE.toPlainText()
        time_val = hour_val + ":" + minute_val

        if stall_times.morn_start_str <= time_val <= stall_times.shift2_end_str and day_val != "Saturday" and day_val != "Sunday":
            self.Menu.setStyleSheet("background-image: url(:/FINAL/FINAL_NS_MENU.jpg);")
            self.Menu.setText("")

        else:
            self.Menu.setStyleSheet("font: 40pt \"Chalkduster\";\n"
                                    "color: rgb(0, 255, 255);")
            self.Menu.setText("  SORRY, THE STORE IS\n     CLOSED AT THE \n     GIVEN TIME!")

    def MS_bt5(self):
        day_val = self.DAY.toPlainText()
        hour_val = self.HOUR.toPlainText()
        minute_val = self.MINUTE.toPlainText()
        time_val = hour_val + ":" + minute_val

        if stall_times.morn_start_str <= time_val <= stall_times.shift2_end_str and day_val != "Saturday" and day_val != "Sunday":
            self.Menu.setStyleSheet("background-image: url(:/FINAL/FINAL_MS_MENU.jpg);")
            self.Menu.setText("")

        else:
            self.Menu.setStyleSheet("font: 40pt \"Chalkduster\";\n"
                                    "color: rgb(0, 255, 255);")
            self.Menu.setText("  SORRY, THE STORE IS\n     CLOSED AT THE \n     GIVEN TIME!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FutureInfo = QtWidgets.QMainWindow()
    ui = Ui_FutureInfo()
    ui.setupUi(FutureInfo)
    FutureInfo.show()
    sys.exit(app.exec_())

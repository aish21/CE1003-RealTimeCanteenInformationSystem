# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Todays_Stalls.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import bg_img
import storeinfo
import date_time
import stall_times

class Ui_CurrentlyOpenStalls(object):
    def setupUi(self, CurrentlyOpenStalls):
        CurrentlyOpenStalls.setObjectName("CurrentlyOpenStalls")
        CurrentlyOpenStalls.resize(908, 698)
        CurrentlyOpenStalls.setMaximumSize(QtCore.QSize(908, 698))
        self.centralwidget = QtWidgets.QWidget(CurrentlyOpenStalls)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 908, 80))
        self.label.setMaximumSize(QtCore.QSize(908, 80))
        self.label.setStyleSheet("background-image: url(:/Heading_Label/Heading_Label.jpg);")
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

        if stall_times.Morning_Shift_Start <= stall_times.now <= stall_times.McD_Shift2_End:
            self.McD_bt.setStyleSheet("background-image: url(:/FINAL/MCD_FINAL.jpg);")
        else:
            self.McD_bt.setStyleSheet("background-image: url(:/FINAL/CLOSED_FINAL.jpg);")

        self.McD_bt.setText("")
        self.McD_bt.setObjectName("McD_bt")
        self.McD_bt.clicked.connect(self.MD_bt1)

        self.WS_bt = QtWidgets.QPushButton(self.centralwidget)
        self.WS_bt.setGeometry(QtCore.QRect(0, 190, 372, 117))
        self.WS_bt.setMaximumSize(QtCore.QSize(372, 117))

        if stall_times.Morning_Shift_Start <= stall_times.now <= stall_times.Shift2_End:
            self.WS_bt.setStyleSheet("background-image: url(:/FINAL/WS_FINAL.jpg);")
        else:
            self.WS_bt.setStyleSheet("background-image: url(:/FINAL/CLOSED_FINAL.jpg);")

        self.WS_bt.setText("")
        self.WS_bt.setObjectName("WS_bt")
        self.WS_bt.clicked.connect(self.WS_bt2)

        self.CR_bt = QtWidgets.QPushButton(self.centralwidget)
        self.CR_bt.setGeometry(QtCore.QRect(0, 300, 372, 117))
        self.CR_bt.setMaximumSize(QtCore.QSize(372, 117))

        if stall_times.Morning_Shift_Start <= stall_times.now <= stall_times.Shift2_End:
            self.CR_bt.setStyleSheet("background-image: url(:/FINAL/CR_FINAL.jpg);")
        else:
            self.CR_bt.setStyleSheet("background-image: url(:/FINAL/CLOSED_FINAL.jpg);")

        self.CR_bt.setText("")
        self.CR_bt.setObjectName("CR_bt")
        self.CR_bt.clicked.connect(self.CR_bt3)

        self.NS_bt = QtWidgets.QPushButton(self.centralwidget)
        self.NS_bt.setGeometry(QtCore.QRect(0, 410, 372, 117))
        self.NS_bt.setMaximumSize(QtCore.QSize(372, 117))

        if stall_times.Morning_Shift_Start <= stall_times.now <= stall_times.Shift2_End:
            self.NS_bt.setStyleSheet("background-image: url(:/FINAL/NS_FINAL.jpg);")
        else:
            self.NS_bt.setStyleSheet("background-image: url(:/FINAL/CLOSED_FINAL.jpg);")

        self.NS_bt.setText("")
        self.NS_bt.setObjectName("NS_bt")
        self.NS_bt.clicked.connect(self.NS_bt4)

        self.MS_bt = QtWidgets.QPushButton(self.centralwidget)
        self.MS_bt.setGeometry(QtCore.QRect(0, 530, 372, 117))
        self.MS_bt.setMaximumSize(QtCore.QSize(372, 117))

        if stall_times.Morning_Shift_Start <= stall_times.now <= stall_times.Shift2_End:
            self.MS_bt.setStyleSheet("background-image: url(:/FINAL/MS_FINAL.jpg);")
        else:
            self.MS_bt.setStyleSheet("background-image: url(:/FINAL/CLOSED_FINAL.jpg);")

        self.MS_bt.setText("")
        self.MS_bt.setObjectName("MS_bt")
        self.MS_bt.clicked.connect(self.MS_bt5)

        self.Menu = QtWidgets.QLabel(self.centralwidget)
        self.Menu.setGeometry(QtCore.QRect(370, 80, 541, 451))
        self.Menu.setMaximumSize(QtCore.QSize(541, 451))
        self.Menu.setText("")
        self.Menu.setObjectName("Menu")
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(380, 530, 521, 121))
        self.info.setMaximumSize(QtCore.QSize(531, 121))
        self.info.setStyleSheet("\n"
"font: 24pt \"Chalkduster\";\n"
"color: rgb(255, 255, 255);")
        self.info.setText("")
        self.info.setObjectName("info")
        CurrentlyOpenStalls.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CurrentlyOpenStalls)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 908, 22))
        self.menubar.setObjectName("menubar")
        CurrentlyOpenStalls.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CurrentlyOpenStalls)
        self.statusbar.setObjectName("statusbar")
        CurrentlyOpenStalls.setStatusBar(self.statusbar)

        self.retranslateUi(CurrentlyOpenStalls)
        QtCore.QMetaObject.connectSlotsByName(CurrentlyOpenStalls)

    def retranslateUi(self, CurrentlyOpenStalls):
        _translate = QtCore.QCoreApplication.translate
        CurrentlyOpenStalls.setWindowTitle(_translate("CurrentlyOpenStalls", "MainWindow"))

    def MD_bt1(self):
        if stall_times.Morning_Shift_Start <= stall_times.now <= stall_times.Morning_Shift_End:
            self.Menu.setStyleSheet("background-image: url(:/FINAL/FINAL_McD_MENU_BF.jpg);")
            self.Menu.setText("")
            self.info.setStyleSheet("font: 20pt \"Chalkduster\";\n"
                                    "color: rgb(252, 255, 255);")
            self.info.setText(storeinfo.infoMCD_str)
        elif stall_times.McD_Shift2_Start <= stall_times.now <= stall_times.McD_Shift2_End:
            self.Menu.setStyleSheet("background-image: url(:/FINAL/FINAL_McD_MENU_reg.jpg);")
            self.Menu.setText("")
            self.info.setStyleSheet("font: 20pt \"Chalkduster\";\n"
                                    "color: rgb(252, 255, 255);")
            self.info.setText(storeinfo.infoMCD_str)
        else:
            self.Menu.setStyleSheet("font: 40pt \"Chalkduster\";\n"
                                    "color: rgb(0, 255, 255);")
            self.Menu.setText("  SORRY, INFORMATION\n    UNAVAILABLE AS\n    STORE IS CLOSED")
            self.info.setText("")

    def WS_bt2(self):
        if stall_times.Morning_Shift_Start <= stall_times.now <= stall_times.Morning_Shift_End:
            self.Menu.setStyleSheet("background-image: url(:/FINAL/FINAL_WS_MENU_1.jpg);")
            self.Menu.setText("")
            self.info.setStyleSheet("font: 10pt \"Chalkduster\";\n"
                                    "color: rgb(252, 255, 255);")
            self.info.setText(storeinfo.infoWS_str)
        elif stall_times.Shift2_Start <= stall_times.now <= stall_times.Shift2_End:
            self.Menu.setStyleSheet("background-image: url(:/FINAL/FINAL_WS_MENU_2.jpg);")
            self.Menu.setText("")
            self.info.setStyleSheet("font: 10pt \"Chalkduster\";\n"
                                    "color: rgb(252, 255, 255);")
            self.info.setText(storeinfo.infoWS_str)
        else:
            self.Menu.setStyleSheet("font: 40pt \"Chalkduster\";\n"
                                    "color: rgb(0, 255, 255);")
            self.Menu.setText("  SORRY, INFORMATION\n    UNAVAILABLE AS\n    STORE IS CLOSED")
            self.info.setText("")

    def CR_bt3(self):
        if stall_times.Morning_Shift_Start <= stall_times.now <= stall_times.Morning_Shift_End:
            self.Menu.setStyleSheet("background-image: url(:/FINAL/FINAL_CR_MENU.jpg);")
            self.Menu.setText("")
            self.info.setStyleSheet("font: 15pt \"Chalkduster\";\n"
                                    "color: rgb(252, 255, 255);")
            self.info.setText(storeinfo.infoCR_str)
        elif stall_times.Shift2_Start <= stall_times.now <= stall_times.Shift2_End:
            self.Menu.setStyleSheet("background-image: url(:/FINAL/FINAL_CR_MENU.jpg);")
            self.Menu.setText("")
            self.info.setStyleSheet("font: 15pt \"Chalkduster\";\n"
                                    "color: rgb(252, 255, 255);")
            self.info.setText(storeinfo.infoCR_str)
        else:
            self.Menu.setStyleSheet("font: 40pt \"Chalkduster\";\n"
                                    "color: rgb(0, 255, 255);")
            self.Menu.setText("  SORRY, INFORMATION\n    UNAVAILABLE AS\n    STORE IS CLOSED")
            self.info.setText("")

    def NS_bt4(self):
        if stall_times.Morning_Shift_Start <= stall_times.now <= stall_times.Morning_Shift_End:
            self.Menu.setStyleSheet("background-image: url(:/FINAL/FINAL_NS_MENU.jpg);")
            self.Menu.setText("")
            self.info.setStyleSheet("font: 15pt \"Chalkduster\";\n"
                                    "color: rgb(252, 255, 255);")
            self.info.setText(storeinfo.infoNS_str)
        elif stall_times.Shift2_Start <= stall_times.now <= stall_times.Shift2_End:
            self.Menu.setStyleSheet("background-image: url(:/FINAL/FINAL_NS_MENU.jpg);")
            self.Menu.setText("")
            self.info.setStyleSheet("font: 15pt \"Chalkduster\";\n"
                                    "color: rgb(252, 255, 255);")
            self.info.setText(storeinfo.infoNS_str)
        else:
            self.Menu.setStyleSheet("font: 40pt \"Chalkduster\";\n"
                                    "color: rgb(0, 255, 255);")
            self.Menu.setText("  SORRY, INFORMATION\n    UNAVAILABLE AS\n    STORE IS CLOSED")
            self.info.setText("")

    def MS_bt5(self):
        if stall_times.Morning_Shift_Start <= stall_times.now <= stall_times.Morning_Shift_End:
            self.Menu.setStyleSheet("background-image: url(:/FINAL/FINAL_MS_MENU.jpg);")
            self.Menu.setText("")
            self.info.setStyleSheet("font: 15pt \"Chalkduster\";\n"
                                    "color: rgb(252, 255, 255);")
            self.info.setText(storeinfo.infoMS_str)
        elif stall_times.Shift2_Start <= stall_times.now <= stall_times.Shift2_End:
            self.Menu.setStyleSheet("background-image: url(:/FINAL/FINAL_MS_MENU.jpg);")
            self.Menu.setText("")
            self.info.setStyleSheet("font: 15pt \"Chalkduster\";\n"
                                    "color: rgb(252, 255, 255);")
            self.info.setText(storeinfo.infoMS_str)
        else:
            self.Menu.setStyleSheet("font: 40pt \"Chalkduster\";\n"
                                    "color: rgb(0, 255, 255);")
            self.Menu.setText("  SORRY, INFORMATION\n    UNAVAILABLE AS\n    STORE IS CLOSED")
            self.info.setText("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrentlyOpenStalls = QtWidgets.QMainWindow()
    ui = Ui_CurrentlyOpenStalls()
    ui.setupUi(CurrentlyOpenStalls)
    CurrentlyOpenStalls.show()
    sys.exit(app.exec_())

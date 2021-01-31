# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OperatingHours.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import bg_img

class Ui_Operating_Hours(object):
    def setupUi(self, Operating_Hours):
        Operating_Hours.setObjectName("Operating_Hours")
        Operating_Hours.resize(681, 451)
        Operating_Hours.setMaximumSize(QtCore.QSize(681, 451))
        self.centralwidget = QtWidgets.QWidget(Operating_Hours)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -20, 681, 451))
        self.label.setMaximumSize(QtCore.QSize(681, 451))
        self.label.setStyleSheet("background-image: url(:/bgImg/today_stalls_wallpaper.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Heading_Label = QtWidgets.QLabel(self.centralwidget)
        self.Heading_Label.setGeometry(QtCore.QRect(0, 0, 681, 71))
        self.Heading_Label.setMaximumSize(QtCore.QSize(681, 71))
        self.Heading_Label.setStyleSheet("background-image: url(:/Heading_Label/Heading_Label_Op.jpg);")
        self.Heading_Label.setText("")
        self.Heading_Label.setObjectName("Heading_Label")

        self.McD = QtWidgets.QPushButton(self.centralwidget)
        self.McD.setGeometry(QtCore.QRect(0, 70, 131, 121))
        self.McD.setMaximumSize(QtCore.QSize(141, 121))
        self.McD.setStyleSheet("background-image: url(:/Logos/MD.jpg);")
        self.McD.setText("")
        self.McD.setObjectName("McD")
        self.McD.clicked.connect(self.MD_bt)

        self.WS = QtWidgets.QPushButton(self.centralwidget)
        self.WS.setGeometry(QtCore.QRect(130, 70, 141, 121))
        self.WS.setStyleSheet("background-image: url(:/Logos/18701ebcc29ab5748c81668844_original..jpeg);")
        self.WS.setText("")
        self.WS.setObjectName("WS")
        self.WS.clicked.connect(self.WS_bt)

        self.CR = QtWidgets.QPushButton(self.centralwidget)
        self.CR.setGeometry(QtCore.QRect(272, 70, 141, 121))
        self.CR.setStyleSheet("background-image: url(:/Logos/154660.jpg);")
        self.CR.setText("")
        self.CR.setObjectName("CR")
        self.CR.clicked.connect(self.CR_bt)


        self.NS = QtWidgets.QPushButton(self.centralwidget)
        self.NS.setGeometry(QtCore.QRect(412, 70, 131, 121))
        self.NS.setStyleSheet("background-image: url(:/Logos/Fishball-mee-2-1080x720.jpg);")
        self.NS.setText("")
        self.NS.setObjectName("NS")
        self.NS.clicked.connect(self.NS_bt)

        self.MS = QtWidgets.QPushButton(self.centralwidget)
        self.MS.setGeometry(QtCore.QRect(540, 70, 141, 121))
        self.MS.setStyleSheet("background-image: url(:/Logos/50eb3334-a38c-11e9-9a3c-98259c87fba2_image_hires_152354.jpg);")
        self.MS.setText("")
        self.MS.setObjectName("MS")
        self.MS.clicked.connect(self.MS_bt)

        self.OP = QtWidgets.QLabel(self.centralwidget)
        self.OP.setGeometry(QtCore.QRect(10, 200, 661, 201))
        self.OP.setObjectName("OP")

        Operating_Hours.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Operating_Hours)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 22))
        self.menubar.setObjectName("menubar")
        Operating_Hours.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Operating_Hours)
        self.statusbar.setObjectName("statusbar")
        Operating_Hours.setStatusBar(self.statusbar)

        self.retranslateUi(Operating_Hours)
        QtCore.QMetaObject.connectSlotsByName(Operating_Hours)

    def retranslateUi(self, Operating_Hours):
        _translate = QtCore.QCoreApplication.translate
        Operating_Hours.setWindowTitle(_translate("Operating_Hours", "MainWindow"))
        self.OP.setText(_translate("Operating_Hours", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))

    def MD_bt(self):
        self.OP.setStyleSheet("font: 38pt \"Chalkduster\";\n"
                                "color: rgb(0, 255, 255);")
        self.OP.setText("        Operating Hours:\n    Breakfast: 7am to 11am\nRegular Menu: 11am to 9:30pm")

    def WS_bt(self):
        self.OP.setStyleSheet("font: 36pt \"Chalkduster\";\n"
                                "color: rgb(0, 255, 255);")
        self.OP.setText("           Operating Hours:\n      First Shift: 7am to 11am\n   Second Shift: 11am to 9:30pm")

    def CR_bt(self):
        self.OP.setStyleSheet("font: 36pt \"Chalkduster\";\n"
                                "color: rgb(0, 255, 255);")
        self.OP.setText("Operating Hours: 7am to 9:30pm")

    def NS_bt(self):
        self.OP.setStyleSheet("font: 36pt \"Chalkduster\";\n"
                                "color: rgb(0, 255, 255);")
        self.OP.setText("Operating Hours: 7am to 9:30pm")

    def MS_bt(self):
        self.OP.setStyleSheet("font: 36pt \"Chalkduster\";\n"
                                "color: rgb(0, 255, 255);")
        self.OP.setText("Operating Hours: 7am to 9:30pm")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Operating_Hours = QtWidgets.QMainWindow()
    ui = Ui_Operating_Hours()
    ui.setupUi(Operating_Hours)
    Operating_Hours.show()
    sys.exit(app.exec_())

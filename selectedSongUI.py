# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectedSong.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from SongDetails import SongsDetails
from Songs import Songs_array


class Ui_mainSelectedSong(object):
    def __init__(self, message):
        self.message = message
        print('current song:' + message)
        # if message in Songs_array:
        #     print(message.artist)
        for x in Songs_array:
            if x.title == message:
                print(x.artist)
                self.artist = x.artist

    def setupUi(self, mainSelectedSong):
        mainSelectedSong.setObjectName("mainSelectedSong")
        mainSelectedSong.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainSelectedSong)
        self.centralwidget.setObjectName("centralwidget")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.back_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.back_btn.setStyleSheet("\n"
                                    "border-radius:10px;\n"
                                    " image: url(D:/College Stuff/Semester 8/Artificial Intelligence/FinalAI/next.png);")
        self.back_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("next.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QtCore.QSize(50, 50))
        self.back_btn.setObjectName("back_btn")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(550, 10, 121, 41))
        self.label_username.setStyleSheet("background-color:#c4c4c4;\n"
                                          "border-radius:10px;\n"
                                          "text-align: center;")
        self.label_username.setAlignment(QtCore.Qt.AlignCenter)
        self.label_username.setObjectName("label_username")
        self.logout_btn = QtWidgets.QPushButton(self.centralwidget)
        self.logout_btn.setGeometry(QtCore.QRect(690, 10, 93, 41))
        self.logout_btn.setStyleSheet("border:1px solid black;\n"
                                      "border-radius:10px;")
        self.logout_btn.setObjectName("logout_btn")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(50, 120, 351, 281))
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 110, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 150, 311, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 200, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 220, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.star5 = QtWidgets.QPushButton(self.centralwidget)
        self.star5.setGeometry(QtCore.QRect(490, 270, 31, 16))
        self.star5.setStyleSheet("\n"
                                 "background-color:transparent;")
        self.star5.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("emptyStar.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.star5.setIcon(icon1)
        self.star5.setObjectName("star5")
        self.star3 = QtWidgets.QPushButton(self.centralwidget)
        self.star3.setGeometry(QtCore.QRect(450, 270, 31, 16))
        self.star3.setStyleSheet("\n"
                                 "background-color:transparent;")
        self.star3.setText("")
        self.star3.setIcon(icon1)
        self.star3.setObjectName("star3")
        self.star1 = QtWidgets.QPushButton(self.centralwidget)
        self.star1.setGeometry(QtCore.QRect(410, 270, 31, 16))
        self.star1.setStyleSheet("\n"
                                 "background-color:transparent;")
        self.star1.setText("")
        self.star1.setIcon(icon1)
        self.star1.setObjectName("star1")
        self.star4 = QtWidgets.QPushButton(self.centralwidget)
        self.star4.setGeometry(QtCore.QRect(470, 270, 31, 16))
        self.star4.setStyleSheet("\n"
                                 "background-color:transparent;")
        self.star4.setText("")
        self.star4.setIcon(icon1)
        self.star4.setObjectName("star4")
        self.star2 = QtWidgets.QPushButton(self.centralwidget)
        self.star2.setGeometry(QtCore.QRect(430, 270, 31, 16))
        self.star2.setStyleSheet("\n"
                                 "background-color:transparent;")
        self.star2.setText("")
        self.star2.setIcon(icon1)
        self.star2.setObjectName("star2")
        mainSelectedSong.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainSelectedSong)
        self.statusbar.setObjectName("statusbar")
        mainSelectedSong.setStatusBar(self.statusbar)

        self.retranslateUi(mainSelectedSong)
        QtCore.QMetaObject.connectSlotsByName(mainSelectedSong)

    def retranslateUi(self, mainSelectedSong):
        _translate = QtCore.QCoreApplication.translate
        mainSelectedSong.setWindowTitle(
            _translate("mainSelectedSong", "MainWindow"))
        self.label_username.setText(_translate("mainSelectedSong", "USER"))
        self.logout_btn.setText(_translate("mainSelectedSong", "LOGOUT"))
        self.label_5.setText(_translate("mainSelectedSong", self.message))
        self.label_2.setText(_translate("mainSelectedSong", self.artist))
        self.label_3.setText(_translate("mainSelectedSong", "Album"))
        self.label_4.setText(_translate("mainSelectedSong", "Duration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainSelectedSong = QtWidgets.QMainWindow()
    ui = Ui_mainSelectedSong()
    ui.setupUi(mainSelectedSong)
    mainSelectedSong.show()
    sys.exit(app.exec_())

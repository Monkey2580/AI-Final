# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectedSong.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setStyleSheet("\n"
"border-radius:10px;\n"
" image: url(D:/College Stuff/Semester 8/Artificial Intelligence/FinalAI/next.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 10, 261, 31))
        self.lineEdit.setStyleSheet("border-radius:10px;\n"
"background-color:#c4c4c4;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 10, 121, 41))
        self.label.setStyleSheet("background-color:#c4c4c4;\n"
"border-radius:10px;\n"
"text-align: center;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 10, 93, 41))
        self.pushButton.setStyleSheet("border:1px solid black;\n"
"border-radius:10px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(50, 120, 351, 281))
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 110, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 150, 55, 16))
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
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(420, 240, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.star5 = QtWidgets.QPushButton(self.centralwidget)
        self.star5.setGeometry(QtCore.QRect(490, 270, 31, 16))
        self.star5.setStyleSheet(" image: url(D:/College Stuff/Semester 8/Artificial Intelligence/FinalAI/emptyStar.png);\n"
"background-color:transparent;")
        self.star5.setText("")
        self.star5.setObjectName("star5")
        self.star3 = QtWidgets.QPushButton(self.centralwidget)
        self.star3.setGeometry(QtCore.QRect(450, 270, 31, 16))
        self.star3.setStyleSheet(" image: url(D:/College Stuff/Semester 8/Artificial Intelligence/FinalAI/emptyStar.png);\n"
"background-color:transparent;")
        self.star3.setText("")
        self.star3.setObjectName("star3")
        self.star1 = QtWidgets.QPushButton(self.centralwidget)
        self.star1.setGeometry(QtCore.QRect(410, 270, 31, 16))
        self.star1.setStyleSheet(" image: url(D:/College Stuff/Semester 8/Artificial Intelligence/FinalAI/emptyStar.png);\n"
"background-color:transparent;")
        self.star1.setText("")
        self.star1.setObjectName("star1")
        self.star4 = QtWidgets.QPushButton(self.centralwidget)
        self.star4.setGeometry(QtCore.QRect(470, 270, 31, 16))
        self.star4.setStyleSheet(" image: url(D:/College Stuff/Semester 8/Artificial Intelligence/FinalAI/emptyStar.png);\n"
"background-color:transparent;")
        self.star4.setText("")
        self.star4.setObjectName("star4")
        self.star2 = QtWidgets.QPushButton(self.centralwidget)
        self.star2.setGeometry(QtCore.QRect(430, 270, 31, 16))
        self.star2.setStyleSheet(" image: url(D:/College Stuff/Semester 8/Artificial Intelligence/FinalAI/emptyStar.png);\n"
"background-color:transparent;")
        self.star2.setText("")
        self.star2.setObjectName("star2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "USER"))
        self.pushButton.setText(_translate("MainWindow", "LOGOUT"))
        self.label_5.setText(_translate("MainWindow", "Song Tittle"))
        self.label_2.setText(_translate("MainWindow", "Artist"))
        self.label_3.setText(_translate("MainWindow", "Description"))
        self.label_4.setText(_translate("MainWindow", "Description"))
        self.label_6.setText(_translate("MainWindow", "Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from dashboard import Ui_dashboardObject


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1011, 81))
        self.frame.setStyleSheet("background-color: #000000;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, -10, 111, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #ffffff;\n"
                                 "text-transform: bold;")
        self.label.setObjectName("label")
        self.login_btn = QtWidgets.QPushButton(self.frame)
        self.login_btn.setGeometry(QtCore.QRect(690, 20, 93, 41))
        self.login_btn.setStyleSheet("border:1px solid white;\n"
                                     "border-radius:10px;\n"
                                     "color: white;")
        self.login_btn.setObjectName("login_btn")
        self.login_username_input = QtWidgets.QLineEdit(self.frame)
        self.login_username_input.setGeometry(QtCore.QRect(420, 20, 261, 41))
        self.login_username_input.setStyleSheet("border-radius:10px;\n"
                                                "background-color:#c4c4c4;\n"
                                                "")
        self.login_username_input.setObjectName("login_username_input")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-160, 80, 1181, 601))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Background.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.login_btn.clicked.connect(self.dashboardscreen)

    def dashboardscreen(self):
        username = self.login_username_input.text()
        if username == 'aditya' or username == 'ADITYA':
            self.dashboardObject = QtWidgets.QMainWindow()
            self.message = username
            self.ui = Ui_dashboardObject(self.message)
            self.ui.setupUi(self.dashboardObject)
            self.dashboardObject.show()
        else:
            print('username not found')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Spofity"))
        self.login_btn.setText(_translate("MainWindow", "LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dashboardObject(object):
    def __init__(self, message):
        self.message = message
        print('currenct user:'+message)

    def setupUi(self, dashboardObject):
        dashboardObject.setObjectName("dashboardObject")
        dashboardObject.resize(800, 600)
        dashboardObject.setMinimumSize(QtCore.QSize(800, 600))
        dashboardObject.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(dashboardObject)
        self.centralwidget.setObjectName("centralwidget")
        self.logout_btn = QtWidgets.QPushButton(self.centralwidget)
        self.logout_btn.setGeometry(QtCore.QRect(690, 10, 93, 41))
        self.logout_btn.setStyleSheet("border:1px solid black;\n"
                                      "border-radius:10px;")
        self.logout_btn.setObjectName("logout_btn")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(550, 10, 121, 41))
        self.username_label.setStyleSheet("background-color:#c4c4c4;\n"
                                          "border-radius:10px;\n"
                                          "text-align: center;")
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.search_input = QtWidgets.QLineEdit(self.centralwidget)
        self.search_input.setGeometry(QtCore.QRect(40, 10, 261, 41))
        self.search_input.setStyleSheet("border-radius:10px;\n"
                                        "background-color:#c4c4c4;\n"
                                        "")
        self.search_input.setObjectName("search_input")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(-20, 130, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(310, 10, 93, 41))
        self.search_btn.setStyleSheet("border:1px solid black;\n"
                                      "border-radius:10px;")
        self.search_btn.setObjectName("search_btn")
        dashboardObject.setCentralWidget(self.centralwidget)

        self.retranslateUi(dashboardObject)
        QtCore.QMetaObject.connectSlotsByName(dashboardObject)
        self.logout_btn.clicked.connect(
            lambda: self.closeDashboardPage(dashboardObject))

    def closeDashboardPage(self, dashboardObject):
        dashboardObject.close()

    def retranslateUi(self, dashboardObject):
        _translate = QtCore.QCoreApplication.translate
        dashboardObject.setWindowTitle(
            _translate("dashboardObject", "MainWindow"))
        self.logout_btn.setText(_translate("dashboardObject", "LOGOUT"))
        self.username_label.setText(
            _translate("dashboardObject", self.message))
        self.label_11.setText(_translate(
            "dashboardObject", "WELCOME TO MAIN DASHBOARD"))
        self.search_btn.setText(_translate("dashboardObject", "SEARCH"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dashboardObject = QtWidgets.QMainWindow()
    ui = Ui_dashboardObject()
    ui.setupUi(dashboardObject)
    dashboardObject.show()
    sys.exit(app.exec_())

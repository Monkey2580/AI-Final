
from dashboard import Ui_dashboardObject
# from testCopas import Ui_MainWindow
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
import csv
import unicodedata

print("Hello World!")

filename = "C:/Users/m250321009/Documents/Aditya Mahendra/College Data/Artificial Intelligence/Final Assignment/adit-finalProject-test/SongCSV2012.csv"

with open(filename, 'r') as data:
    for line in csv.reader(data):
        print(line)


class loginWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_dashboardObject()
        self.ui.setupUi(lambda: self, dashboardObject)
        self.dashboardObject = QtWidgets.QMainWindow()

        self.logout_btn.clicked.connect(
            lambda: self.closedashboard(dashboardObject))

    def closedashboard(self, dashboardObject):
        dashboardObject.hide()

    def test(self):
        print("button is clicked!")


if __name__ == "__main__":
    import sys

    app = qtw.QApplication(sys.argv)
    widget = loginWindow()
    widget.show()
    app.exec_()

from selectedSongUI import Ui_MainWindow


from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

class loginWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.auth)
        self.ui.star1.clicked.connect(self.ratingFilledStars)
        self.ui.star2.clicked.connect(self.ratingFilledStars2)
        self.ui.star3.clicked.connect(self.ratingFilledStars3)
        self.ui.star4.clicked.connect(self.ratingFilledStars4)
        self.ui.star5.clicked.connect(self.ratingFilledStar5)
        self.stars = [self.ui.star1, self.ui.star2, self.ui.star3, self.ui.star4, self.ui.star5]
        self.rating = 0;
    def ratingFilledStars(self):
        self.ui.star1.setStyleSheet(
                             "qproperty-icon: url(filledStar.png);"
                            "background-color:transparent;"
                             );
        for i in range(1,5):
            self.stars[i].setStyleSheet(
                "qproperty-icon: url(emptyStar.png);"
                "background-color:transparent;"
            );
        self.rating = 1
    def auth(self):
            lol = ["akujulio","saya julio","aku julio2"]
            for x in lol:
                if "aku" in x:
                    print(x)
            print("The Rating: " + str(self.rating))
    def ratingFilledStars2(self):
        for i in range(0, 2):
            self.stars[i].setStyleSheet(
                "qproperty-icon: url(filledStar.png);"
                "background-color:transparent;"
            );
        for i in range(2, 5):
            self.stars[i].setStyleSheet(
                "qproperty-icon: url(emptyStar.png);"
                "background-color:transparent;"
            );
        self.rating = 2

    def ratingFilledStars3(self):
        for i in range(0, 3):
            self.stars[i].setStyleSheet(
                "qproperty-icon: url(filledStar.png);"
                "background-color:transparent;"
            );
        for i in range(3, 5):
            self.stars[i].setStyleSheet(
                "qproperty-icon: url(emptyStar.png);"
                "background-color:transparent;"
            );
        self.rating = 3

    def ratingFilledStars4(self):
        for i in range(0, 4):
            self.stars[i].setStyleSheet(
                "qproperty-icon: url(filledStar.png);"
                "background-color:transparent;"
            );
        for i in range(4, 5):
            self.stars[i].setStyleSheet(
                "qproperty-icon: url(emptyStar.png);"
                "background-color:transparent;"
            );
        self.rating = 4
    def ratingFilledStar5(self):
        for i in range(0, 5):
            self.stars[i].setStyleSheet(
                "qproperty-icon: url(filledStar.png);"
                "background-color:transparent;"
            );
        self.rating = 5


if __name__ == "__main__":
    import sys
    app = qtw.QApplication(sys.argv)
    widget= loginWindow()
    widget.show()
    app.exec_()
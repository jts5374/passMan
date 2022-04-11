import sys
import PyQt5
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import basicfunctions as bf

class MainWindow(QDialog):
    def __init__(self) :
        super(MainWindow, self).__init__()
        loadUi("C:\\Users\\JT\\Documents\\Python\\passMan\\GUI\\mainwindow.ui", self)
        self.label_2.setVisible(False)
        self.loginbtn.clicked.connect(self.loginbutton)

    def loginbutton(self):
        if not bf.check_password(self.passwordEdit.text(), self.usernameEdit.text()):
            self.label_2.setVisible(True)

# class Screen2(QDialog):
#     def __init__(self) :
#         super(Screen2, self).__init__()
#         loadUi("C:\\Users\\JT\\Documents\\Python\\MultiWindowApp\\screen2.ui", self)
#         self.pushButton.clicked.connect(self.gotoScreen1)

#     def gotoScreen1(self):
#         widget.setCurrentIndex(widget.currentIndex()-1)
    

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

mainwindow = MainWindow()
widget.addWidget(mainwindow)

widget.setFixedHeight(300)
widget.setFixedWidth(400)

widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")
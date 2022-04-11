from distutils.log import Log
import sys
import PyQt5
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import basicfunctions as bf


activeuser = bf.currentUser()


class MainWindow(QDialog):
    def __init__(self) :
        super(MainWindow, self).__init__()
        loadUi("C:\\Users\\JT\\Documents\\Python\\passMan\\GUI\\mainwindow.ui", self)
        self.label_2.setVisible(False)
        self.loginbtn.clicked.connect(self.loginbutton)
        self.createAccountbtn.clicked.connect(self.goToCreateAccount)
        

    def loginbutton(self):
        if not bf.check_password(self.passwordEdit.text(), self.usernameEdit.text()):
            self.label_2.setVisible(True)
        else :
            activeuser.login(self.usernameEdit.text(),self.passwordEdit.text())
            widget.setCurrentIndex(widget.currentIndex()+1)
    
    def goToCreateAccount(self):
        widget.setCurrentIndex(widget.currentIndex()+2)

class LoginSuccess(QDialog):
    def __init__(self) :
        super(LoginSuccess, self).__init__()
        loadUi("C:\\Users\\JT\\Documents\\Python\\passMan\\GUI\\loginsuccessful.ui", self)
        self.pushButton.clicked.connect(self.gotoScreen1)
        self.refreshbutton.clicked.connect(self.refreshbtn)
        self.hellouserlabel.setText('Hello {}'.format(activeuser.username))

    def refreshbtn(self):
        self.hellouserlabel.setText('Hello {}'.format(activeuser.username))

    def gotoScreen1(self):
        activeuser.logout()
        widget.setCurrentIndex(widget.currentIndex()-1)

class createAccount(QDialog):
    def __init__(self) :
        super(createAccount, self).__init__()
        loadUi("C:\\Users\\JT\\Documents\\Python\\passMan\\GUI\\createaccount.ui", self)
        self.createaccountbtn.clicked.connect(self.createaccount)
        self.returntoLoginbtn.clicked.connect(self.returntoLogin)
        self.warninglabel.setVisible(False)
    def createaccount(self):
        if self.capasswordedit.text() != self.confirmpasswordedit.text():
            self.warninglabel.setVisible(True)
    def returntoLogin(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

mainwindow = MainWindow()
loginsuccess = LoginSuccess()
createaccount = createAccount()
widget.addWidget(mainwindow)
widget.addWidget(loginsuccess)
widget.addWidget(createaccount)

widget.setFixedHeight(300)
widget.setFixedWidth(400)

widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")
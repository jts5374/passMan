from distutils.log import Log
import sys
import PyQt5
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import basicfunctions as bf
import os
import pyperclip

activeuser = bf.currentUser()


class MainWindow(QDialog):
    def __init__(self) :
        super(MainWindow, self).__init__()
        loadUi((os.path.join(os.getcwd(), 'GUI', 'mainwindow.ui')), self)
        bf.startup()
        self.label_2.setVisible(False)
        self.loginbtn.clicked.connect(self.loginbutton)
        self.createAccountbtn.clicked.connect(self.goToCreateAccount)
        

    def loginbutton(self):
        if bf.userexists(self.usernameEdit.text()):
            if not bf.check_password(self.passwordEdit.text(), self.usernameEdit.text()):
                self.label_2.setVisible(True)
            else :
                activeuser.login(self.usernameEdit.text(),self.passwordEdit.text())
                loginsuccess = LoginSuccess()
                widget.addWidget(loginsuccess)
                widget.setCurrentIndex(widget.currentIndex()+1)
                widget.removeWidget(self)
    
    def goToCreateAccount(self):
        createaccount = createAccount()
        widget.addWidget(createaccount)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(self)

class LoginSuccess(QDialog):  
    
    
    def __init__(self) :
        super(LoginSuccess, self).__init__()
        loadUi((os.path.join(os.getcwd(), 'GUI', "loginsuccessful.ui")), self)
        self.pushButton.clicked.connect(self.gotoScreen1)
        self.addupsaccountbutton.clicked.connect(self.gotoAddUpsAccount)
        self.copypasswordbtn.clicked.connect(self.copypassword)
        self.hellouserlabel.setText('Hello {}'.format(activeuser.username))
        self.tabledata = bf.get_all_userpasswords(activeuser.username)
        
        for item in self.tabledata:
            self.passwordscomboBox.addItem("Site:{} Username:{}".format(item[1], item[2]))

        self.removepasswordbutton.clicked.connect(self.removepassword)
    def gotoScreen1(self):
        activeuser.logout()
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(self)
    def copypassword(self):
        password = bf.get_encrypted_password(self.tabledata[self.passwordscomboBox.currentIndex()][0], activeuser.decryptkey)
        pyperclip.copy(password)

    def removepassword(self):
        
        bf.remove_ups_account(self.tabledata[self.passwordscomboBox.currentIndex()][0])
        
        loginsuccess = LoginSuccess()
        widget.addWidget(loginsuccess)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(self)

    def gotoAddUpsAccount(self):
        addupsaccount = AddUpsAccount()
        widget.addWidget(addupsaccount)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(self)

class createAccount(QDialog):
    def __init__(self) :
        super(createAccount, self).__init__()
        loadUi((os.path.join(os.getcwd(), 'GUI', 'createaccount.ui')), self)
        self.createaccountbtn.clicked.connect(self.createaccount)
        self.returntoLoginbtn.clicked.connect(self.returntoLogin)
        self.warninglabel.setVisible(False)
    def createaccount(self):
        if not bf.userexists(self.causernameEdit.text()):
            if self.capasswordedit.text() != self.confirmpasswordedit.text():
                self.warninglabel.setVisible(True)
            else:
                bf.add_user(self.causernameEdit.text(), self.capasswordedit.text())
                mainwindow = MainWindow()
                widget.addWidget(mainwindow)
                widget.setCurrentIndex(widget.currentIndex()+1)
                widget.removeWidget(self)
        
    def returntoLogin(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(self)

class AddUpsAccount(QDialog):
    def __init__(self):
        super(AddUpsAccount, self).__init__()
        loadUi((os.path.join(os.getcwd(), 'GUI', 'addupsaccount.ui')), self)
        self.addupsaccountbutton.clicked.connect(self.addaccount)
        self.backbutton.clicked.connect(self.goback)
    def addaccount(self):
        bf.add_passwords(self.siteedit.text(), self.unameedit.text(), self.pwordedit.text(), activeuser.username, activeuser.decryptkey)
        loginsuccess = LoginSuccess()
        widget.addWidget(loginsuccess)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(self)
        
    def goback(self):
        loginsuccess = LoginSuccess()
        widget.addWidget(loginsuccess)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(self)


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
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password_generator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


#from _typeshed import Self
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import random
import sqlite3


class Ui_MainWindow(object):
    # Main UI setup
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 481)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")

        # Top Label starts
        self.topLabel()
        # Top Label ends
        # Setup Password GroupBox Starts
        self.setupPasswordGroupBox()
        # Setup Password GroupBox Ends

        # Search GroupBox Starts
        self.searchGroupBox()
        # Search GroupBox Ends
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Top Label
    def topLabel(self):
        self.top_label = QtWidgets.QLabel(self.centralwidget)
        self.top_label.setGeometry(QtCore.QRect(220, 20, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(25)
        self.top_label.setFont(font)
        self.top_label.setStyleSheet("background-color: rgb(255, 255, 10);\n"
        "color: rgb(0, 0, 0);\n"
        "border-color: rgb(0, 0, 0);")
        self.top_label.setFrameShape(QtWidgets.QFrame.Box)
        self.top_label.setLineWidth(1)
        self.top_label.setAlignment(QtCore.Qt.AlignCenter)
        self.top_label.setObjectName("top_label")

    # Setup Password GroupBox    
    def setupPasswordGroupBox(self):
        self.setup_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.setup_groupBox.setGeometry(QtCore.QRect(30, 100, 361, 291))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.setup_groupBox.setFont(font)
        self.setup_groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.setup_groupBox.setFlat(False)
        self.setup_groupBox.setObjectName("setup_groupBox")
        # Username Input
        self.usernameInput()

        # Password Input
        self.passwordInput()

        # Website Input
        self.websiteInput()

        # Keyword Input
        self.keywordInput()
        
        # Submit Button
        self.submitBtn()

        # Cancel Button
        self.cancelBtn()
    
    # Username Input
    def usernameInput(self):
        self.username_lineEdit = QtWidgets.QLineEdit(self.setup_groupBox)
        self.username_lineEdit.setGeometry(QtCore.QRect(140, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.userName_label = QtWidgets.QLabel(self.setup_groupBox)
        self.userName_label.setGeometry(QtCore.QRect(40, 50, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userName_label.setFont(font)
        self.userName_label.setObjectName("userName_label")
    
    # Password Input
    def passwordInput(self):
        self.password_lineEdit = QtWidgets.QLineEdit(self.setup_groupBox)
        self.password_lineEdit.setGeometry(QtCore.QRect(140, 90, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.password_label = QtWidgets.QLabel(self.setup_groupBox)
        self.password_label.setGeometry(QtCore.QRect(40, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
    
    # Website Input
    def websiteInput(self):
        self.website_label = QtWidgets.QLabel(self.setup_groupBox)
        self.website_label.setGeometry(QtCore.QRect(50, 150, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.website_label.setFont(font)
        self.website_label.setObjectName("website_label")
        self.website_lineEdit = QtWidgets.QLineEdit(self.setup_groupBox)
        self.website_lineEdit.setGeometry(QtCore.QRect(140, 140, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.website_lineEdit.setFont(font)
        self.website_lineEdit.setObjectName("website_lineEdit")
    
    # Keyword Input
    def keywordInput(self):
        self.label_5 = QtWidgets.QLabel(self.setup_groupBox)
        self.label_5.setGeometry(QtCore.QRect(50, 200, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.keyword_lineEdit = QtWidgets.QLineEdit(self.setup_groupBox)
        self.keyword_lineEdit.setGeometry(QtCore.QRect(140, 190, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.keyword_lineEdit.setFont(font)
        self.keyword_lineEdit.setObjectName("keyword_lineEdit")

    # Submit Button
    def submitBtn(self):
        self.submit_pushButton = QtWidgets.QPushButton(self.setup_groupBox)
        self.submit_pushButton.setGeometry(QtCore.QRect(170, 240, 81, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submit_pushButton.setFont(font)
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.submit_pushButton.clicked.connect(self.onSubmit)

    # Cancel Button
    def cancelBtn(self):
        self.cancel_pushButton = QtWidgets.QPushButton(self.setup_groupBox)
        self.cancel_pushButton.setGeometry(QtCore.QRect(250, 240, 81, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_pushButton.setFont(font)
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.cancel_pushButton.clicked.connect(self.onCancel)
    
    # OnSubmit Action
    def onSubmit(self):
        print("submited")
        # User Inputs
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        website = self.website_lineEdit.text()
        keyword = self.keyword_lineEdit.text()

        # Checks base conditions
        hasNumber = False
        hasUpperCase = False
        hasLowerCase = False
        hasSpecialCharacters = False
        hasAcceptedLength = len(password) >= 8
        special_characters = '!@#$%^&*()?/|\{[]}~`_-+=><,.'

        for i in range(len(password)):
            char = password[i]
            if char.isdigit():
                hasNumber = True
                print('pass number check')
            elif char.isupper():
                hasUpperCase = True
                print('pass upper check')
            elif char.islower():
                hasLowerCase = True
                print('pass lower check')
            elif char in special_characters:
                hasSpecialCharacters = True
                print('pass special character check')
        
        if hasNumber == True and hasUpperCase == True and hasLowerCase == True and hasSpecialCharacters == True and hasAcceptedLength:
            conn = sqlite3.connect('password.sqlite')
            cur = conn.cursor()
            try:
                task = (username, password, website)
                result = cur.execute('INSERT INTO password (username, password, website) VALUES (?,?,?)', task)
                #result = cur.fetchall()

                if result:
                    print(result)
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setText("Entry Successful")#to set a text in Qmessagebox
                    msgBox.setWindowTitle("Password Manager")
                    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    returnValue = msgBox.exec()
                else:
                    print(result)
            except:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setWindowTitle("Password Manager")
                msgBox.setText("An Error Occured, trying to connect to database")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)    
                returnValue = msgBox.exec()
            conn.commit()
            conn.close()
        else:
            special="!@#$%^&*()?/|\{[]}~`_-+=><,."
            suggest=""
            i=0
            while i<4:
                #to check whether given keyword by the user has len >8
                while len(keyword) < 8:
                    #generates a Alphabet using random numbers generated with a range of ASCII Values
                    keyword = keyword + chr(random.randint(ord('a'),ord('z')))
                keyword += str(random.randint(0,9))
                #used to generate a char in a specfic set of elements
                keyword+=str(random.choice(special))
                #to capitalize first letter of word
                keyword = keyword.capitalize()
                suggest += keyword + '\n'
                i= i + 1
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("Password Manager")
            msgBox.setText("Your password didn't meet the standards.")
            suggestion="Your password should meet the conditions mentions below \n 1. At least 1 Uppercase \n 2. At least 1 lower case \n 3. At least 1 number \n 4. At least 1 special character \n 5. At least 8 characters."
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            #show a msg in the qmsg box
            msgBox.setInformativeText("Password Suggestions: \n"+str(suggest))
            #to create a hide details option in the msg box
            msgBox.setDetailedText(suggestion)
            msgBox.exec()


    # OnCancel Action
    def onCancel(self):
        self.username_lineEdit.setText('')
        self.password_lineEdit.setText('')
        self.website_lineEdit.setText('')
        self.keyword_lineEdit.setText('')

    # Search GroupBox  
    def searchGroupBox(self):
        self.search_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.search_groupBox.setGeometry(QtCore.QRect(410, 100, 361, 291))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.search_groupBox.setFont(font)
        self.search_groupBox.setObjectName("search_groupBox")
        # Passcode Input
        self.passcodeInput()
        
        # Search Website Input
        self.searchWebsiteInput()

        # Result Text
        self.resultTextbox()

        # Search Button
        self.searchBtn()

        # Cancel Button
        self.cancelSearchBtn()

    # Search Website Input
    def searchWebsiteInput(self):
        self.search_website_label = QtWidgets.QLabel(self.search_groupBox)
        self.search_website_label.setGeometry(QtCore.QRect(60, 50, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_website_label.setFont(font)
        self.search_website_label.setObjectName("search_website_label")
        self.search_website_lineEdit = QtWidgets.QLineEdit(self.search_groupBox)
        self.search_website_lineEdit.setGeometry(QtCore.QRect(140, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_website_lineEdit.setFont(font)
        self.search_website_lineEdit.setObjectName("search_website_lineEdit")
    
    # Passcode Input
    def passcodeInput(self):
        self.passcode_lineEdit = QtWidgets.QLineEdit(self.search_groupBox)
        self.passcode_lineEdit.setGeometry(QtCore.QRect(140, 90, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passcode_lineEdit.setFont(font)
        self.passcode_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passcode_lineEdit.setObjectName("passcode_lineEdit")
        self.passcode_label = QtWidgets.QLabel(self.search_groupBox)
        self.passcode_label.setGeometry(QtCore.QRect(50, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passcode_label.setFont(font)
        self.passcode_label.setObjectName("passcode_label")

    # Result Textbox
    def resultTextbox(self):
        print('Result Text Box')
        self.result_textEdit = QtWidgets.QTextEdit(self.search_groupBox)
        self.result_textEdit.setGeometry(QtCore.QRect(40, 140, 291, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_textEdit.setFont(font)
        self.result_textEdit.setObjectName("result_textEdit")

    # search Button
    def searchBtn(self):
        self.search_pushButton = QtWidgets.QPushButton(self.search_groupBox)
        self.search_pushButton.setGeometry(QtCore.QRect(170, 240, 81, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_pushButton.setFont(font)
        self.search_pushButton.setObjectName("search_pushButton")
        self.search_pushButton.clicked.connect(self.onSearch)
    
    # Cancel Search Button
    def cancelSearchBtn(self):
        self.cancel_pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_pushButton_2.setGeometry(QtCore.QRect(660, 340, 81, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_pushButton_2.setFont(font)
        self.cancel_pushButton_2.setObjectName("cancel_pushButton_2")
        self.cancel_pushButton_2.clicked.connect(self.onCancelSearch)
    
    # OnSearch Action
    def onSearch(self):
        passcode = self.passcode_lineEdit.text()
        website = self.search_website_lineEdit.text()

        # if users enters root only the search buttons works
        if passcode == 'root':
            conn = sqlite3.connect('password.sqlite')
            cur = conn.cursor()
            try:
                # fetching username and password using website name
                cur.execute("SELECT * FROM password WHERE website=?", [website])

                results = cur.fetchall()

                if results:
                    print(results)
                else:
                    print(results)
                message="Username \t Password \n\n"
            
                #show a msg in the qmsg box
                #msgBox.setInformativeText("Password Suggestions: \n"+str(suggest))
                for result in results:
                    message += str(result[0]) + "\t" + str(result[1]) + "\n"
                
                self.result_textEdit.setText("Passsword Info \n=============\n\n" + message)
            except:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setWindowTitle("Password Manager")
                msgBox.setText("An Error Occured, trying to connect to database")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)    
                msgBox.exec()

            conn.commit()
            conn.close()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setWindowTitle("Password Manager")
            msgBox.setText("Wrong password. Please try again!!")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)    
            msgBox.exec()

    # OnCancel Action
    def onCancelSearch(self):
        self.result_textEdit.setText('')
        self.passcode_lineEdit.setText('')
        self.search_website_lineEdit.setText('')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Manager"))
        self.setup_groupBox.setTitle(_translate("MainWindow", "Setup Password"))
        self.userName_label.setText(_translate("MainWindow", "Username :"))
        self.password_label.setText(_translate("MainWindow", "Password :"))
        self.website_label.setText(_translate("MainWindow", "Website :"))
        self.label_5.setText(_translate("MainWindow", "Keyword :"))
        self.submit_pushButton.setText(_translate("MainWindow", "Submit"))
        self.cancel_pushButton.setText(_translate("MainWindow", "Cancel"))
        self.top_label.setText(_translate("MainWindow", "Password Manager"))
        self.search_groupBox.setTitle(_translate("MainWindow", "Search"))
        self.passcode_label.setText(_translate("MainWindow", "Passcode :"))
        self.search_website_label.setText(_translate("MainWindow", "Website :"))
        self.search_pushButton.setText(_translate("MainWindow", "Search"))
        self.cancel_pushButton_2.setText(_translate("MainWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

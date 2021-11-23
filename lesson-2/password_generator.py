# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password_generator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 481)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")
        self.setup_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.setup_groupBox.setGeometry(QtCore.QRect(30, 100, 361, 291))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.setup_groupBox.setFont(font)
        self.setup_groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.setup_groupBox.setFlat(False)
        self.setup_groupBox.setObjectName("setup_groupBox")
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
        self.submit_pushButton = QtWidgets.QPushButton(self.setup_groupBox)
        self.submit_pushButton.setGeometry(QtCore.QRect(170, 240, 81, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submit_pushButton.setFont(font)
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.cancel_pushButton = QtWidgets.QPushButton(self.setup_groupBox)
        self.cancel_pushButton.setGeometry(QtCore.QRect(250, 240, 81, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_pushButton.setFont(font)
        self.cancel_pushButton.setObjectName("cancel_pushButton")
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
        self.search_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.search_groupBox.setGeometry(QtCore.QRect(410, 100, 361, 291))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.search_groupBox.setFont(font)
        self.search_groupBox.setObjectName("search_groupBox")
        self.passcode_lineEdit = QtWidgets.QLineEdit(self.search_groupBox)
        self.passcode_lineEdit.setGeometry(QtCore.QRect(140, 90, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passcode_lineEdit.setFont(font)
        self.passcode_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passcode_lineEdit.setObjectName("passcode_lineEdit")
        self.password_label_2 = QtWidgets.QLabel(self.search_groupBox)
        self.password_label_2.setGeometry(QtCore.QRect(50, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_label_2.setFont(font)
        self.password_label_2.setObjectName("password_label_2")
        self.userName_label_2 = QtWidgets.QLabel(self.search_groupBox)
        self.userName_label_2.setGeometry(QtCore.QRect(60, 50, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userName_label_2.setFont(font)
        self.userName_label_2.setObjectName("userName_label_2")
        self.search_website_lineEdit = QtWidgets.QLineEdit(self.search_groupBox)
        self.search_website_lineEdit.setGeometry(QtCore.QRect(140, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_website_lineEdit.setFont(font)
        self.search_website_lineEdit.setObjectName("search_website_lineEdit")
        self.result_textEdit = QtWidgets.QTextEdit(self.search_groupBox)
        self.result_textEdit.setGeometry(QtCore.QRect(40, 140, 291, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result_textEdit.setFont(font)
        self.result_textEdit.setObjectName("result_textEdit")
        self.search_pushButton = QtWidgets.QPushButton(self.search_groupBox)
        self.search_pushButton.setGeometry(QtCore.QRect(170, 240, 81, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_pushButton.setFont(font)
        self.search_pushButton.setObjectName("search_pushButton")
        self.cancel_pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_pushButton_2.setGeometry(QtCore.QRect(660, 340, 81, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_pushButton_2.setFont(font)
        self.cancel_pushButton_2.setObjectName("cancel_pushButton_2")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Generator"))
        self.setup_groupBox.setTitle(_translate("MainWindow", "Setup Password"))
        self.userName_label.setText(_translate("MainWindow", "Username :"))
        self.password_label.setText(_translate("MainWindow", "Password :"))
        self.website_label.setText(_translate("MainWindow", "Website :"))
        self.label_5.setText(_translate("MainWindow", "Keyword :"))
        self.submit_pushButton.setText(_translate("MainWindow", "Submit"))
        self.cancel_pushButton.setText(_translate("MainWindow", "Cancel"))
        self.top_label.setText(_translate("MainWindow", "Password Generator"))
        self.search_groupBox.setTitle(_translate("MainWindow", "Search"))
        self.password_label_2.setText(_translate("MainWindow", "Passcode :"))
        self.userName_label_2.setText(_translate("MainWindow", "Website :"))
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

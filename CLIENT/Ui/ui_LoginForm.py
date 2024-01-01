# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginFormBLckSp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_login_rc
from ui_UserForm8 import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(504, 329)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.UsernameInput = QLineEdit(self.centralwidget)
        self.UsernameInput.setObjectName(u"UsernameInput")
        self.UsernameInput.setGeometry(QRect(170, 106, 281, 41))
        self.UsernameInput.setStyleSheet(u"QLineEdit#UsernameInput\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgba(0, 0, 0, 100);\n"
"	padding: 10px;\n"
"	padding-left: 17px;\n"
"	font: 14pt \"Terminal\";\n"
"}\n"
"QLineEdit#UsernameInput:hover\n"
"{\n"
"\n"
"}")
        self.LoginButton = QPushButton(self.centralwidget)
        self.LoginButton.setObjectName(u"LoginButton")
        self.LoginButton.setGeometry(QRect(210, 250, 241, 41))
        self.LoginButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.LoginButton.setStyleSheet(u"QPushButton#LoginButton\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgba(0, 0, 0, 100);\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 14pt \"Terminal\";\n"
"}\n"
"QPushButton#LoginButton:hover\n"
"{\n"
"	background-color: rgb(244, 244, 244);\n"
"}")
        
        self.UsernameLabel = QLabel(self.centralwidget)
        self.UsernameLabel.setObjectName(u"UsernameLabel")
        self.UsernameLabel.setGeometry(QRect(50, 106, 91, 41))
        self.UsernameLabel.setStyleSheet(u"font: 14pt \"Terminal\";")
        self.UsernameLabel.setWordWrap(True)
        self.PasswordInput = QLineEdit(self.centralwidget)
        self.PasswordInput.setObjectName(u"PasswordInput")
        self.PasswordInput.setGeometry(QRect(170, 175, 281, 42))
        self.PasswordInput.setStyleSheet(u"QLineEdit#PasswordInput\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgba(0, 0, 0, 100);\n"
"	padding: 10px;\n"
"	padding-left: 17px;\n"
"	font: 14pt \"Terminal\";\n"
"}\n"
"QLineEdit#PasswordInput:hover\n"
"{\n"
"\n"
"}")
        self.PasswordInput.setEchoMode(QLineEdit.Password)
        self.RoleLabel = QLabel(self.centralwidget)
        self.RoleLabel.setObjectName(u"RoleLabel")
        self.RoleLabel.setGeometry(QRect(50, 36, 101, 41))
        self.RoleLabel.setStyleSheet(u"font: 14pt \"Terminal\";")
        self.RoleLabel.setAlignment(Qt.AlignCenter)
        self.RoleLabel.setWordWrap(True)
        self.PasswordLabel = QLabel(self.centralwidget)
        self.PasswordLabel.setObjectName(u"PasswordLabel")
        self.PasswordLabel.setGeometry(QRect(50, 176, 91, 41))
        self.PasswordLabel.setStyleSheet(u"font: 14pt \"Terminal\";")
        self.PasswordLabel.setWordWrap(True)
        self.RoleComboBox = QComboBox(self.centralwidget)
        self.RoleComboBox.addItem("")
        self.RoleComboBox.addItem("")
        self.RoleComboBox.addItem("")
        self.RoleComboBox.setObjectName(u"RoleComboBox")
        self.RoleComboBox.setGeometry(QRect(170, 36, 281, 41))
        self.RoleComboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.RoleComboBox.setStyleSheet(u"QComboBox#RoleComboBox\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgba(0, 0, 0, 100);\n"
"	padding: 10px;\n"
"	padding-left: 17px;\n"
"	font: 14pt \"Terminal\";\n"
"}\n"
"QComboBox#RoleComboBox:hover\n"
"{\n"
"	background-color: rgb(244, 244, 244);\n"
"}\n"
"QComboBox#RoleComboBox::drop-down:button\n"
"{\n"
"	border-radius:20px;\n"
"}")
        self.ShowButton = QPushButton(self.centralwidget)
        self.ShowButton.setObjectName(u"ShowButton")
        self.ShowButton.setGeometry(QRect(400, 176, 50, 40))
        self.ShowButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ShowButton.setAutoFillBackground(False)
        self.ShowButton.setStyleSheet(u"QPushButton#ShowButton\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 0px solid rgba(0, 0, 0, 100);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	font: 14pt \"Terminal\";\n"
"}\n"
"QPushButton#ShowButton:hover\n"
"{\n"
"	background-color: rgb(244, 244, 244);\n"
"}")
        icon = QIcon()
        icon.addFile(u"view.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"hide.png", QSize(), QIcon.Active, QIcon.Off)
        self.ShowButton.setIcon(icon)
        self.ShowButton.setIconSize(QSize(23, 23))
        self.ShowButton.setAutoRepeat(True)
        self.DropDownImg = QLabel(self.centralwidget)
        self.DropDownImg.setObjectName(u"DropDownImg")
        self.DropDownImg.setGeometry(QRect(416, 46, 20, 20))
        self.DropDownImg.setStyleSheet(u"")
        self.DropDownImg.setPixmap(QPixmap(u":/icons/EC8482/chevron-down.svg"))
        self.DropDownImg.setScaledContents(True)
        self.RegisterButton = QPushButton(self.centralwidget)
        self.RegisterButton.setObjectName(u"RegisterButton")
        self.RegisterButton.setGeometry(QRect(50, 250, 141, 41))
        self.RegisterButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.RegisterButton.setStyleSheet(u"QPushButton#RegisterButton\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgba(0, 0, 0, 100);\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 14pt \"Terminal\";\n"
"}\n"
"QPushButton#RegisterButton:hover\n"
"{\n"
"	background-color: rgb(244, 244, 244);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.UsernameLabel.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.PasswordInput.setText("")
        self.RoleLabel.setText(QCoreApplication.translate("MainWindow", u"Your Role:", None))
        self.PasswordLabel.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.RoleComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Admin", None))
        self.RoleComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"User", None))
        self.RoleComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Creater", None))

        self.ShowButton.setText("")
        self.DropDownImg.setText("")
        self.RegisterButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
    # retranslateUi


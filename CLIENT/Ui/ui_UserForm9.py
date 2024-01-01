# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserFormLsSODs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget

import resources_rc

class Ui_UserWindow(object):
    def setupUi(self, UserWindow):
        if not UserWindow.objectName():
            UserWindow.setObjectName(u"UserWindow")
        UserWindow.resize(1262, 748)
        UserWindow.setStyleSheet(u"* {\n"
"	border:none;\n"
"	background-color: transparent;\n"
"	background:transparent;\n"
"	padding:0;\n"
"	margin:0;\n"
"	color:#fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"#leftMenuSubContainer{\n"
"	background-color: #16191d;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align:left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuSubContainer, #rightMenuSubContainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"#headerCenterMenu, #rightMenuBar, #popupNotificationSubContainer{\n"
"	background-color: #16191d;\n"
"	border-radius: 10px;\n"
"}\n"
"#headerContainer, #footerContainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(UserWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.UserWidget = QWidget(self.centralwidget)
        self.UserWidget.setObjectName(u"UserWidget")
        self.UserWidget.setGeometry(QRect(0, 0, 1265, 743))
        self.horizontalLayout = QHBoxLayout(self.UserWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftMenuContainer = QCustomSlideMenu(self.UserWidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMinimumSize(QSize(200, 0))
        self.leftMenuContainer.setMaximumSize(QSize(55, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(100)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.menuBar = QFrame(self.leftMenuSubContainer)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setFrameShape(QFrame.StyledPanel)
        self.menuBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menuBar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 5)
        self.menuBtn = QPushButton(self.menuBar)
        self.menuBtn.setObjectName(u"menuBtn")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menuBtn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/EC8482/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.menuBar, 0, Qt.AlignTop)

        self.navBar = QFrame(self.leftMenuSubContainer)
        self.navBar.setObjectName(u"navBar")
        self.navBar.setFrameShape(QFrame.StyledPanel)
        self.navBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.navBar)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.Nav_H_Spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.Nav_H_Spacer)

        self.homeBtn = QPushButton(self.navBar)
        self.homeBtn.setObjectName(u"homeBtn")
        font1 = QFont()
        font1.setPointSize(10)
        self.homeBtn.setFont(font1)
        self.homeBtn.setStyleSheet(u"backgound-color: #1f232a;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/EC8482/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.homeBtn)

        self.libraryBtn = QPushButton(self.navBar)
        self.libraryBtn.setObjectName(u"libraryBtn")
        self.libraryBtn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/EC8482/github.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.libraryBtn.setIcon(icon2)
        self.libraryBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.libraryBtn)

        self.cartsBtn = QPushButton(self.navBar)
        self.cartsBtn.setObjectName(u"cartsBtn")
        self.cartsBtn.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/EC8482/shopping-cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cartsBtn.setIcon(icon3)
        self.cartsBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.cartsBtn)


        self.verticalLayout_2.addWidget(self.navBar, 0, Qt.AlignTop)

        self.Nav_O_Spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.Nav_O_Spacer)

        self.optionsBar = QFrame(self.leftMenuSubContainer)
        self.optionsBar.setObjectName(u"optionsBar")
        self.optionsBar.setFrameShape(QFrame.StyledPanel)
        self.optionsBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.optionsBar)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.optionsBar)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/EC8482/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon4)
        self.settingsBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.optionsBar)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/icons/EC8482/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon5)
        self.infoBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.optionsBar)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/icons/EC8482/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.optionsBar, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer)

        self.centerMenuContainer = QWidget(self.UserWidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(0, 0))
        self.centerMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.centerMenuContainer.setStyleSheet(u"border-radius: 10px;")
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QCustomSlideMenu(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(0, 0))
        self.verticalLayout_7 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.headerCenterMenu = QFrame(self.centerMenuSubContainer)
        self.headerCenterMenu.setObjectName(u"headerCenterMenu")
        self.headerCenterMenu.setFrameShape(QFrame.StyledPanel)
        self.headerCenterMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.headerCenterMenu)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.titleCenterMenu = QLabel(self.headerCenterMenu)
        self.titleCenterMenu.setObjectName(u"titleCenterMenu")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.titleCenterMenu.setFont(font2)
        self.titleCenterMenu.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.titleCenterMenu)

        self.closeCenterMenuBtn = QPushButton(self.headerCenterMenu)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/EC8482/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon7)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.headerCenterMenu, 0, Qt.AlignTop)

        self.centerMenuPages = QCustomQStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.centerMenuPages.setStyleSheet(u"")
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.horizontalLayout_3 = QHBoxLayout(self.settingsPage)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.settingsLabel = QLabel(self.settingsPage)
        self.settingsLabel.setObjectName(u"settingsLabel")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setWeight(50)
        self.settingsLabel.setFont(font3)
        self.settingsLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.settingsLabel)

        self.centerMenuPages.addWidget(self.settingsPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.horizontalLayout_5 = QHBoxLayout(self.helpPage)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.helpLabel = QLabel(self.helpPage)
        self.helpLabel.setObjectName(u"helpLabel")
        self.helpLabel.setFont(font3)
        self.helpLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.helpLabel)

        self.centerMenuPages.addWidget(self.helpPage)
        self.infoPage = QWidget()
        self.infoPage.setObjectName(u"infoPage")
        self.horizontalLayout_4 = QHBoxLayout(self.infoPage)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.infoLabel = QLabel(self.infoPage)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setFont(font3)
        self.infoLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.infoLabel)

        self.centerMenuPages.addWidget(self.infoPage)

        self.verticalLayout_7.addWidget(self.centerMenuPages)


        self.verticalLayout_6.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.UserWidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_7 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.appInfo = QFrame(self.headerContainer)
        self.appInfo.setObjectName(u"appInfo")
        self.appInfo.setFrameShape(QFrame.StyledPanel)
        self.appInfo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.appInfo)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.appIcon = QLabel(self.appInfo)
        self.appIcon.setObjectName(u"appIcon")
        self.appIcon.setMaximumSize(QSize(30, 30))
        self.appIcon.setStyleSheet(u"")
        self.appIcon.setPixmap(QPixmap(u":/images/icon-app-user.png"))
        self.appIcon.setScaledContents(True)
        self.appIcon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.appIcon)

        self.appTitle = QLabel(self.appInfo)
        self.appTitle.setObjectName(u"appTitle")
        self.appTitle.setFont(font2)

        self.horizontalLayout_8.addWidget(self.appTitle)


        self.horizontalLayout_7.addWidget(self.appInfo, 0, Qt.AlignLeft)

        self.userMenu = QFrame(self.headerContainer)
        self.userMenu.setObjectName(u"userMenu")
        self.userMenu.setFrameShape(QFrame.StyledPanel)
        self.userMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.userMenu)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.userMenu)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/EC8482/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon8)
        self.notificationBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.notificationBtn)

        self.moreMenuBtn = QPushButton(self.userMenu)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/EC8482/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon9)
        self.moreMenuBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.moreMenuBtn)

        self.profileMenuBtn = QPushButton(self.userMenu)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/EC8482/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileMenuBtn.setIcon(icon10)
        self.profileMenuBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.profileMenuBtn)


        self.horizontalLayout_7.addWidget(self.userMenu, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.windowOptions = QFrame(self.headerContainer)
        self.windowOptions.setObjectName(u"windowOptions")
        self.windowOptions.setFrameShape(QFrame.StyledPanel)
        self.windowOptions.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.windowOptions)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.windowOptions)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/EC8482/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon11)
        self.minimizeBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.windowOptions)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons/EC8482/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon12)
        self.restoreBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.windowOptions)
        self.closeBtn.setObjectName(u"closeBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/EC8482/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon13)
        self.closeBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.closeBtn)


        self.horizontalLayout_7.addWidget(self.windowOptions, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.headerContainer)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy1)
        self.mainBodyContent.setMinimumSize(QSize(931, 518))
        self.horizontalLayout_10 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.mainContentsContainer.setMinimumSize(QSize(0, 0))
        self.mainContentsContainer.setMaximumSize(QSize(1000, 16777215))
        self.verticalLayout_13 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.mainPages = QCustomQStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.mainPages.setMinimumSize(QSize(1000, 0))
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_14 = QVBoxLayout(self.homePage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.home_header = QWidget(self.homePage)
        self.home_header.setObjectName(u"home_header")
        self.home_header.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #fff;\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgba(0, 0, 0, 100);\n"
"	padding: 10px;\n"
"	padding-left: 17px;\n"
"	color: #rgb(0,255,255);\n"
"}\n"
"QPushButton\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgba(0, 0, 0, 100);\n"
"	font: 14pt \"Terminal\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(244, 244, 244);\n"
"}")
        self.home_search_line = QLineEdit(self.home_header)
        self.home_search_line.setObjectName(u"home_search_line")
        self.home_search_line.setEnabled(True)
        self.home_search_line.setGeometry(QRect(440, 10, 351, 42))
        font4 = QFont()
        font4.setFamily(u"Terminal")
        font4.setPointSize(15)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.home_search_line.setFont(font4)
        self.home_search_line.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.home_search_label = QLabel(self.home_header)
        self.home_search_label.setObjectName(u"home_search_label")
        self.home_search_label.setGeometry(QRect(320, 20, 111, 30))
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(False)
        font5.setWeight(50)
        self.home_search_label.setFont(font5)
        self.home_search_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.home_search_btn = QPushButton(self.home_header)
        self.home_search_btn.setObjectName(u"home_search_btn")
        self.home_search_btn.setGeometry(QRect(800, 10, 161, 41))
        font6 = QFont()
        font6.setFamily(u"Terminal")
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.home_search_btn.setFont(font6)
        self.home_search_btn.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        icon14 = QIcon()
        icon14.addFile(u":/icons/EC8482/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_search_btn.setIcon(icon14)
        self.home_game_btn1 = QPushButton(self.home_header)
        self.home_game_btn1.setObjectName(u"home_game_btn1")
        self.home_game_btn1.setGeometry(QRect(10, 70, 121, 171))
        self.home_game_btn1.setFont(font6)
        self.home_game_btn1.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        icon15 = QIcon()
        icon15.addFile(u"../../../../../../DLcghhhiinnotu/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_game_btn1.setIcon(icon15)
        self.home_game_btn1.setIconSize(QSize(115, 115))
        self.home_game_btn1.setAutoRepeat(False)
        self.home_game_btn2 = QPushButton(self.home_header)
        self.home_game_btn2.setObjectName(u"home_game_btn2")
        self.home_game_btn2.setGeometry(QRect(160, 70, 121, 171))
        self.home_game_btn2.setFont(font6)
        self.home_game_btn2.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.home_game_btn2.setIcon(icon15)
        self.home_game_btn2.setIconSize(QSize(115, 115))
        self.home_game_btn3 = QPushButton(self.home_header)
        self.home_game_btn3.setObjectName(u"home_game_btn3")
        self.home_game_btn3.setGeometry(QRect(310, 70, 121, 171))
        self.home_game_btn3.setFont(font6)
        self.home_game_btn3.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.home_game_btn3.setIcon(icon15)
        self.home_game_btn3.setIconSize(QSize(115, 115))
        self.home_game_btn6 = QPushButton(self.home_header)
        self.home_game_btn6.setObjectName(u"home_game_btn6")
        self.home_game_btn6.setGeometry(QRect(760, 70, 121, 171))
        self.home_game_btn6.setFont(font6)
        self.home_game_btn6.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.home_game_btn6.setIcon(icon15)
        self.home_game_btn6.setIconSize(QSize(115, 115))
        self.home_game_btn5 = QPushButton(self.home_header)
        self.home_game_btn5.setObjectName(u"home_game_btn5")
        self.home_game_btn5.setGeometry(QRect(610, 70, 121, 171))
        self.home_game_btn5.setFont(font6)
        self.home_game_btn5.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.home_game_btn5.setIcon(icon15)
        self.home_game_btn5.setIconSize(QSize(115, 115))
        self.home_game_btn4 = QPushButton(self.home_header)
        self.home_game_btn4.setObjectName(u"home_game_btn4")
        self.home_game_btn4.setGeometry(QRect(460, 70, 121, 171))
        self.home_game_btn4.setFont(font6)
        self.home_game_btn4.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.home_game_btn4.setIcon(icon15)
        self.home_game_btn4.setIconSize(QSize(115, 115))
        self.home_game_btn12 = QPushButton(self.home_header)
        self.home_game_btn12.setObjectName(u"home_game_btn12")
        self.home_game_btn12.setGeometry(QRect(760, 330, 121, 171))
        self.home_game_btn12.setFont(font6)
        self.home_game_btn12.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.home_game_btn12.setIcon(icon15)
        self.home_game_btn12.setIconSize(QSize(115, 115))
        self.home_game_btn9 = QPushButton(self.home_header)
        self.home_game_btn9.setObjectName(u"home_game_btn9")
        self.home_game_btn9.setGeometry(QRect(310, 330, 121, 171))
        self.home_game_btn9.setFont(font6)
        self.home_game_btn9.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.home_game_btn9.setIcon(icon15)
        self.home_game_btn9.setIconSize(QSize(115, 115))
        self.home_game_btn10 = QPushButton(self.home_header)
        self.home_game_btn10.setObjectName(u"home_game_btn10")
        self.home_game_btn10.setGeometry(QRect(460, 330, 121, 171))
        self.home_game_btn10.setFont(font6)
        self.home_game_btn10.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.home_game_btn10.setIcon(icon15)
        self.home_game_btn10.setIconSize(QSize(115, 115))
        self.home_game_btn8 = QPushButton(self.home_header)
        self.home_game_btn8.setObjectName(u"home_game_btn8")
        self.home_game_btn8.setGeometry(QRect(160, 330, 121, 171))
        self.home_game_btn8.setFont(font6)
        self.home_game_btn8.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.home_game_btn8.setIcon(icon15)
        self.home_game_btn8.setIconSize(QSize(115, 115))
        self.home_game_btn7 = QPushButton(self.home_header)
        self.home_game_btn7.setObjectName(u"home_game_btn7")
        self.home_game_btn7.setGeometry(QRect(10, 330, 121, 171))
        self.home_game_btn7.setFont(font6)
        self.home_game_btn7.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.home_game_btn7.setIcon(icon15)
        self.home_game_btn7.setIconSize(QSize(115, 115))
        self.home_game_btn11 = QPushButton(self.home_header)
        self.home_game_btn11.setObjectName(u"home_game_btn11")
        self.home_game_btn11.setGeometry(QRect(610, 330, 121, 171))
        self.home_game_btn11.setFont(font6)
        self.home_game_btn11.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.home_game_btn11.setIcon(icon15)
        self.home_game_btn11.setIconSize(QSize(115, 115))
        self.home_more_game_btn = QPushButton(self.home_header)
        self.home_more_game_btn.setObjectName(u"home_more_game_btn")
        self.home_more_game_btn.setGeometry(QRect(890, 500, 71, 41))
        self.home_more_game_btn.setFont(font6)
        self.home_more_game_btn.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 255, 255);")
        icon16 = QIcon()
        icon16.addFile(u":/icons/EC8482/chevrons-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_more_game_btn.setIcon(icon16)
        self.home_more_game_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_14.addWidget(self.home_header)

        self.mainPages.addWidget(self.homePage)
        self.libraryPage = QWidget()
        self.libraryPage.setObjectName(u"libraryPage")
        self.verticalLayout_15 = QVBoxLayout(self.libraryPage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.library_header = QWidget(self.libraryPage)
        self.library_header.setObjectName(u"library_header")
        self.library_header.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #fff;\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgba(0, 0, 0, 100);\n"
"	padding: 10px;\n"
"	padding-left: 17px;\n"
"	color: #rgb(0,255,255);\n"
"}\n"
"QPushButton\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgba(0, 0, 0, 100);\n"
"	font: 14pt \"Terminal\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(244, 244, 244);\n"
"}")
        self.library_search_line = QLineEdit(self.library_header)
        self.library_search_line.setObjectName(u"library_search_line")
        self.library_search_line.setEnabled(True)
        self.library_search_line.setGeometry(QRect(440, 10, 351, 42))
        self.library_search_line.setFont(font4)
        self.library_search_line.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.library_search_label = QLabel(self.library_header)
        self.library_search_label.setObjectName(u"library_search_label")
        self.library_search_label.setGeometry(QRect(320, 20, 111, 30))
        self.library_search_label.setFont(font5)
        self.library_search_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.library_search_btn = QPushButton(self.library_header)
        self.library_search_btn.setObjectName(u"library_search_btn")
        self.library_search_btn.setGeometry(QRect(800, 10, 161, 41))
        self.library_search_btn.setFont(font6)
        self.library_search_btn.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.library_search_btn.setIcon(icon14)
        self.library_game_btn1 = QPushButton(self.library_header)
        self.library_game_btn1.setObjectName(u"library_game_btn1")
        self.library_game_btn1.setGeometry(QRect(10, 70, 121, 171))
        self.library_game_btn1.setFont(font6)
        self.library_game_btn1.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.library_game_btn1.setIcon(icon15)
        self.library_game_btn1.setIconSize(QSize(115, 115))
        self.library_game_btn1.setAutoRepeat(False)
        self.library_game_btn2 = QPushButton(self.library_header)
        self.library_game_btn2.setObjectName(u"library_game_btn2")
        self.library_game_btn2.setGeometry(QRect(160, 70, 121, 171))
        self.library_game_btn2.setFont(font6)
        self.library_game_btn2.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.library_game_btn2.setIcon(icon15)
        self.library_game_btn2.setIconSize(QSize(115, 115))
        self.library_game_btn3 = QPushButton(self.library_header)
        self.library_game_btn3.setObjectName(u"library_game_btn3")
        self.library_game_btn3.setGeometry(QRect(310, 70, 121, 171))
        self.library_game_btn3.setFont(font6)
        self.library_game_btn3.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.library_game_btn3.setIcon(icon15)
        self.library_game_btn3.setIconSize(QSize(115, 115))
        self.library_game_btn6 = QPushButton(self.library_header)
        self.library_game_btn6.setObjectName(u"library_game_btn6")
        self.library_game_btn6.setGeometry(QRect(760, 70, 121, 171))
        self.library_game_btn6.setFont(font6)
        self.library_game_btn6.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.library_game_btn6.setIcon(icon15)
        self.library_game_btn6.setIconSize(QSize(115, 115))
        self.library_game_btn5 = QPushButton(self.library_header)
        self.library_game_btn5.setObjectName(u"library_game_btn5")
        self.library_game_btn5.setGeometry(QRect(610, 70, 121, 171))
        self.library_game_btn5.setFont(font6)
        self.library_game_btn5.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.library_game_btn5.setIcon(icon15)
        self.library_game_btn5.setIconSize(QSize(115, 115))
        self.library_game_btn4 = QPushButton(self.library_header)
        self.library_game_btn4.setObjectName(u"library_game_btn4")
        self.library_game_btn4.setGeometry(QRect(460, 70, 121, 171))
        self.library_game_btn4.setFont(font6)
        self.library_game_btn4.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.library_game_btn4.setIcon(icon15)
        self.library_game_btn4.setIconSize(QSize(115, 115))
        self.library_game_btn12 = QPushButton(self.library_header)
        self.library_game_btn12.setObjectName(u"library_game_btn12")
        self.library_game_btn12.setGeometry(QRect(760, 330, 121, 171))
        self.library_game_btn12.setFont(font6)
        self.library_game_btn12.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.library_game_btn12.setIcon(icon15)
        self.library_game_btn12.setIconSize(QSize(115, 115))
        self.library_game_btn9 = QPushButton(self.library_header)
        self.library_game_btn9.setObjectName(u"library_game_btn9")
        self.library_game_btn9.setGeometry(QRect(310, 330, 121, 171))
        self.library_game_btn9.setFont(font6)
        self.library_game_btn9.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.library_game_btn9.setIcon(icon15)
        self.library_game_btn9.setIconSize(QSize(115, 115))
        self.library_game_btn10 = QPushButton(self.library_header)
        self.library_game_btn10.setObjectName(u"library_game_btn10")
        self.library_game_btn10.setGeometry(QRect(460, 330, 121, 171))
        self.library_game_btn10.setFont(font6)
        self.library_game_btn10.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.library_game_btn10.setIcon(icon15)
        self.library_game_btn10.setIconSize(QSize(115, 115))
        self.library_game_btn8 = QPushButton(self.library_header)
        self.library_game_btn8.setObjectName(u"library_game_btn8")
        self.library_game_btn8.setGeometry(QRect(160, 330, 121, 171))
        self.library_game_btn8.setFont(font6)
        self.library_game_btn8.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.library_game_btn8.setIcon(icon15)
        self.library_game_btn8.setIconSize(QSize(115, 115))
        self.library_game_btn7 = QPushButton(self.library_header)
        self.library_game_btn7.setObjectName(u"library_game_btn7")
        self.library_game_btn7.setGeometry(QRect(10, 330, 121, 171))
        self.library_game_btn7.setFont(font6)
        self.library_game_btn7.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.library_game_btn7.setIcon(icon15)
        self.library_game_btn7.setIconSize(QSize(115, 115))
        self.library_game_btn11 = QPushButton(self.library_header)
        self.library_game_btn11.setObjectName(u"library_game_btn11")
        self.library_game_btn11.setGeometry(QRect(610, 330, 121, 171))
        self.library_game_btn11.setFont(font6)
        self.library_game_btn11.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.library_game_btn11.setIcon(icon15)
        self.library_game_btn11.setIconSize(QSize(115, 115))
        self.library_more_game_btn = QPushButton(self.library_header)
        self.library_more_game_btn.setObjectName(u"library_more_game_btn")
        self.library_more_game_btn.setGeometry(QRect(890, 500, 71, 41))
        self.library_more_game_btn.setFont(font6)
        self.library_more_game_btn.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 255, 255);")
        self.library_more_game_btn.setIcon(icon16)
        self.library_more_game_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_15.addWidget(self.library_header)

        self.mainPages.addWidget(self.libraryPage)
        self.cartsPage = QWidget()
        self.cartsPage.setObjectName(u"cartsPage")
        self.cartsPage.setLayoutDirection(Qt.LeftToRight)
        self.listOrder = QScrollArea(self.cartsPage)
        self.listOrder.setObjectName(u"listOrder")
        self.listOrder.setGeometry(QRect(11, 88, 981, 321))
        self.listOrder.setStyleSheet(u"border: 2px solid rgb(255,255,255);")
        self.listOrder.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.listOrder.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 956, 1000))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 1000))
        self.gameOrderBox_1 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_1.setObjectName(u"gameOrderBox_1")
        self.gameOrderBox_1.setGeometry(QRect(10, 10, 931, 101))
        self.nameGameOrder_1 = QLabel(self.gameOrderBox_1)
        self.nameGameOrder_1.setObjectName(u"nameGameOrder_1")
        self.nameGameOrder_1.setGeometry(QRect(110, 30, 551, 41))
        self.avtGameOrder_1 = QLabel(self.gameOrderBox_1)
        self.avtGameOrder_1.setObjectName(u"avtGameOrder_1")
        self.avtGameOrder_1.setGeometry(QRect(10, 10, 81, 81))
        self.deleteOrder_1 = QPushButton(self.gameOrderBox_1)
        self.deleteOrder_1.setObjectName(u"deleteOrder_1")
        self.deleteOrder_1.setGeometry(QRect(850, 20, 61, 61))
        icon17 = QIcon()
        icon17.addFile(u":/icons/EC8482/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteOrder_1.setIcon(icon17)
        self.deleteOrder_1.setIconSize(QSize(50, 50))
        self.gameOrderBox_2 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_2.setObjectName(u"gameOrderBox_2")
        self.gameOrderBox_2.setGeometry(QRect(10, 120, 931, 101))
        self.nameGameOrder_2 = QLabel(self.gameOrderBox_2)
        self.nameGameOrder_2.setObjectName(u"nameGameOrder_2")
        self.nameGameOrder_2.setGeometry(QRect(110, 30, 551, 41))
        self.avtGameOrder_2 = QLabel(self.gameOrderBox_2)
        self.avtGameOrder_2.setObjectName(u"avtGameOrder_2")
        self.avtGameOrder_2.setGeometry(QRect(10, 10, 81, 81))
        self.deleteOrder_2 = QPushButton(self.gameOrderBox_2)
        self.deleteOrder_2.setObjectName(u"deleteOrder_2")
        self.deleteOrder_2.setGeometry(QRect(850, 20, 61, 61))
        self.deleteOrder_2.setIcon(icon17)
        self.deleteOrder_2.setIconSize(QSize(50, 50))
        self.gameOrderBox_3 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_3.setObjectName(u"gameOrderBox_3")
        self.gameOrderBox_3.setGeometry(QRect(10, 230, 931, 101))
        self.nameGameOrder_3 = QLabel(self.gameOrderBox_3)
        self.nameGameOrder_3.setObjectName(u"nameGameOrder_3")
        self.nameGameOrder_3.setGeometry(QRect(110, 30, 551, 41))
        self.avtGameOrder_3 = QLabel(self.gameOrderBox_3)
        self.avtGameOrder_3.setObjectName(u"avtGameOrder_3")
        self.avtGameOrder_3.setGeometry(QRect(10, 10, 81, 81))
        self.deleteOrder_3 = QPushButton(self.gameOrderBox_3)
        self.deleteOrder_3.setObjectName(u"deleteOrder_3")
        self.deleteOrder_3.setGeometry(QRect(850, 20, 61, 61))
        self.deleteOrder_3.setIcon(icon17)
        self.deleteOrder_3.setIconSize(QSize(50, 50))
        self.gameOrderBox_5 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_5.setObjectName(u"gameOrderBox_5")
        self.gameOrderBox_5.setGeometry(QRect(10, 450, 931, 101))
        self.nameGameOrder_5 = QLabel(self.gameOrderBox_5)
        self.nameGameOrder_5.setObjectName(u"nameGameOrder_5")
        self.nameGameOrder_5.setGeometry(QRect(110, 30, 551, 41))
        self.avtGameOrder_5 = QLabel(self.gameOrderBox_5)
        self.avtGameOrder_5.setObjectName(u"avtGameOrder_5")
        self.avtGameOrder_5.setGeometry(QRect(10, 10, 81, 81))
        self.deleteOrder_5 = QPushButton(self.gameOrderBox_5)
        self.deleteOrder_5.setObjectName(u"deleteOrder_5")
        self.deleteOrder_5.setGeometry(QRect(850, 20, 61, 61))
        self.deleteOrder_5.setIcon(icon17)
        self.deleteOrder_5.setIconSize(QSize(50, 50))
        self.gameOrderBox_4 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_4.setObjectName(u"gameOrderBox_4")
        self.gameOrderBox_4.setGeometry(QRect(10, 340, 931, 101))
        self.nameGameOrder_4 = QLabel(self.gameOrderBox_4)
        self.nameGameOrder_4.setObjectName(u"nameGameOrder_4")
        self.nameGameOrder_4.setGeometry(QRect(110, 30, 551, 41))
        self.avtGameOrder_4 = QLabel(self.gameOrderBox_4)
        self.avtGameOrder_4.setObjectName(u"avtGameOrder_4")
        self.avtGameOrder_4.setGeometry(QRect(10, 10, 81, 81))
        self.deleteOrder_4 = QPushButton(self.gameOrderBox_4)
        self.deleteOrder_4.setObjectName(u"deleteOrder_4")
        self.deleteOrder_4.setGeometry(QRect(850, 20, 61, 61))
        self.deleteOrder_4.setIcon(icon17)
        self.deleteOrder_4.setIconSize(QSize(50, 50))
        self.gameOrderBox_7 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_7.setObjectName(u"gameOrderBox_7")
        self.gameOrderBox_7.setGeometry(QRect(10, 560, 931, 101))
        self.nameGameOrder_7 = QLabel(self.gameOrderBox_7)
        self.nameGameOrder_7.setObjectName(u"nameGameOrder_7")
        self.nameGameOrder_7.setGeometry(QRect(110, 30, 551, 41))
        self.avtGameOrder_7 = QLabel(self.gameOrderBox_7)
        self.avtGameOrder_7.setObjectName(u"avtGameOrder_7")
        self.avtGameOrder_7.setGeometry(QRect(10, 10, 81, 81))
        self.deleteOrder_7 = QPushButton(self.gameOrderBox_7)
        self.deleteOrder_7.setObjectName(u"deleteOrder_7")
        self.deleteOrder_7.setGeometry(QRect(850, 20, 61, 61))
        self.deleteOrder_7.setIcon(icon17)
        self.deleteOrder_7.setIconSize(QSize(50, 50))
        self.gameOrderBox_8 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_8.setObjectName(u"gameOrderBox_8")
        self.gameOrderBox_8.setGeometry(QRect(10, 890, 931, 101))
        self.nameGameOrder_8 = QLabel(self.gameOrderBox_8)
        self.nameGameOrder_8.setObjectName(u"nameGameOrder_8")
        self.nameGameOrder_8.setGeometry(QRect(110, 30, 551, 41))
        self.avtGameOrder_8 = QLabel(self.gameOrderBox_8)
        self.avtGameOrder_8.setObjectName(u"avtGameOrder_8")
        self.avtGameOrder_8.setGeometry(QRect(10, 10, 81, 81))
        self.deleteOrder_8 = QPushButton(self.gameOrderBox_8)
        self.deleteOrder_8.setObjectName(u"deleteOrder_8")
        self.deleteOrder_8.setGeometry(QRect(850, 20, 61, 61))
        self.deleteOrder_8.setIcon(icon17)
        self.deleteOrder_8.setIconSize(QSize(50, 50))
        self.gameOrderBox_9 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_9.setObjectName(u"gameOrderBox_9")
        self.gameOrderBox_9.setGeometry(QRect(10, 670, 931, 101))
        self.nameGameOrder_9 = QLabel(self.gameOrderBox_9)
        self.nameGameOrder_9.setObjectName(u"nameGameOrder_9")
        self.nameGameOrder_9.setGeometry(QRect(110, 30, 551, 41))
        self.avtGameOrder_9 = QLabel(self.gameOrderBox_9)
        self.avtGameOrder_9.setObjectName(u"avtGameOrder_9")
        self.avtGameOrder_9.setGeometry(QRect(10, 10, 81, 81))
        self.deleteOrder_9 = QPushButton(self.gameOrderBox_9)
        self.deleteOrder_9.setObjectName(u"deleteOrder_9")
        self.deleteOrder_9.setGeometry(QRect(850, 20, 61, 61))
        self.deleteOrder_9.setIcon(icon17)
        self.deleteOrder_9.setIconSize(QSize(50, 50))
        self.gameOrderBox_6 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_6.setObjectName(u"gameOrderBox_6")
        self.gameOrderBox_6.setGeometry(QRect(10, 780, 931, 101))
        self.nameGameOrder_6 = QLabel(self.gameOrderBox_6)
        self.nameGameOrder_6.setObjectName(u"nameGameOrder_6")
        self.nameGameOrder_6.setGeometry(QRect(110, 30, 551, 41))
        self.avtGameOrder_6 = QLabel(self.gameOrderBox_6)
        self.avtGameOrder_6.setObjectName(u"avtGameOrder_6")
        self.avtGameOrder_6.setGeometry(QRect(10, 10, 81, 81))
        self.deleteOrder_6 = QPushButton(self.gameOrderBox_6)
        self.deleteOrder_6.setObjectName(u"deleteOrder_6")
        self.deleteOrder_6.setGeometry(QRect(850, 20, 61, 61))
        self.deleteOrder_6.setIcon(icon17)
        self.deleteOrder_6.setIconSize(QSize(50, 50))
        self.listOrder.setWidget(self.scrollAreaWidgetContents)
        self.titleCart = QWidget(self.cartsPage)
        self.titleCart.setObjectName(u"titleCart")
        self.titleCart.setGeometry(QRect(11, 11, 978, 71))
        self.titleCart.setStyleSheet(u"border: 2px solid rgb(255,255,255);")
        self.payMethodBox = QComboBox(self.titleCart)
        self.payMethodBox.addItem("")
        self.payMethodBox.addItem("")
        self.payMethodBox.addItem("")
        self.payMethodBox.addItem("")
        self.payMethodBox.setObjectName(u"payMethodBox")
        self.payMethodBox.setGeometry(QRect(760, 20, 201, 31))
        self.orderBtn = QWidget(self.cartsPage)
        self.orderBtn.setObjectName(u"orderBtn")
        self.orderBtn.setGeometry(QRect(11, 416, 978, 71))
        self.orderBtn.setStyleSheet(u"border: 2px solid rgb(255,255,255);")
        self.payBtn = QPushButton(self.orderBtn)
        self.payBtn.setObjectName(u"payBtn")
        self.payBtn.setGeometry(QRect(850, 20, 111, 41))
        self.payBtn.setFont(font6)
        self.payBtn.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 255, 255);")
        icon18 = QIcon()
        icon18.addFile(u":/icons/EC8482/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.payBtn.setIcon(icon18)
        self.payBtn.setIconSize(QSize(30, 30))
        self.totalCost = QLabel(self.orderBtn)
        self.totalCost.setObjectName(u"totalCost")
        self.totalCost.setEnabled(True)
        self.totalCost.setGeometry(QRect(650, 20, 191, 41))
        font7 = QFont()
        font7.setFamily(u"Arial")
        font7.setPointSize(11)
        self.totalCost.setFont(font7)
        self.mainPages.addWidget(self.cartsPage)
        self.gameInfoPage = QWidget()
        self.gameInfoPage.setObjectName(u"gameInfoPage")
        self.verticalLayout_19 = QVBoxLayout(self.gameInfoPage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gameInfo = QWidget(self.gameInfoPage)
        self.gameInfo.setObjectName(u"gameInfo")
        self.gameInfo.setMinimumSize(QSize(0, 350))
        self.gameInfo.setFont(font5)
        self.gameInfo.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #fff;\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgba(0, 0, 0, 100);\n"
"	padding: 10px;\n"
"	padding-left: 17px;\n"
"	color: #rgb(0,255,255);\n"
"}\n"
"QPushButton\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgba(0, 0, 0, 100);\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 14pt \"Terminal\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(244, 244, 244);\n"
"}")
        self.idLabel_2 = QLabel(self.gameInfo)
        self.idLabel_2.setObjectName(u"idLabel_2")
        self.idLabel_2.setGeometry(QRect(200, 20, 80, 30))
        self.idLabel_2.setFont(font5)
        self.idLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.nameLabel_2 = QLabel(self.gameInfo)
        self.nameLabel_2.setObjectName(u"nameLabel_2")
        self.nameLabel_2.setGeometry(QRect(200, 90, 80, 30))
        self.nameLabel_2.setFont(font5)
        self.nameLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.emailLabel_2 = QLabel(self.gameInfo)
        self.emailLabel_2.setObjectName(u"emailLabel_2")
        self.emailLabel_2.setGeometry(QRect(200, 160, 80, 30))
        self.emailLabel_2.setFont(font5)
        self.emailLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.avtGame = QLabel(self.gameInfo)
        self.avtGame.setObjectName(u"avtGame")
        self.avtGame.setGeometry(QRect(30, 10, 151, 191))
        self.avtGame.setStyleSheet(u"border-radius: 20px;\n"
"border: 2px solid rgba(0,0,0,100)")
        self.avtGame.setLineWidth(0)
        self.avtGame.setTextFormat(Qt.MarkdownText)
        self.avtGame.setPixmap(QPixmap(u":/images/icon-app-user.png"))
        self.avtGame.setScaledContents(True)
        self.avtGame.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.avtGame.setMargin(6)
        self.videoWidget = QWidget(self.gameInfo)
        self.videoWidget.setObjectName(u"videoWidget")
        self.videoWidget.setGeometry(QRect(580, 10, 384, 216))
        self.videoWidget.setStyleSheet(u"border: 2px SOLID rgba(0,0,0,100)")
        self.vidGame = QLabel(self.videoWidget)
        self.vidGame.setObjectName(u"vidGame")
        self.vidGame.setGeometry(QRect(8, 9, 371, 201))
        self.vidGame.setAlignment(Qt.AlignCenter)
        self.PlayBuyBtn = QPushButton(self.gameInfo)
        self.PlayBuyBtn.setObjectName(u"PlayBuyBtn")
        self.PlayBuyBtn.setGeometry(QRect(580, 400, 181, 41))
        self.PlayBuyBtn.setFont(font6)
        self.PlayBuyBtn.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 255, 255);")
        icon19 = QIcon()
        icon19.addFile(u":/icons/EC8482/airplay.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.PlayBuyBtn.setIcon(icon19)
        self.descriptionGame = QLabel(self.gameInfo)
        self.descriptionGame.setObjectName(u"descriptionGame")
        self.descriptionGame.setGeometry(QRect(44, 225, 491, 221))
        font8 = QFont()
        font8.setPointSize(11)
        self.descriptionGame.setFont(font8)
        self.descriptionGame.setStyleSheet(u"border-radius: 20px;\n"
"border: 2px solid rgba(0,0,0,100);\n"
"background-color: rgba(255,255,255,255);\n"
"color: rgb(0,0,0);\n"
"padding-top: 7px;\n"
"padding-left: 7px;")
        self.descriptionGame.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.descriptionGame.setWordWrap(True)
        self.descriptionGame.setMargin(0)
        self.idGame = QLabel(self.gameInfo)
        self.idGame.setObjectName(u"idGame")
        self.idGame.setGeometry(QRect(290, 10, 261, 51))
        font9 = QFont()
        font9.setPointSize(13)
        self.idGame.setFont(font9)
        self.idGame.setStyleSheet(u"border-radius: 20px;\n"
"border: 2px solid rgba(0,0,0,100);\n"
"background-color: rgba(255,255,255,255);\n"
"color: rgb(0,0,0);\n"
"padding-left: 7px;")
        self.idGame.setWordWrap(True)
        self.idGame.setMargin(0)
        self.nameGame = QLabel(self.gameInfo)
        self.nameGame.setObjectName(u"nameGame")
        self.nameGame.setGeometry(QRect(290, 80, 261, 51))
        self.nameGame.setFont(font9)
        self.nameGame.setStyleSheet(u"border-radius: 20px;\n"
"border: 2px solid rgba(0,0,0,100);\n"
"background-color: rgba(255,255,255,255);\n"
"color: rgb(0,0,0);\n"
"padding-left: 7px;")
        self.nameGame.setWordWrap(True)
        self.nameGame.setMargin(0)
        self.priceGame = QLabel(self.gameInfo)
        self.priceGame.setObjectName(u"priceGame")
        self.priceGame.setGeometry(QRect(290, 150, 261, 51))
        self.priceGame.setFont(font9)
        self.priceGame.setStyleSheet(u"border-radius: 20px;\n"
"border: 2px solid rgba(0,0,0,100);\n"
"background-color: rgba(255,255,255,255);\n"
"color: rgb(0,0,0);\n"
"padding-left: 7px;")
        self.priceGame.setWordWrap(True)
        self.priceGame.setMargin(0)

        self.verticalLayout_19.addWidget(self.gameInfo)

        self.mainPages.addWidget(self.gameInfoPage)

        self.verticalLayout_13.addWidget(self.mainPages)


        self.horizontalLayout_10.addWidget(self.mainContentsContainer)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(0, 0))
        self.rightMenuContainer.setMaximumSize(QSize(0, 496))
        self.rightMenuContainer.setStyleSheet(u"border-radius: 10px")
        self.verticalLayout_9 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(1000, 0))
        self.rightMenuSubContainer.setMaximumSize(QSize(16777215, 500))
        self.verticalLayout_10 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.rightMenuBar = QFrame(self.rightMenuSubContainer)
        self.rightMenuBar.setObjectName(u"rightMenuBar")
        self.rightMenuBar.setMinimumSize(QSize(0, 0))
        self.rightMenuBar.setFrameShape(QFrame.StyledPanel)
        self.rightMenuBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.rightMenuBar)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.rightMenuTile = QLabel(self.rightMenuBar)
        self.rightMenuTile.setObjectName(u"rightMenuTile")
        self.rightMenuTile.setFont(font2)
        self.rightMenuTile.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.rightMenuTile)

        self.closeRightMenuBtn = QPushButton(self.rightMenuBar)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon7)
        self.closeRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.rightMenuBar)

        self.rightMenuPages = QCustomQStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.rightMenuPages.setMinimumSize(QSize(0, 0))
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.verticalLayout_11 = QVBoxLayout(self.profilePage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.userInfor = QWidget(self.profilePage)
        self.userInfor.setObjectName(u"userInfor")
        self.userInfor.setMinimumSize(QSize(0, 350))
        self.userInfor.setFont(font5)
        self.userInfor.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #fff;\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgba(0, 0, 0, 100);\n"
"	padding: 10px;\n"
"	padding-left: 17px;\n"
"	color: #rgb(0,255,255);\n"
"}\n"
"QPushButton\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgba(0, 0, 0, 100);\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 14pt \"Terminal\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(244, 244, 244);\n"
"}")
        self.idLabel = QLabel(self.userInfor)
        self.idLabel.setObjectName(u"idLabel")
        self.idLabel.setGeometry(QRect(20, 30, 150, 30))
        self.idLabel.setFont(font5)
        self.idLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.nameLabel = QLabel(self.userInfor)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(20, 100, 150, 30))
        self.nameLabel.setFont(font5)
        self.nameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.emailLabel = QLabel(self.userInfor)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setGeometry(QRect(20, 170, 150, 30))
        self.emailLabel.setFont(font5)
        self.emailLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.passwordLabel = QLabel(self.userInfor)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(20, 240, 150, 30))
        self.passwordLabel.setFont(font5)
        self.passwordLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.idLine = QLineEdit(self.userInfor)
        self.idLine.setObjectName(u"idLine")
        self.idLine.setEnabled(True)
        self.idLine.setGeometry(QRect(200, 30, 381, 41))
        font10 = QFont()
        font10.setFamily(u"Arial")
        font10.setPointSize(11)
        font10.setBold(False)
        font10.setItalic(False)
        font10.setWeight(50)
        self.idLine.setFont(font10)
        self.idLine.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding: 0px 0px 0px 15px;")
        self.nameLine = QLineEdit(self.userInfor)
        self.nameLine.setObjectName(u"nameLine")
        self.nameLine.setEnabled(True)
        self.nameLine.setGeometry(QRect(200, 100, 381, 41))
        self.nameLine.setFont(font10)
        self.nameLine.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding: 0px 0px 0px 15px;")
        self.emailLine = QLineEdit(self.userInfor)
        self.emailLine.setObjectName(u"emailLine")
        self.emailLine.setGeometry(QRect(200, 170, 381, 41))
        self.emailLine.setFont(font10)
        self.emailLine.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding: 0px 0px 0px 15px;")
        self.passLine = QLineEdit(self.userInfor)
        self.passLine.setObjectName(u"passLine")
        self.passLine.setGeometry(QRect(200, 240, 381, 41))
        self.passLine.setFont(font10)
        self.passLine.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding: 0px 0px 0px 15px;")
        self.AvatarLabel = QLabel(self.userInfor)
        self.AvatarLabel.setObjectName(u"AvatarLabel")
        self.AvatarLabel.setGeometry(QRect(730, 10, 200, 200))
        self.AvatarLabel.setStyleSheet(u"border-radius: 20px;\n"
"border: 2px solid rgba(0,0,0,100)")
        self.AvatarLabel.setLineWidth(0)
        self.AvatarLabel.setTextFormat(Qt.MarkdownText)
        self.AvatarLabel.setPixmap(QPixmap(u":/images/z4721841278414_41db3f1c2d44195237d25ddf1ebfad34.jpg"))
        self.AvatarLabel.setScaledContents(True)
        self.AvatarLabel.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.AvatarLabel.setMargin(0)
        self.pushButton = QPushButton(self.userInfor)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(730, 280, 181, 41))
        self.pushButton.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_11.addWidget(self.userInfor)

        self.userBtn = QWidget(self.profilePage)
        self.userBtn.setObjectName(u"userBtn")
        self.userBtn.setMinimumSize(QSize(0, 100))
        self.userBtn.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgba(0, 0, 0, 100);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(244, 244, 244);\n"
"}")
        self.doneBtn = QPushButton(self.userBtn)
        self.doneBtn.setObjectName(u"doneBtn")
        self.doneBtn.setGeometry(QRect(730, 40, 181, 41))
        font11 = QFont()
        font11.setPointSize(12)
        self.doneBtn.setFont(font11)
        self.doneBtn.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 255, 255);")
        icon20 = QIcon()
        icon20.addFile(u":/icons/EC8482/check-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.doneBtn.setIcon(icon20)
        self.cancelBtn = QPushButton(self.userBtn)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setGeometry(QRect(530, 40, 181, 41))
        self.cancelBtn.setFont(font11)
        self.cancelBtn.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(206, 103, 114);")
        self.cancelBtn.setIcon(icon17)

        self.verticalLayout_11.addWidget(self.userBtn)

        self.rightMenuPages.addWidget(self.profilePage)
        self.morePage = QWidget()
        self.morePage.setObjectName(u"morePage")
        self.verticalLayout_12 = QVBoxLayout(self.morePage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.moreLabel = QLabel(self.morePage)
        self.moreLabel.setObjectName(u"moreLabel")
        self.moreLabel.setFont(font3)
        self.moreLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.moreLabel)

        self.rightMenuPages.addWidget(self.morePage)

        self.verticalLayout_10.addWidget(self.rightMenuPages)


        self.verticalLayout_9.addWidget(self.rightMenuSubContainer, 0, Qt.AlignRight)


        self.horizontalLayout_10.addWidget(self.rightMenuContainer)


        self.verticalLayout_8.addWidget(self.mainBodyContent)

        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.verticalLayout_17 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.verticalLayout_18 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.notificationTitle = QLabel(self.popupNotificationSubContainer)
        self.notificationTitle.setObjectName(u"notificationTitle")
        font12 = QFont()
        font12.setPointSize(10)
        font12.setBold(True)
        font12.setWeight(75)
        self.notificationTitle.setFont(font12)

        self.verticalLayout_18.addWidget(self.notificationTitle)

        self.notificationsFrame = QFrame(self.popupNotificationSubContainer)
        self.notificationsFrame.setObjectName(u"notificationsFrame")
        self.notificationsFrame.setFrameShape(QFrame.StyledPanel)
        self.notificationsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.notificationsFrame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.messageLabel = QLabel(self.notificationsFrame)
        self.messageLabel.setObjectName(u"messageLabel")
        sizePolicy.setHeightForWidth(self.messageLabel.sizePolicy().hasHeightForWidth())
        self.messageLabel.setSizePolicy(sizePolicy)
        self.messageLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.messageLabel)

        self.closeNotificationBtn = QPushButton(self.notificationsFrame)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        icon21 = QIcon()
        icon21.addFile(u":/icons/EC8482/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon21)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_12.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight)


        self.verticalLayout_18.addWidget(self.notificationsFrame)


        self.verticalLayout_17.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_8.addWidget(self.popupNotificationContainer)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_13 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.copyRight = QFrame(self.footerContainer)
        self.copyRight.setObjectName(u"copyRight")
        self.copyRight.setFrameShape(QFrame.StyledPanel)
        self.copyRight.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.copyRight)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.copyRightTitle = QLabel(self.copyRight)
        self.copyRightTitle.setObjectName(u"copyRightTitle")

        self.horizontalLayout_14.addWidget(self.copyRightTitle)


        self.horizontalLayout_13.addWidget(self.copyRight)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(10, 10))
        self.sizeGrip.setMaximumSize(QSize(30, 30))
        self.sizeGrip.setStyleSheet(u"")
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.sizeGrip)


        self.verticalLayout_8.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        self.mainLogin = QWidget(self.centralwidget)
        self.mainLogin.setObjectName(u"mainLogin")
        self.mainLogin.setGeometry(QRect(11, 60, 1243, 681))
        self.mainLogin.setStyleSheet(u"background-color: rgb(255, 152, 152);")
        self.LoginButton = QPushButton(self.mainLogin)
        self.LoginButton.setObjectName(u"LoginButton")
        self.LoginButton.setGeometry(QRect(200, 180, 241, 41))
        self.LoginButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.LoginButton.setStyleSheet(u"QPushButton#LoginButton\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgba(0, 0, 0, 100);\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 14pt \"Terminal\";\n"
"	color: rgba(0,0,0)\n"
"}\n"
"QPushButton#LoginButton:hover\n"
"{\n"
"	background-color: rgb(244, 244, 244);\n"
"}")
        self.UsernameLabel = QLabel(self.mainLogin)
        self.UsernameLabel.setObjectName(u"UsernameLabel")
        self.UsernameLabel.setGeometry(QRect(40, 36, 91, 41))
        self.UsernameLabel.setStyleSheet(u"font: 14pt \"Terminal\";")
        self.UsernameLabel.setWordWrap(True)
        self.PasswordLabel = QLabel(self.mainLogin)
        self.PasswordLabel.setObjectName(u"PasswordLabel")
        self.PasswordLabel.setGeometry(QRect(40, 106, 91, 41))
        self.PasswordLabel.setStyleSheet(u"font: 14pt \"Terminal\";")
        self.PasswordLabel.setWordWrap(True)
        self.RegisterButton = QPushButton(self.mainLogin)
        self.RegisterButton.setObjectName(u"RegisterButton")
        self.RegisterButton.setGeometry(QRect(40, 180, 141, 41))
        self.RegisterButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.RegisterButton.setStyleSheet(u"QPushButton#RegisterButton\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgba(0, 0, 0, 100);\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 14pt \"Terminal\";\n"
"	color: rgba(0,0,0)\n"
"}\n"
"QPushButton#RegisterButton:hover\n"
"{\n"
"	background-color: rgb(244, 244, 244);\n"
"}")
        self.PasswordInput = QLineEdit(self.mainLogin)
        self.PasswordInput.setObjectName(u"PasswordInput")
        self.PasswordInput.setGeometry(QRect(160, 105, 281, 42))
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
        self.UsernameInput = QLineEdit(self.mainLogin)
        self.UsernameInput.setObjectName(u"UsernameInput")
        self.UsernameInput.setGeometry(QRect(160, 36, 281, 41))
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
        self.headerLogin = QWidget(self.centralwidget)
        self.headerLogin.setObjectName(u"headerLogin")
        self.headerLogin.setGeometry(QRect(11, 11, 1101, 47))
        self.headerLogin.setStyleSheet(u"background-color: rgb(255, 152, 152);")
        self.headerLoginLabel = QLabel(self.headerLogin)
        self.headerLoginLabel.setObjectName(u"headerLoginLabel")
        self.headerLoginLabel.setGeometry(QRect(44, 15, 121, 21))
        font13 = QFont()
        font13.setFamily(u"Arial")
        font13.setPointSize(11)
        font13.setBold(True)
        font13.setWeight(75)
        self.headerLoginLabel.setFont(font13)
        self.hidExpand = QWidget(self.centralwidget)
        self.hidExpand.setObjectName(u"hidExpand")
        self.hidExpand.setGeometry(QRect(1168, 11, 41, 47))
        self.hidExpand.setStyleSheet(u"background-color: rgba(0,0,0, 50);")
        UserWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserWindow)

        self.centerMenuPages.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(2)
        self.rightMenuPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(UserWindow)
    # setupUi

    def retranslateUi(self, UserWindow):
        UserWindow.setWindowTitle(QCoreApplication.translate("UserWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText(QCoreApplication.translate("UserWindow", u"  Main Menu", None))
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("UserWindow", u"  Home", None))
#if QT_CONFIG(tooltip)
        self.libraryBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Data Analysis", None))
#endif // QT_CONFIG(tooltip)
        self.libraryBtn.setText(QCoreApplication.translate("UserWindow", u"  Library", None))
#if QT_CONFIG(tooltip)
        self.cartsBtn.setToolTip(QCoreApplication.translate("UserWindow", u"View Reports", None))
#endif // QT_CONFIG(tooltip)
        self.cartsBtn.setText(QCoreApplication.translate("UserWindow", u"  Carts", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Go to Setting", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("UserWindow", u"  Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Information for App", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("UserWindow", u"  Information", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Any Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("UserWindow", u"  Help", None))
        self.titleCenterMenu.setText(QCoreApplication.translate("UserWindow", u"   Details", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.settingsLabel.setText(QCoreApplication.translate("UserWindow", u"Settings", None))
        self.helpLabel.setText(QCoreApplication.translate("UserWindow", u"Help", None))
        self.infoLabel.setText(QCoreApplication.translate("UserWindow", u"Information", None))
        self.appIcon.setText("")
        self.appTitle.setText(QCoreApplication.translate("UserWindow", u"HomeMader-User", None))
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.moreMenuBtn.setToolTip(QCoreApplication.translate("UserWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.moreMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileMenuBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.home_search_line.setText("")
        self.home_search_label.setText(QCoreApplication.translate("UserWindow", u"T\u00ecm ki\u1ebfm:", None))
        self.home_search_btn.setText(QCoreApplication.translate("UserWindow", u" Search", None))
        self.home_game_btn1.setText("")
        self.home_game_btn2.setText("")
        self.home_game_btn3.setText("")
        self.home_game_btn6.setText("")
        self.home_game_btn5.setText("")
        self.home_game_btn4.setText("")
        self.home_game_btn12.setText("")
        self.home_game_btn9.setText("")
        self.home_game_btn10.setText("")
        self.home_game_btn8.setText("")
        self.home_game_btn7.setText("")
        self.home_game_btn11.setText("")
        self.home_more_game_btn.setText("")
        self.library_search_line.setText("")
        self.library_search_label.setText(QCoreApplication.translate("UserWindow", u"T\u00ecm ki\u1ebfm:", None))
        self.library_search_btn.setText(QCoreApplication.translate("UserWindow", u" Search", None))
        self.library_game_btn1.setText("")
        self.library_game_btn2.setText("")
        self.library_game_btn3.setText("")
        self.library_game_btn6.setText("")
        self.library_game_btn5.setText("")
        self.library_game_btn4.setText("")
        self.library_game_btn12.setText("")
        self.library_game_btn9.setText("")
        self.library_game_btn10.setText("")
        self.library_game_btn8.setText("")
        self.library_game_btn7.setText("")
        self.library_game_btn11.setText("")
        self.library_more_game_btn.setText("")
        self.nameGameOrder_1.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.avtGameOrder_1.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.deleteOrder_1.setText("")
        self.nameGameOrder_2.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.avtGameOrder_2.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.deleteOrder_2.setText("")
        self.nameGameOrder_3.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.avtGameOrder_3.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.deleteOrder_3.setText("")
        self.nameGameOrder_5.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.avtGameOrder_5.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.deleteOrder_5.setText("")
        self.nameGameOrder_4.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.avtGameOrder_4.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.deleteOrder_4.setText("")
        self.nameGameOrder_7.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.avtGameOrder_7.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.deleteOrder_7.setText("")
        self.nameGameOrder_8.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.avtGameOrder_8.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.deleteOrder_8.setText("")
        self.nameGameOrder_9.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.avtGameOrder_9.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.deleteOrder_9.setText("")
        self.nameGameOrder_6.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.avtGameOrder_6.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.deleteOrder_6.setText("")
        self.payMethodBox.setItemText(0, QCoreApplication.translate("UserWindow", u"Cash", None))
        self.payMethodBox.setItemText(1, QCoreApplication.translate("UserWindow", u"Credit card", None))
        self.payMethodBox.setItemText(2, QCoreApplication.translate("UserWindow", u"Visa", None))
        self.payMethodBox.setItemText(3, QCoreApplication.translate("UserWindow", u"Paypal", None))

        self.payBtn.setText("")
        self.totalCost.setText(QCoreApplication.translate("UserWindow", u"0", None))
        self.idLabel_2.setText(QCoreApplication.translate("UserWindow", u"ID:", None))
        self.nameLabel_2.setText(QCoreApplication.translate("UserWindow", u"Name:", None))
        self.emailLabel_2.setText(QCoreApplication.translate("UserWindow", u"Price:", None))
        self.avtGame.setText("")
        self.vidGame.setText("")
        self.PlayBuyBtn.setText(QCoreApplication.translate("UserWindow", u" Play", None))
        self.descriptionGame.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.idGame.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.nameGame.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.priceGame.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.rightMenuTile.setText(QCoreApplication.translate("UserWindow", u"   Menu", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.idLabel.setText(QCoreApplication.translate("UserWindow", u"ID:", None))
        self.nameLabel.setText(QCoreApplication.translate("UserWindow", u"Name:", None))
        self.emailLabel.setText(QCoreApplication.translate("UserWindow", u"Email:", None))
        self.passwordLabel.setText(QCoreApplication.translate("UserWindow", u"Password:", None))
        self.idLine.setInputMask("")
        self.idLine.setText(QCoreApplication.translate("UserWindow", u"2055010153", None))
        self.nameLine.setText(QCoreApplication.translate("UserWindow", u"Nguy\u1ec5n Th\u00e0nh D\u01b0\u01a1ng", None))
        self.AvatarLabel.setText("")
        self.pushButton.setText(QCoreApplication.translate("UserWindow", u"Change Image", None))
        self.doneBtn.setText(QCoreApplication.translate("UserWindow", u" Done", None))
        self.cancelBtn.setText(QCoreApplication.translate("UserWindow", u" Cancel", None))
        self.moreLabel.setText(QCoreApplication.translate("UserWindow", u"More...", None))
        self.notificationTitle.setText(QCoreApplication.translate("UserWindow", u"Notification", None))
        self.messageLabel.setText(QCoreApplication.translate("UserWindow", u"Notification Message", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Close Notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
        self.copyRightTitle.setText(QCoreApplication.translate("UserWindow", u"Copyright By DuongKLinh", None))
        self.LoginButton.setText(QCoreApplication.translate("UserWindow", u"Login", None))
        self.UsernameLabel.setText(QCoreApplication.translate("UserWindow", u"Username:", None))
        self.PasswordLabel.setText(QCoreApplication.translate("UserWindow", u"Password:", None))
        self.RegisterButton.setText(QCoreApplication.translate("UserWindow", u"Register", None))
        self.PasswordInput.setText("")
        self.headerLoginLabel.setText(QCoreApplication.translate("UserWindow", u"Log In", None))
    # retranslateUi


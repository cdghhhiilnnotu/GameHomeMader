# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserFormjlYScg.ui'
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

import Ui.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1391, 726)
        MainWindow.setStyleSheet(u"* {\n"
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
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

        self.gamesBtn = QPushButton(self.navBar)
        self.gamesBtn.setObjectName(u"gamesBtn")
        self.gamesBtn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/EC8482/github.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.gamesBtn.setIcon(icon2)
        self.gamesBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.gamesBtn)

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

        self.centerMenuContainer = QWidget(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(0, 0))
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

        self.mainBodyContainer = QWidget(self.centralwidget)
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
        self.headerHome = QWidget(self.homePage)
        self.headerHome.setObjectName(u"headerHome")
        self.headerHome.setStyleSheet(u"QLineEdit\n"
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
        self.searchLine = QLineEdit(self.headerHome)
        self.searchLine.setObjectName(u"searchLine")
        self.searchLine.setEnabled(True)
        self.searchLine.setGeometry(QRect(440, 10, 351, 42))
        font4 = QFont()
        font4.setFamily(u"Terminal")
        font4.setPointSize(15)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.searchLine.setFont(font4)
        self.searchLine.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.searchLabel = QLabel(self.headerHome)
        self.searchLabel.setObjectName(u"searchLabel")
        self.searchLabel.setGeometry(QRect(320, 20, 111, 30))
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(False)
        font5.setWeight(50)
        self.searchLabel.setFont(font5)
        self.searchLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.searchBtn = QPushButton(self.headerHome)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setGeometry(QRect(800, 10, 161, 41))
        font6 = QFont()
        font6.setFamily(u"Terminal")
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.searchBtn.setFont(font6)
        self.searchBtn.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        icon14 = QIcon()
        icon14.addFile(u":/icons/EC8482/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchBtn.setIcon(icon14)
        self.game1 = QPushButton(self.headerHome)
        self.game1.setObjectName(u"game1")
        self.game1.setGeometry(QRect(10, 70, 121, 171))
        self.game1.setFont(font6)
        self.game1.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        icon15 = QIcon()
        icon15.addFile(u"../../../../../../../DLcghhhiinnotu/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.game1.setIcon(icon15)
        self.game1.setIconSize(QSize(115, 115))
        self.game1.setAutoRepeat(False)
        self.game2 = QPushButton(self.headerHome)
        self.game2.setObjectName(u"game2")
        self.game2.setGeometry(QRect(160, 70, 121, 171))
        self.game2.setFont(font6)
        self.game2.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.game2.setIcon(icon15)
        self.game2.setIconSize(QSize(115, 115))
        self.game3 = QPushButton(self.headerHome)
        self.game3.setObjectName(u"game3")
        self.game3.setGeometry(QRect(310, 70, 121, 171))
        self.game3.setFont(font6)
        self.game3.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.game3.setIcon(icon15)
        self.game3.setIconSize(QSize(115, 115))
        self.game6 = QPushButton(self.headerHome)
        self.game6.setObjectName(u"game6")
        self.game6.setGeometry(QRect(760, 70, 121, 171))
        self.game6.setFont(font6)
        self.game6.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.game6.setIcon(icon15)
        self.game6.setIconSize(QSize(115, 115))
        self.game5 = QPushButton(self.headerHome)
        self.game5.setObjectName(u"game5")
        self.game5.setGeometry(QRect(610, 70, 121, 171))
        self.game5.setFont(font6)
        self.game5.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.game5.setIcon(icon15)
        self.game5.setIconSize(QSize(115, 115))
        self.game4 = QPushButton(self.headerHome)
        self.game4.setObjectName(u"game4")
        self.game4.setGeometry(QRect(460, 70, 121, 171))
        self.game4.setFont(font6)
        self.game4.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.game4.setIcon(icon15)
        self.game4.setIconSize(QSize(115, 115))
        self.game12 = QPushButton(self.headerHome)
        self.game12.setObjectName(u"game12")
        self.game12.setGeometry(QRect(760, 330, 121, 171))
        self.game12.setFont(font6)
        self.game12.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.game12.setIcon(icon15)
        self.game12.setIconSize(QSize(115, 115))
        self.game9 = QPushButton(self.headerHome)
        self.game9.setObjectName(u"game9")
        self.game9.setGeometry(QRect(310, 330, 121, 171))
        self.game9.setFont(font6)
        self.game9.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.game9.setIcon(icon15)
        self.game9.setIconSize(QSize(115, 115))
        self.game10 = QPushButton(self.headerHome)
        self.game10.setObjectName(u"game10")
        self.game10.setGeometry(QRect(460, 330, 121, 171))
        self.game10.setFont(font6)
        self.game10.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.game10.setIcon(icon15)
        self.game10.setIconSize(QSize(115, 115))
        self.game8 = QPushButton(self.headerHome)
        self.game8.setObjectName(u"game8")
        self.game8.setGeometry(QRect(160, 330, 121, 171))
        self.game8.setFont(font6)
        self.game8.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.game8.setIcon(icon15)
        self.game8.setIconSize(QSize(115, 115))
        self.game7 = QPushButton(self.headerHome)
        self.game7.setObjectName(u"game7")
        self.game7.setGeometry(QRect(10, 330, 121, 171))
        self.game7.setFont(font6)
        self.game7.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.game7.setIcon(icon15)
        self.game7.setIconSize(QSize(115, 115))
        self.game11 = QPushButton(self.headerHome)
        self.game11.setObjectName(u"game11")
        self.game11.setGeometry(QRect(610, 330, 121, 171))
        self.game11.setFont(font6)
        self.game11.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.game11.setIcon(icon15)
        self.game11.setIconSize(QSize(115, 115))
        self.moreGameBtn = QPushButton(self.headerHome)
        self.moreGameBtn.setObjectName(u"moreGameBtn")
        self.moreGameBtn.setGeometry(QRect(890, 500, 71, 41))
        self.moreGameBtn.setFont(font6)
        self.moreGameBtn.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 255, 255);")
        icon16 = QIcon()
        icon16.addFile(u":/icons/EC8482/chevrons-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreGameBtn.setIcon(icon16)
        self.moreGameBtn.setIconSize(QSize(30, 30))

        self.verticalLayout_14.addWidget(self.headerHome)

        self.mainPages.addWidget(self.homePage)
        self.gamesPage = QWidget()
        self.gamesPage.setObjectName(u"gamesPage")
        self.verticalLayout_15 = QVBoxLayout(self.gamesPage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.gamesLabel = QLabel(self.gamesPage)
        self.gamesLabel.setObjectName(u"gamesLabel")
        self.gamesLabel.setFont(font3)
        self.gamesLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.gamesLabel)

        self.mainPages.addWidget(self.gamesPage)
        self.cartsPage = QWidget()
        self.cartsPage.setObjectName(u"cartsPage")
        self.verticalLayout_16 = QVBoxLayout(self.cartsPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.cartLabel = QLabel(self.cartsPage)
        self.cartLabel.setObjectName(u"cartLabel")
        self.cartLabel.setFont(font3)
        self.cartLabel.setStyleSheet(u"")
        self.cartLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.cartLabel)

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
        self.idGameLine = QLineEdit(self.gameInfo)
        self.idGameLine.setObjectName(u"idGameLine")
        self.idGameLine.setEnabled(False)
        self.idGameLine.setGeometry(QRect(290, 20, 250, 41))
        self.idGameLine.setFont(font4)
        self.idGameLine.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.nameGameLine = QLineEdit(self.gameInfo)
        self.nameGameLine.setObjectName(u"nameGameLine")
        self.nameGameLine.setEnabled(False)
        self.nameGameLine.setGeometry(QRect(290, 90, 250, 41))
        self.nameGameLine.setFont(font4)
        self.nameGameLine.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.priceGameLine = QLineEdit(self.gameInfo)
        self.priceGameLine.setObjectName(u"priceGameLine")
        self.priceGameLine.setEnabled(False)
        self.priceGameLine.setGeometry(QRect(290, 160, 250, 41))
        self.priceGameLine.setFont(font4)
        self.priceGameLine.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.descriptionGameLine = QLineEdit(self.gameInfo)
        self.descriptionGameLine.setObjectName(u"descriptionGameLine")
        self.descriptionGameLine.setEnabled(False)
        self.descriptionGameLine.setGeometry(QRect(20, 230, 531, 211))
        self.descriptionGameLine.setFont(font4)
        self.descriptionGameLine.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.AvatarLabel_2 = QLabel(self.gameInfo)
        self.AvatarLabel_2.setObjectName(u"AvatarLabel_2")
        self.AvatarLabel_2.setGeometry(QRect(30, 10, 151, 191))
        self.AvatarLabel_2.setStyleSheet(u"border-radius: 20px;\n"
"border: 2px solid rgba(0,0,0,100)")
        self.AvatarLabel_2.setLineWidth(0)
        self.AvatarLabel_2.setTextFormat(Qt.MarkdownText)
        self.AvatarLabel_2.setPixmap(QPixmap(u":/images/icon-app-user.png"))
        self.AvatarLabel_2.setScaledContents(True)
        self.AvatarLabel_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.AvatarLabel_2.setMargin(6)
        self.videoWidget = QWidget(self.gameInfo)
        self.videoWidget.setObjectName(u"videoWidget")
        self.videoWidget.setGeometry(QRect(580, 10, 384, 216))
        self.videoWidget.setStyleSheet(u"border: 2px SOLID rgba(0,0,0,100)")
        self.videoLabel = QLabel(self.videoWidget)
        self.videoLabel.setObjectName(u"videoLabel")
        self.videoLabel.setGeometry(QRect(8, 9, 371, 201))
        self.videoLabel.setAlignment(Qt.AlignCenter)
        self.doneBtn_2 = QPushButton(self.gameInfo)
        self.doneBtn_2.setObjectName(u"doneBtn_2")
        self.doneBtn_2.setGeometry(QRect(580, 400, 181, 41))
        self.doneBtn_2.setFont(font6)
        self.doneBtn_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 255, 255);")
        icon17 = QIcon()
        icon17.addFile(u":/icons/EC8482/airplay.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.doneBtn_2.setIcon(icon17)

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
        self.idLine.setFont(font4)
        self.idLine.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.nameLine = QLineEdit(self.userInfor)
        self.nameLine.setObjectName(u"nameLine")
        self.nameLine.setEnabled(True)
        self.nameLine.setGeometry(QRect(200, 100, 381, 41))
        self.nameLine.setFont(font4)
        self.nameLine.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.emailLine = QLineEdit(self.userInfor)
        self.emailLine.setObjectName(u"emailLine")
        self.emailLine.setGeometry(QRect(200, 170, 381, 41))
        self.emailLine.setFont(font4)
        self.emailLine.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.passLine = QLineEdit(self.userInfor)
        self.passLine.setObjectName(u"passLine")
        self.passLine.setGeometry(QRect(200, 240, 381, 41))
        self.passLine.setFont(font4)
        self.passLine.setStyleSheet(u"color: rgb(0, 0, 0);")
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
        font7 = QFont()
        font7.setPointSize(12)
        self.doneBtn.setFont(font7)
        self.doneBtn.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 255, 255);")
        icon18 = QIcon()
        icon18.addFile(u":/icons/EC8482/check-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.doneBtn.setIcon(icon18)
        self.cancelBtn = QPushButton(self.userBtn)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setGeometry(QRect(530, 40, 181, 41))
        self.cancelBtn.setFont(font7)
        self.cancelBtn.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(206, 103, 114);")
        icon19 = QIcon()
        icon19.addFile(u":/icons/EC8482/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelBtn.setIcon(icon19)

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
        font8 = QFont()
        font8.setPointSize(10)
        font8.setBold(True)
        font8.setWeight(75)
        self.notificationTitle.setFont(font8)

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
        icon20 = QIcon()
        icon20.addFile(u":/icons/EC8482/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon20)
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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(2)
        self.mainPages.setCurrentIndex(3)
        self.rightMenuPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText(QCoreApplication.translate("MainWindow", u"  Main Menu", None))
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"  Home", None))
#if QT_CONFIG(tooltip)
        self.gamesBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
#endif // QT_CONFIG(tooltip)
        self.gamesBtn.setText(QCoreApplication.translate("MainWindow", u"  Library", None))
#if QT_CONFIG(tooltip)
        self.cartsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Reports", None))
#endif // QT_CONFIG(tooltip)
        self.cartsBtn.setText(QCoreApplication.translate("MainWindow", u"  Carts", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to Setting", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"  Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information for App", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"  Information", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Any Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"  Help", None))
        self.titleCenterMenu.setText(QCoreApplication.translate("MainWindow", u"   Details", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.settingsLabel.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.helpLabel.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.infoLabel.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.appIcon.setText("")
        self.appTitle.setText(QCoreApplication.translate("MainWindow", u"HomeMader-User", None))
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.moreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.moreMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.searchLine.setText("")
        self.searchLabel.setText(QCoreApplication.translate("MainWindow", u"T\u00ecm ki\u1ebfm:", None))
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u" Search", None))
        self.game1.setText("")
        self.game2.setText("")
        self.game3.setText("")
        self.game6.setText("")
        self.game5.setText("")
        self.game4.setText("")
        self.game12.setText("")
        self.game9.setText("")
        self.game10.setText("")
        self.game8.setText("")
        self.game7.setText("")
        self.game11.setText("")
        self.moreGameBtn.setText("")
        self.gamesLabel.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.cartLabel.setText(QCoreApplication.translate("MainWindow", u"Carts", None))
        self.idLabel_2.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.nameLabel_2.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.emailLabel_2.setText(QCoreApplication.translate("MainWindow", u"Price:", None))
        self.idGameLine.setInputMask("")
        self.idGameLine.setText(QCoreApplication.translate("MainWindow", u"2055010153", None))
        self.nameGameLine.setText("")
        self.AvatarLabel_2.setText("")
        self.videoLabel.setText("")
        self.doneBtn_2.setText(QCoreApplication.translate("MainWindow", u" Play", None))
        self.rightMenuTile.setText(QCoreApplication.translate("MainWindow", u"   Menu", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.idLabel.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.idLine.setInputMask("")
        self.idLine.setText(QCoreApplication.translate("MainWindow", u"2055010153", None))
        self.nameLine.setText("")
        self.AvatarLabel.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Change Image", None))
        self.doneBtn.setText(QCoreApplication.translate("MainWindow", u" Done", None))
        self.cancelBtn.setText(QCoreApplication.translate("MainWindow", u" Cancel", None))
        self.moreLabel.setText(QCoreApplication.translate("MainWindow", u"More...", None))
        self.notificationTitle.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.messageLabel.setText(QCoreApplication.translate("MainWindow", u"Notification Message", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
        self.copyRightTitle.setText(QCoreApplication.translate("MainWindow", u"Copyright By DuongKLinh", None))
    # retranslateUi


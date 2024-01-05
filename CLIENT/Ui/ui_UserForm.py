# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserFormVztYRe.ui'
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
        UserWindow.resize(1262, 751)
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
        self.homeBtn.setStyleSheet(u"")
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
        self.centerMenuContainer.setMaximumSize(QSize(5000, 16777215))
        self.centerMenuContainer.setStyleSheet(u"border-radius: 10px;")
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QCustomSlideMenu(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(0, 0))
        self.centerMenuSubContainer.setMaximumSize(QSize(0, 16777215))
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
        self.Setting = QWidget(self.settingsPage)
        self.Setting.setObjectName(u"Setting")
        self.logOutBtn = QPushButton(self.Setting)
        self.logOutBtn.setObjectName(u"logOutBtn")
        self.logOutBtn.setGeometry(QRect(10, 590, 195, 35))
        self.logOutBtn.setFont(font1)
        self.logOutBtn.setStyleSheet(u"#QPushButton:hover{\n"
"	border-radius: 20px;\n"
"	background-color: rgb(90, 90, 90);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/EC8482/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logOutBtn.setIcon(icon8)
        self.logOutBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.Setting)

        self.centerMenuPages.addWidget(self.settingsPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.horizontalLayout_5 = QHBoxLayout(self.helpPage)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.helpLabel = QLabel(self.helpPage)
        self.helpLabel.setObjectName(u"helpLabel")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setWeight(50)
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
        icon9 = QIcon()
        icon9.addFile(u":/icons/EC8482/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon9)
        self.notificationBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.notificationBtn)

        self.moreMenuBtn = QPushButton(self.userMenu)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/EC8482/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon10)
        self.moreMenuBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.moreMenuBtn)

        self.profileMenuBtn = QPushButton(self.userMenu)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/EC8482/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileMenuBtn.setIcon(icon11)
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
        icon12 = QIcon()
        icon12.addFile(u":/icons/EC8482/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon12)
        self.minimizeBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.windowOptions)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/EC8482/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon13)
        self.restoreBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.windowOptions)
        self.closeBtn.setObjectName(u"closeBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/EC8482/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon14)
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
"}")
        self.verticalLayout_21 = QVBoxLayout(self.home_header)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.top_home = QWidget(self.home_header)
        self.top_home.setObjectName(u"top_home")
        self.top_home.setStyleSheet(u"")
        self.home_search_btn = QPushButton(self.top_home)
        self.home_search_btn.setObjectName(u"home_search_btn")
        self.home_search_btn.setGeometry(QRect(810, 0, 161, 41))
        font4 = QFont()
        font4.setFamily(u"Terminal")
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.home_search_btn.setFont(font4)
        self.home_search_btn.setStyleSheet(u"border-radius: 20px;\n"
"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        icon15 = QIcon()
        icon15.addFile(u":/icons/EC8482/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_search_btn.setIcon(icon15)
        self.home_search_line = QLineEdit(self.top_home)
        self.home_search_line.setObjectName(u"home_search_line")
        self.home_search_line.setEnabled(True)
        self.home_search_line.setGeometry(QRect(450, 0, 351, 42))
        font5 = QFont()
        font5.setFamily(u"Terminal")
        font5.setPointSize(15)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.home_search_line.setFont(font5)
        self.home_search_line.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.home_search_label = QLabel(self.top_home)
        self.home_search_label.setObjectName(u"home_search_label")
        self.home_search_label.setGeometry(QRect(330, 10, 111, 30))
        font6 = QFont()
        font6.setPointSize(15)
        font6.setBold(False)
        font6.setWeight(50)
        self.home_search_label.setFont(font6)
        self.home_search_label.setStyleSheet(u"")
        self.home_search_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_21.addWidget(self.top_home)

        self.middle_home = QWidget(self.home_header)
        self.middle_home.setObjectName(u"middle_home")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.middle_home.sizePolicy().hasHeightForWidth())
        self.middle_home.setSizePolicy(sizePolicy2)
        self.middle_home.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.middle_home)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.home_game_btn4 = QPushButton(self.middle_home)
        self.home_game_btn4.setObjectName(u"home_game_btn4")
        sizePolicy2.setHeightForWidth(self.home_game_btn4.sizePolicy().hasHeightForWidth())
        self.home_game_btn4.setSizePolicy(sizePolicy2)
        self.home_game_btn4.setFont(font4)
        self.home_game_btn4.setStyleSheet(u"border: 0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.home_game_btn4.setIconSize(QSize(319, 165))

        self.gridLayout_2.addWidget(self.home_game_btn4, 1, 0, 1, 1)

        self.home_game_btn1 = QPushButton(self.middle_home)
        self.home_game_btn1.setObjectName(u"home_game_btn1")
        sizePolicy2.setHeightForWidth(self.home_game_btn1.sizePolicy().hasHeightForWidth())
        self.home_game_btn1.setSizePolicy(sizePolicy2)
        self.home_game_btn1.setFont(font4)
        self.home_game_btn1.setStyleSheet(u"border: 0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.home_game_btn1.setIconSize(QSize(319, 165))
        self.home_game_btn1.setAutoRepeat(False)

        self.gridLayout_2.addWidget(self.home_game_btn1, 0, 0, 1, 1)

        self.home_game_btn3 = QPushButton(self.middle_home)
        self.home_game_btn3.setObjectName(u"home_game_btn3")
        sizePolicy2.setHeightForWidth(self.home_game_btn3.sizePolicy().hasHeightForWidth())
        self.home_game_btn3.setSizePolicy(sizePolicy2)
        self.home_game_btn3.setFont(font4)
        self.home_game_btn3.setStyleSheet(u"border: 0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.home_game_btn3.setIconSize(QSize(319, 165))

        self.gridLayout_2.addWidget(self.home_game_btn3, 0, 2, 1, 1)

        self.home_game_btn5 = QPushButton(self.middle_home)
        self.home_game_btn5.setObjectName(u"home_game_btn5")
        sizePolicy2.setHeightForWidth(self.home_game_btn5.sizePolicy().hasHeightForWidth())
        self.home_game_btn5.setSizePolicy(sizePolicy2)
        self.home_game_btn5.setFont(font4)
        self.home_game_btn5.setStyleSheet(u"border: 0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.home_game_btn5.setIconSize(QSize(319, 165))

        self.gridLayout_2.addWidget(self.home_game_btn5, 1, 1, 1, 1)

        self.home_game_btn6 = QPushButton(self.middle_home)
        self.home_game_btn6.setObjectName(u"home_game_btn6")
        sizePolicy2.setHeightForWidth(self.home_game_btn6.sizePolicy().hasHeightForWidth())
        self.home_game_btn6.setSizePolicy(sizePolicy2)
        self.home_game_btn6.setFont(font4)
        self.home_game_btn6.setStyleSheet(u"border: 0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.home_game_btn6.setIconSize(QSize(319, 165))

        self.gridLayout_2.addWidget(self.home_game_btn6, 1, 2, 1, 1)

        self.home_game_btn2 = QPushButton(self.middle_home)
        self.home_game_btn2.setObjectName(u"home_game_btn2")
        sizePolicy2.setHeightForWidth(self.home_game_btn2.sizePolicy().hasHeightForWidth())
        self.home_game_btn2.setSizePolicy(sizePolicy2)
        self.home_game_btn2.setFont(font4)
        self.home_game_btn2.setStyleSheet(u"border: 0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.home_game_btn2.setIconSize(QSize(319, 165))

        self.gridLayout_2.addWidget(self.home_game_btn2, 0, 1, 1, 1)


        self.verticalLayout_21.addWidget(self.middle_home)

        self.bottom_home = QWidget(self.home_header)
        self.bottom_home.setObjectName(u"bottom_home")
        self.home_more_game_btn = QPushButton(self.bottom_home)
        self.home_more_game_btn.setObjectName(u"home_more_game_btn")
        self.home_more_game_btn.setGeometry(QRect(880, 0, 71, 41))
        self.home_more_game_btn.setFont(font4)
        self.home_more_game_btn.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 255, 255);\n"
"border-radius: 20px;")
        icon16 = QIcon()
        icon16.addFile(u":/icons/EC8482/chevrons-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_more_game_btn.setIcon(icon16)
        self.home_more_game_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_21.addWidget(self.bottom_home)

        self.verticalLayout_21.setStretch(0, 1)
        self.verticalLayout_21.setStretch(1, 7)
        self.verticalLayout_21.setStretch(2, 1)

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
"}")
        self.verticalLayout_16 = QVBoxLayout(self.library_header)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.top_library = QWidget(self.library_header)
        self.top_library.setObjectName(u"top_library")
        self.library_search_btn = QPushButton(self.top_library)
        self.library_search_btn.setObjectName(u"library_search_btn")
        self.library_search_btn.setGeometry(QRect(810, 0, 161, 41))
        self.library_search_btn.setFont(font4)
        self.library_search_btn.setStyleSheet(u"border-radius: 20px;\n"
"color: #EC8482;\n"
"background-color: rgb(0, 0, 0);")
        self.library_search_btn.setIcon(icon15)
        self.library_search_line = QLineEdit(self.top_library)
        self.library_search_line.setObjectName(u"library_search_line")
        self.library_search_line.setEnabled(True)
        self.library_search_line.setGeometry(QRect(450, 0, 351, 42))
        self.library_search_line.setFont(font5)
        self.library_search_line.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.library_search_label = QLabel(self.top_library)
        self.library_search_label.setObjectName(u"library_search_label")
        self.library_search_label.setGeometry(QRect(330, 10, 111, 30))
        self.library_search_label.setFont(font6)
        self.library_search_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(self.top_library)

        self.middle_library = QWidget(self.library_header)
        self.middle_library.setObjectName(u"middle_library")
        sizePolicy2.setHeightForWidth(self.middle_library.sizePolicy().hasHeightForWidth())
        self.middle_library.setSizePolicy(sizePolicy2)
        self.middle_library.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.middle_library)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.library_game_btn4 = QPushButton(self.middle_library)
        self.library_game_btn4.setObjectName(u"library_game_btn4")
        sizePolicy2.setHeightForWidth(self.library_game_btn4.sizePolicy().hasHeightForWidth())
        self.library_game_btn4.setSizePolicy(sizePolicy2)
        self.library_game_btn4.setFont(font4)
        self.library_game_btn4.setStyleSheet(u"border: 0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.library_game_btn4.setIconSize(QSize(320, 165))

        self.gridLayout.addWidget(self.library_game_btn4, 1, 0, 1, 1)

        self.library_game_btn2 = QPushButton(self.middle_library)
        self.library_game_btn2.setObjectName(u"library_game_btn2")
        sizePolicy2.setHeightForWidth(self.library_game_btn2.sizePolicy().hasHeightForWidth())
        self.library_game_btn2.setSizePolicy(sizePolicy2)
        self.library_game_btn2.setFont(font4)
        self.library_game_btn2.setStyleSheet(u"border: 0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.library_game_btn2.setIconSize(QSize(320, 165))

        self.gridLayout.addWidget(self.library_game_btn2, 0, 1, 1, 1)

        self.library_game_btn6 = QPushButton(self.middle_library)
        self.library_game_btn6.setObjectName(u"library_game_btn6")
        sizePolicy2.setHeightForWidth(self.library_game_btn6.sizePolicy().hasHeightForWidth())
        self.library_game_btn6.setSizePolicy(sizePolicy2)
        self.library_game_btn6.setFont(font4)
        self.library_game_btn6.setStyleSheet(u"border: 0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.library_game_btn6.setIconSize(QSize(320, 165))

        self.gridLayout.addWidget(self.library_game_btn6, 1, 2, 1, 1)

        self.library_game_btn1 = QPushButton(self.middle_library)
        self.library_game_btn1.setObjectName(u"library_game_btn1")
        sizePolicy2.setHeightForWidth(self.library_game_btn1.sizePolicy().hasHeightForWidth())
        self.library_game_btn1.setSizePolicy(sizePolicy2)
        self.library_game_btn1.setFont(font4)
        self.library_game_btn1.setStyleSheet(u"border: 0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.library_game_btn1.setIconSize(QSize(320, 165))
        self.library_game_btn1.setAutoRepeat(False)

        self.gridLayout.addWidget(self.library_game_btn1, 0, 0, 1, 1)

        self.library_game_btn3 = QPushButton(self.middle_library)
        self.library_game_btn3.setObjectName(u"library_game_btn3")
        sizePolicy2.setHeightForWidth(self.library_game_btn3.sizePolicy().hasHeightForWidth())
        self.library_game_btn3.setSizePolicy(sizePolicy2)
        self.library_game_btn3.setFont(font4)
        self.library_game_btn3.setStyleSheet(u"border: 0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.library_game_btn3.setIconSize(QSize(320, 165))

        self.gridLayout.addWidget(self.library_game_btn3, 0, 2, 1, 1)

        self.library_game_btn5 = QPushButton(self.middle_library)
        self.library_game_btn5.setObjectName(u"library_game_btn5")
        sizePolicy2.setHeightForWidth(self.library_game_btn5.sizePolicy().hasHeightForWidth())
        self.library_game_btn5.setSizePolicy(sizePolicy2)
        self.library_game_btn5.setFont(font4)
        self.library_game_btn5.setStyleSheet(u"border: 0px;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.library_game_btn5.setIconSize(QSize(320, 165))

        self.gridLayout.addWidget(self.library_game_btn5, 1, 1, 1, 1)


        self.verticalLayout_16.addWidget(self.middle_library)

        self.bottom_library = QWidget(self.library_header)
        self.bottom_library.setObjectName(u"bottom_library")
        self.library_more_game_btn = QPushButton(self.bottom_library)
        self.library_more_game_btn.setObjectName(u"library_more_game_btn")
        self.library_more_game_btn.setGeometry(QRect(880, 0, 71, 41))
        self.library_more_game_btn.setFont(font4)
        self.library_more_game_btn.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 255, 255);\n"
"border-radius: 20px;")
        self.library_more_game_btn.setIcon(icon16)
        self.library_more_game_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_16.addWidget(self.bottom_library)

        self.verticalLayout_16.setStretch(0, 1)
        self.verticalLayout_16.setStretch(1, 7)
        self.verticalLayout_16.setStretch(2, 1)

        self.verticalLayout_15.addWidget(self.library_header)

        self.mainPages.addWidget(self.libraryPage)
        self.cartsPage = QWidget()
        self.cartsPage.setObjectName(u"cartsPage")
        self.cartsPage.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_20 = QVBoxLayout(self.cartsPage)
        self.verticalLayout_20.setSpacing(10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(10, 10, 10, 10)
        self.titleCart = QWidget(self.cartsPage)
        self.titleCart.setObjectName(u"titleCart")
        self.titleCart.setStyleSheet(u"")
        self.payMethodBox = QComboBox(self.titleCart)
        self.payMethodBox.addItem("")
        self.payMethodBox.addItem("")
        self.payMethodBox.addItem("")
        self.payMethodBox.addItem("")
        self.payMethodBox.setObjectName(u"payMethodBox")
        self.payMethodBox.setGeometry(QRect(760, 10, 201, 41))
        font7 = QFont()
        font7.setPointSize(11)
        font7.setStrikeOut(False)
        self.payMethodBox.setFont(font7)
        self.payMethodBox.setStyleSheet(u"border: 2px solid rgb(255,255,255);\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"border-radius: 5px;")

        self.verticalLayout_20.addWidget(self.titleCart)

        self.listOrder = QScrollArea(self.cartsPage)
        self.listOrder.setObjectName(u"listOrder")
        self.listOrder.setStyleSheet(u"border: 2px solid rgb(255,255,255);")
        self.listOrder.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.listOrder.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 75, 1000))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 1000))
        self.gameOrderBox_1 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_1.setObjectName(u"gameOrderBox_1")
        self.gameOrderBox_1.setGeometry(QRect(10, 10, 931, 101))
        self.gameOrderBox_1.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(255,255,255);\n"
"background-color: #2c313c;")
        self.nameGameOrder_1 = QLabel(self.gameOrderBox_1)
        self.nameGameOrder_1.setObjectName(u"nameGameOrder_1")
        self.nameGameOrder_1.setGeometry(QRect(200, 30, 551, 41))
        self.nameGameOrder_1.setFont(font1)
        self.nameGameOrder_1.setStyleSheet(u"border: 0px;")
        self.avtGameOrder_1 = QLabel(self.gameOrderBox_1)
        self.avtGameOrder_1.setObjectName(u"avtGameOrder_1")
        self.avtGameOrder_1.setGeometry(QRect(10, 10, 154, 81))
        self.avtGameOrder_1.setStyleSheet(u"border: 1px solid #000;\n"
"border-radius: 0px;")
        self.avtGameOrder_1.setScaledContents(True)
        self.deleteOrder_1 = QPushButton(self.gameOrderBox_1)
        self.deleteOrder_1.setObjectName(u"deleteOrder_1")
        self.deleteOrder_1.setGeometry(QRect(860, 30, 40, 40))
        self.deleteOrder_1.setStyleSheet(u"border:0px;\n"
"padding: 0px")
        icon17 = QIcon()
        icon17.addFile(u":/icons/EC8482/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteOrder_1.setIcon(icon17)
        self.deleteOrder_1.setIconSize(QSize(30, 30))
        self.gameOrderBox_2 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_2.setObjectName(u"gameOrderBox_2")
        self.gameOrderBox_2.setGeometry(QRect(10, 120, 931, 101))
        self.gameOrderBox_2.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(255,255,255);\n"
"background-color: #2c313c;")
        self.nameGameOrder_2 = QLabel(self.gameOrderBox_2)
        self.nameGameOrder_2.setObjectName(u"nameGameOrder_2")
        self.nameGameOrder_2.setGeometry(QRect(200, 30, 551, 41))
        self.nameGameOrder_2.setFont(font1)
        self.nameGameOrder_2.setStyleSheet(u"border: 0px;")
        self.avtGameOrder_2 = QLabel(self.gameOrderBox_2)
        self.avtGameOrder_2.setObjectName(u"avtGameOrder_2")
        self.avtGameOrder_2.setGeometry(QRect(10, 10, 154, 81))
        self.avtGameOrder_2.setStyleSheet(u"border: 1px solid #000;\n"
"border-radius: 0px;")
        self.avtGameOrder_2.setScaledContents(True)
        self.deleteOrder_2 = QPushButton(self.gameOrderBox_2)
        self.deleteOrder_2.setObjectName(u"deleteOrder_2")
        self.deleteOrder_2.setGeometry(QRect(860, 30, 40, 40))
        self.deleteOrder_2.setStyleSheet(u"border:0px;\n"
"padding: 0px")
        self.deleteOrder_2.setIcon(icon17)
        self.deleteOrder_2.setIconSize(QSize(30, 30))
        self.gameOrderBox_3 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_3.setObjectName(u"gameOrderBox_3")
        self.gameOrderBox_3.setGeometry(QRect(10, 230, 931, 101))
        self.gameOrderBox_3.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(255,255,255);\n"
"background-color: #2c313c;")
        self.nameGameOrder_3 = QLabel(self.gameOrderBox_3)
        self.nameGameOrder_3.setObjectName(u"nameGameOrder_3")
        self.nameGameOrder_3.setGeometry(QRect(200, 30, 551, 41))
        self.nameGameOrder_3.setFont(font1)
        self.nameGameOrder_3.setStyleSheet(u"border: 0px;")
        self.avtGameOrder_3 = QLabel(self.gameOrderBox_3)
        self.avtGameOrder_3.setObjectName(u"avtGameOrder_3")
        self.avtGameOrder_3.setGeometry(QRect(10, 10, 154, 81))
        self.avtGameOrder_3.setStyleSheet(u"border: 1px solid #000;\n"
"border-radius: 0px;")
        self.avtGameOrder_3.setScaledContents(True)
        self.deleteOrder_3 = QPushButton(self.gameOrderBox_3)
        self.deleteOrder_3.setObjectName(u"deleteOrder_3")
        self.deleteOrder_3.setGeometry(QRect(860, 30, 40, 40))
        self.deleteOrder_3.setStyleSheet(u"border:0px;\n"
"padding: 0px")
        self.deleteOrder_3.setIcon(icon17)
        self.deleteOrder_3.setIconSize(QSize(30, 30))
        self.gameOrderBox_5 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_5.setObjectName(u"gameOrderBox_5")
        self.gameOrderBox_5.setGeometry(QRect(10, 450, 931, 101))
        self.gameOrderBox_5.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(255,255,255);\n"
"background-color: #2c313c;")
        self.nameGameOrder_5 = QLabel(self.gameOrderBox_5)
        self.nameGameOrder_5.setObjectName(u"nameGameOrder_5")
        self.nameGameOrder_5.setGeometry(QRect(200, 30, 551, 41))
        self.nameGameOrder_5.setFont(font1)
        self.nameGameOrder_5.setStyleSheet(u"border: 0px;")
        self.avtGameOrder_5 = QLabel(self.gameOrderBox_5)
        self.avtGameOrder_5.setObjectName(u"avtGameOrder_5")
        self.avtGameOrder_5.setGeometry(QRect(10, 10, 154, 81))
        self.avtGameOrder_5.setStyleSheet(u"border: 1px solid #000;\n"
"border-radius: 0px;")
        self.avtGameOrder_5.setScaledContents(True)
        self.deleteOrder_5 = QPushButton(self.gameOrderBox_5)
        self.deleteOrder_5.setObjectName(u"deleteOrder_5")
        self.deleteOrder_5.setGeometry(QRect(860, 30, 40, 40))
        self.deleteOrder_5.setStyleSheet(u"border:0px;\n"
"padding: 0px")
        self.deleteOrder_5.setIcon(icon17)
        self.deleteOrder_5.setIconSize(QSize(30, 30))
        self.gameOrderBox_4 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_4.setObjectName(u"gameOrderBox_4")
        self.gameOrderBox_4.setGeometry(QRect(10, 340, 931, 101))
        self.gameOrderBox_4.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(255,255,255);\n"
"background-color: #2c313c;")
        self.nameGameOrder_4 = QLabel(self.gameOrderBox_4)
        self.nameGameOrder_4.setObjectName(u"nameGameOrder_4")
        self.nameGameOrder_4.setGeometry(QRect(200, 30, 551, 41))
        self.nameGameOrder_4.setFont(font1)
        self.nameGameOrder_4.setStyleSheet(u"border: 0px;")
        self.avtGameOrder_4 = QLabel(self.gameOrderBox_4)
        self.avtGameOrder_4.setObjectName(u"avtGameOrder_4")
        self.avtGameOrder_4.setGeometry(QRect(10, 10, 154, 81))
        self.avtGameOrder_4.setStyleSheet(u"border: 1px solid #000;\n"
"border-radius: 0px;")
        self.avtGameOrder_4.setScaledContents(True)
        self.deleteOrder_4 = QPushButton(self.gameOrderBox_4)
        self.deleteOrder_4.setObjectName(u"deleteOrder_4")
        self.deleteOrder_4.setGeometry(QRect(860, 30, 40, 40))
        self.deleteOrder_4.setStyleSheet(u"border:0px;\n"
"padding: 0px")
        self.deleteOrder_4.setIcon(icon17)
        self.deleteOrder_4.setIconSize(QSize(30, 30))
        self.gameOrderBox_7 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_7.setObjectName(u"gameOrderBox_7")
        self.gameOrderBox_7.setGeometry(QRect(10, 560, 931, 101))
        self.gameOrderBox_7.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(255,255,255);\n"
"background-color: #2c313c;")
        self.nameGameOrder_7 = QLabel(self.gameOrderBox_7)
        self.nameGameOrder_7.setObjectName(u"nameGameOrder_7")
        self.nameGameOrder_7.setGeometry(QRect(200, 30, 551, 41))
        self.nameGameOrder_7.setFont(font1)
        self.nameGameOrder_7.setStyleSheet(u"border: 0px;")
        self.avtGameOrder_7 = QLabel(self.gameOrderBox_7)
        self.avtGameOrder_7.setObjectName(u"avtGameOrder_7")
        self.avtGameOrder_7.setGeometry(QRect(10, 10, 154, 81))
        self.avtGameOrder_7.setStyleSheet(u"border: 1px solid #000;\n"
"border-radius: 0px;")
        self.avtGameOrder_7.setScaledContents(True)
        self.deleteOrder_7 = QPushButton(self.gameOrderBox_7)
        self.deleteOrder_7.setObjectName(u"deleteOrder_7")
        self.deleteOrder_7.setGeometry(QRect(860, 30, 40, 40))
        self.deleteOrder_7.setStyleSheet(u"border:0px;\n"
"padding: 0px")
        self.deleteOrder_7.setIcon(icon17)
        self.deleteOrder_7.setIconSize(QSize(30, 30))
        self.gameOrderBox_8 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_8.setObjectName(u"gameOrderBox_8")
        self.gameOrderBox_8.setGeometry(QRect(10, 890, 931, 101))
        self.gameOrderBox_8.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(255,255,255);\n"
"background-color: #2c313c;")
        self.nameGameOrder_8 = QLabel(self.gameOrderBox_8)
        self.nameGameOrder_8.setObjectName(u"nameGameOrder_8")
        self.nameGameOrder_8.setGeometry(QRect(200, 30, 551, 41))
        self.nameGameOrder_8.setFont(font1)
        self.nameGameOrder_8.setStyleSheet(u"border: 0px;")
        self.avtGameOrder_8 = QLabel(self.gameOrderBox_8)
        self.avtGameOrder_8.setObjectName(u"avtGameOrder_8")
        self.avtGameOrder_8.setGeometry(QRect(10, 10, 154, 81))
        self.avtGameOrder_8.setStyleSheet(u"border: 1px solid #000;\n"
"border-radius: 0px;")
        self.avtGameOrder_8.setScaledContents(True)
        self.deleteOrder_8 = QPushButton(self.gameOrderBox_8)
        self.deleteOrder_8.setObjectName(u"deleteOrder_8")
        self.deleteOrder_8.setGeometry(QRect(860, 30, 40, 40))
        self.deleteOrder_8.setStyleSheet(u"border:0px;\n"
"padding: 0px")
        self.deleteOrder_8.setIcon(icon17)
        self.deleteOrder_8.setIconSize(QSize(30, 30))
        self.gameOrderBox_9 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_9.setObjectName(u"gameOrderBox_9")
        self.gameOrderBox_9.setGeometry(QRect(10, 670, 931, 101))
        self.gameOrderBox_9.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(255,255,255);\n"
"background-color: #2c313c;")
        self.nameGameOrder_9 = QLabel(self.gameOrderBox_9)
        self.nameGameOrder_9.setObjectName(u"nameGameOrder_9")
        self.nameGameOrder_9.setGeometry(QRect(200, 30, 551, 41))
        self.nameGameOrder_9.setFont(font1)
        self.nameGameOrder_9.setStyleSheet(u"border: 0px;")
        self.avtGameOrder_9 = QLabel(self.gameOrderBox_9)
        self.avtGameOrder_9.setObjectName(u"avtGameOrder_9")
        self.avtGameOrder_9.setGeometry(QRect(10, 10, 154, 81))
        self.avtGameOrder_9.setStyleSheet(u"border: 1px solid #000;\n"
"border-radius: 0px;")
        self.avtGameOrder_9.setScaledContents(True)
        self.deleteOrder_9 = QPushButton(self.gameOrderBox_9)
        self.deleteOrder_9.setObjectName(u"deleteOrder_9")
        self.deleteOrder_9.setGeometry(QRect(860, 30, 40, 40))
        self.deleteOrder_9.setStyleSheet(u"border:0px;\n"
"padding: 0px")
        self.deleteOrder_9.setIcon(icon17)
        self.deleteOrder_9.setIconSize(QSize(30, 30))
        self.gameOrderBox_6 = QWidget(self.scrollAreaWidgetContents)
        self.gameOrderBox_6.setObjectName(u"gameOrderBox_6")
        self.gameOrderBox_6.setGeometry(QRect(10, 780, 931, 101))
        self.gameOrderBox_6.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(255,255,255);\n"
"background-color: #2c313c;")
        self.nameGameOrder_6 = QLabel(self.gameOrderBox_6)
        self.nameGameOrder_6.setObjectName(u"nameGameOrder_6")
        self.nameGameOrder_6.setGeometry(QRect(200, 30, 551, 41))
        self.nameGameOrder_6.setFont(font1)
        self.nameGameOrder_6.setStyleSheet(u"border: 0px;")
        self.avtGameOrder_6 = QLabel(self.gameOrderBox_6)
        self.avtGameOrder_6.setObjectName(u"avtGameOrder_6")
        self.avtGameOrder_6.setGeometry(QRect(10, 10, 154, 81))
        self.avtGameOrder_6.setStyleSheet(u"border: 1px solid #000;\n"
"border-radius: 0px;")
        self.avtGameOrder_6.setScaledContents(True)
        self.deleteOrder_6 = QPushButton(self.gameOrderBox_6)
        self.deleteOrder_6.setObjectName(u"deleteOrder_6")
        self.deleteOrder_6.setGeometry(QRect(860, 30, 40, 40))
        self.deleteOrder_6.setStyleSheet(u"border:0px;\n"
"padding: 0px")
        self.deleteOrder_6.setIcon(icon17)
        self.deleteOrder_6.setIconSize(QSize(30, 30))
        self.listOrder.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_20.addWidget(self.listOrder)

        self.orderBtn = QWidget(self.cartsPage)
        self.orderBtn.setObjectName(u"orderBtn")
        self.orderBtn.setStyleSheet(u"")
        self.payBtn = QPushButton(self.orderBtn)
        self.payBtn.setObjectName(u"payBtn")
        self.payBtn.setGeometry(QRect(850, 0, 111, 41))
        font8 = QFont()
        font8.setFamily(u"MS Shell Dlg 2")
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setWeight(50)
        self.payBtn.setFont(font8)
        self.payBtn.setLayoutDirection(Qt.LeftToRight)
        self.payBtn.setStyleSheet(u"color: #EC8482;\n"
"background-color: rgb(0, 255, 255);\n"
"border-radius: 20px;")
        icon18 = QIcon()
        icon18.addFile(u":/icons/EC8482/dollar-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.payBtn.setIcon(icon18)
        self.payBtn.setIconSize(QSize(30, 30))
        self.totalCost = QLabel(self.orderBtn)
        self.totalCost.setObjectName(u"totalCost")
        self.totalCost.setEnabled(True)
        self.totalCost.setGeometry(QRect(650, 0, 191, 41))
        font9 = QFont()
        font9.setFamily(u"MS Shell Dlg 2")
        font9.setPointSize(12)
        self.totalCost.setFont(font9)
        self.totalCost.setStyleSheet(u"border: 1px solid rgb(255,255,255);\n"
"padding-left: 10px;")

        self.verticalLayout_20.addWidget(self.orderBtn)

        self.verticalLayout_20.setStretch(0, 1)
        self.verticalLayout_20.setStretch(1, 6)
        self.verticalLayout_20.setStretch(2, 1)
        self.mainPages.addWidget(self.cartsPage)
        self.gameInfoPage = QWidget()
        self.gameInfoPage.setObjectName(u"gameInfoPage")
        self.verticalLayout_19 = QVBoxLayout(self.gameInfoPage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gameInfo = QWidget(self.gameInfoPage)
        self.gameInfo.setObjectName(u"gameInfo")
        self.gameInfo.setMinimumSize(QSize(0, 350))
        self.gameInfo.setFont(font6)
        self.gameInfo.setStyleSheet(u"QLineEdit\n"
"{\n"
"	background-color: #fff;\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgba(0, 0, 0, 100);\n"
"	padding: 10px;\n"
"	padding-left: 17px;\n"
"	color: #rgb(0,255,255);\n"
"}")
        self.idGameLabel = QLabel(self.gameInfo)
        self.idGameLabel.setObjectName(u"idGameLabel")
        self.idGameLabel.setGeometry(QRect(380, 20, 80, 30))
        self.idGameLabel.setFont(font6)
        self.idGameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.nameGameLabel = QLabel(self.gameInfo)
        self.nameGameLabel.setObjectName(u"nameGameLabel")
        self.nameGameLabel.setGeometry(QRect(380, 90, 80, 30))
        self.nameGameLabel.setFont(font6)
        self.nameGameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.priceGameLabel = QLabel(self.gameInfo)
        self.priceGameLabel.setObjectName(u"priceGameLabel")
        self.priceGameLabel.setGeometry(QRect(380, 160, 80, 30))
        self.priceGameLabel.setFont(font6)
        self.priceGameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.avtGame = QLabel(self.gameInfo)
        self.avtGame.setObjectName(u"avtGame")
        self.avtGame.setGeometry(QRect(30, 10, 320, 180))
        self.avtGame.setStyleSheet(u"")
        self.avtGame.setLineWidth(0)
        self.avtGame.setTextFormat(Qt.MarkdownText)
        self.avtGame.setPixmap(QPixmap(u":/images/icon-app-user.png"))
        self.avtGame.setScaledContents(True)
        self.avtGame.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.avtGame.setMargin(6)
        self.videoWidget = QWidget(self.gameInfo)
        self.videoWidget.setObjectName(u"videoWidget")
        self.videoWidget.setGeometry(QRect(30, 210, 320, 180))
        self.videoWidget.setStyleSheet(u"border: 2px SOLID rgba(0,0,0,100)")
        self.vidGame = QLabel(self.videoWidget)
        self.vidGame.setObjectName(u"vidGame")
        self.vidGame.setGeometry(QRect(8, 4, 304, 171))
        self.vidGame.setAlignment(Qt.AlignCenter)
        self.PlayBuyBtn = QPushButton(self.gameInfo)
        self.PlayBuyBtn.setObjectName(u"PlayBuyBtn")
        self.PlayBuyBtn.setGeometry(QRect(90, 400, 181, 41))
        font10 = QFont()
        font10.setFamily(u"MS Shell Dlg 2")
        font10.setPointSize(14)
        font10.setBold(False)
        font10.setItalic(False)
        font10.setWeight(50)
        self.PlayBuyBtn.setFont(font10)
        self.PlayBuyBtn.setStyleSheet(u"#PlayBuyBtn{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 255, 255);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#PlayBuyBtn:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 109, 109);\n"
"	border-radius: 20px;\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/icons/EC8482/airplay.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.PlayBuyBtn.setIcon(icon19)
        self.descriptionGame = QLabel(self.gameInfo)
        self.descriptionGame.setObjectName(u"descriptionGame")
        self.descriptionGame.setGeometry(QRect(470, 220, 491, 221))
        font11 = QFont()
        font11.setPointSize(10)
        font11.setBold(False)
        font11.setWeight(50)
        self.descriptionGame.setFont(font11)
        self.descriptionGame.setStyleSheet(u"border-radius: 20px;\n"
"border: 2px solid rgba(0,0,0,100);\n"
"background-color: rgba(255,255,255,255);\n"
"color: rgb(0,0,0);\n"
"padding-top: 7px;\n"
"padding-left: 7px;")
        self.descriptionGame.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.descriptionGame.setWordWrap(True)
        self.descriptionGame.setMargin(0)
        self.idGameText = QLabel(self.gameInfo)
        self.idGameText.setObjectName(u"idGameText")
        self.idGameText.setGeometry(QRect(470, 10, 471, 51))
        font12 = QFont()
        font12.setPointSize(13)
        self.idGameText.setFont(font12)
        self.idGameText.setStyleSheet(u"border-radius: 20px;\n"
"border: 2px solid rgba(0,0,0,100);\n"
"background-color: rgba(255,255,255,255);\n"
"color: rgb(0,0,0);\n"
"padding-left: 7px;")
        self.idGameText.setWordWrap(True)
        self.idGameText.setMargin(0)
        self.nameGameText = QLabel(self.gameInfo)
        self.nameGameText.setObjectName(u"nameGameText")
        self.nameGameText.setGeometry(QRect(470, 80, 471, 51))
        self.nameGameText.setFont(font12)
        self.nameGameText.setStyleSheet(u"border-radius: 20px;\n"
"border: 2px solid rgba(0,0,0,100);\n"
"background-color: rgba(255,255,255,255);\n"
"color: rgb(0,0,0);\n"
"padding-left: 7px;")
        self.nameGameText.setWordWrap(True)
        self.nameGameText.setMargin(0)
        self.priceGameText = QLabel(self.gameInfo)
        self.priceGameText.setObjectName(u"priceGameText")
        self.priceGameText.setGeometry(QRect(470, 150, 471, 51))
        self.priceGameText.setFont(font12)
        self.priceGameText.setStyleSheet(u"border-radius: 20px;\n"
"border: 2px solid rgba(0,0,0,100);\n"
"background-color: rgba(255,255,255,255);\n"
"color: rgb(0,0,0);\n"
"padding-left: 7px;")
        self.priceGameText.setWordWrap(True)
        self.priceGameText.setMargin(0)

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
        self.userInfor.setFont(font6)
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
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(244, 244, 244);\n"
"}")
        self.idLabel = QLabel(self.userInfor)
        self.idLabel.setObjectName(u"idLabel")
        self.idLabel.setGeometry(QRect(20, 30, 150, 30))
        self.idLabel.setFont(font6)
        self.idLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.nameLabel = QLabel(self.userInfor)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(20, 100, 150, 30))
        self.nameLabel.setFont(font6)
        self.nameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.emailLabel = QLabel(self.userInfor)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setGeometry(QRect(20, 170, 150, 30))
        self.emailLabel.setFont(font6)
        self.emailLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.passwordLabel = QLabel(self.userInfor)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(20, 240, 150, 30))
        self.passwordLabel.setFont(font6)
        self.passwordLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.idLine = QLineEdit(self.userInfor)
        self.idLine.setObjectName(u"idLine")
        self.idLine.setEnabled(True)
        self.idLine.setGeometry(QRect(200, 30, 381, 41))
        font13 = QFont()
        font13.setFamily(u"Arial")
        font13.setPointSize(11)
        font13.setBold(False)
        font13.setItalic(False)
        font13.setWeight(50)
        self.idLine.setFont(font13)
        self.idLine.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding: 0px 0px 0px 15px;")
        self.nameLine = QLineEdit(self.userInfor)
        self.nameLine.setObjectName(u"nameLine")
        self.nameLine.setEnabled(True)
        self.nameLine.setGeometry(QRect(200, 100, 381, 41))
        self.nameLine.setFont(font13)
        self.nameLine.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding: 0px 0px 0px 15px;")
        self.emailLine = QLineEdit(self.userInfor)
        self.emailLine.setObjectName(u"emailLine")
        self.emailLine.setGeometry(QRect(200, 170, 381, 41))
        self.emailLine.setFont(font13)
        self.emailLine.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding: 0px 0px 0px 15px;")
        self.passLine = QLineEdit(self.userInfor)
        self.passLine.setObjectName(u"passLine")
        self.passLine.setGeometry(QRect(200, 240, 381, 41))
        self.passLine.setFont(font13)
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
        font14 = QFont()
        font14.setPointSize(12)
        self.doneBtn.setFont(font14)
        self.doneBtn.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 255, 255);")
        icon20 = QIcon()
        icon20.addFile(u":/icons/EC8482/check-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.doneBtn.setIcon(icon20)
        self.cancelBtn = QPushButton(self.userBtn)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setGeometry(QRect(530, 40, 181, 41))
        self.cancelBtn.setFont(font14)
        self.cancelBtn.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(206, 103, 114);")
        icon21 = QIcon()
        icon21.addFile(u":/icons/EC8482/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelBtn.setIcon(icon21)

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
        font15 = QFont()
        font15.setPointSize(10)
        font15.setBold(True)
        font15.setWeight(75)
        self.notificationTitle.setFont(font15)

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
        icon22 = QIcon()
        icon22.addFile(u":/icons/EC8482/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon22)
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
        self.mainLogin.setStyleSheet(u"background-color: #2c313c;")
        self.LoginForm = QWidget(self.mainLogin)
        self.LoginForm.setObjectName(u"LoginForm")
        self.LoginForm.setGeometry(QRect(60, 170, 501, 301))
        self.LoginForm.setStyleSheet(u"border-radius: 20px;\n"
"border: 2px #EC8482;\n"
"background-color: #1f232a;")
        self.RegisterButton = QPushButton(self.LoginForm)
        self.RegisterButton.setObjectName(u"RegisterButton")
        self.RegisterButton.setGeometry(QRect(50, 240, 141, 41))
        self.RegisterButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.RegisterButton.setStyleSheet(u"QPushButton#RegisterButton\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 2px solid #EC8482;\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgba(0,0,0)\n"
"}\n"
"QPushButton#RegisterButton:hover\n"
"{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgba(236, 132, 130, 255);\n"
"}")
        self.LoginButton = QPushButton(self.LoginForm)
        self.LoginButton.setObjectName(u"LoginButton")
        self.LoginButton.setGeometry(QRect(210, 240, 241, 41))
        self.LoginButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.LoginButton.setStyleSheet(u"QPushButton#LoginButton\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 2px solid #EC8482;\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgba(0,0,0)\n"
"}\n"
"QPushButton#LoginButton:hover\n"
"{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgba(236, 132, 130, 255);\n"
"}")
        self.PasswordInput = QLineEdit(self.LoginForm)
        self.PasswordInput.setObjectName(u"PasswordInput")
        self.PasswordInput.setGeometry(QRect(170, 139, 281, 42))
        self.PasswordInput.setStyleSheet(u"QLineEdit#PasswordInput\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 2px solid #EC8482;\n"
"	padding: 10px;\n"
"	padding-left: 17px;\n"
"}\n"
"QLineEdit#PasswordInput:hover\n"
"{\n"
"\n"
"}")
        self.PasswordInput.setEchoMode(QLineEdit.Password)
        self.UsernameInput = QLineEdit(self.LoginForm)
        self.UsernameInput.setObjectName(u"UsernameInput")
        self.UsernameInput.setGeometry(QRect(170, 70, 281, 41))
        self.UsernameInput.setStyleSheet(u"QLineEdit#UsernameInput\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 2px solid #EC8482;\n"
"	padding: 10px;\n"
"	padding-left: 17px;\n"
"}\n"
"QLineEdit#UsernameInput:hover\n"
"{\n"
"\n"
"}")
        self.emailLoginLabel = QLabel(self.LoginForm)
        self.emailLoginLabel.setObjectName(u"emailLoginLabel")
        self.emailLoginLabel.setGeometry(QRect(0, 80, 161, 31))
        font16 = QFont()
        font16.setFamily(u"Arial")
        font16.setPointSize(14)
        font16.setBold(False)
        font16.setWeight(50)
        self.emailLoginLabel.setFont(font16)
        self.emailLoginLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.passwordLoginLabel = QLabel(self.LoginForm)
        self.passwordLoginLabel.setObjectName(u"passwordLoginLabel")
        self.passwordLoginLabel.setGeometry(QRect(0, 150, 161, 31))
        self.passwordLoginLabel.setFont(font16)
        self.passwordLoginLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.signUpLabel_2 = QLabel(self.LoginForm)
        self.signUpLabel_2.setObjectName(u"signUpLabel_2")
        self.signUpLabel_2.setGeometry(QRect(170, 10, 161, 51))
        font17 = QFont()
        font17.setFamily(u"Arial")
        font17.setPointSize(15)
        font17.setBold(True)
        font17.setWeight(75)
        self.signUpLabel_2.setFont(font17)
        self.signUpLabel_2.setStyleSheet(u"")
        self.signUpLabel_2.setAlignment(Qt.AlignCenter)
        self.wrongUserInputLabel = QLabel(self.LoginForm)
        self.wrongUserInputLabel.setObjectName(u"wrongUserInputLabel")
        self.wrongUserInputLabel.setGeometry(QRect(100, 195, 291, 31))
        font18 = QFont()
        font18.setFamily(u"MS Shell Dlg 2")
        font18.setPointSize(11)
        font18.setBold(False)
        font18.setWeight(50)
        self.wrongUserInputLabel.setFont(font18)
        self.wrongUserInputLabel.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.wrongUserInputLabel.setAlignment(Qt.AlignCenter)
        self.RegisterForm = QWidget(self.mainLogin)
        self.RegisterForm.setObjectName(u"RegisterForm")
        self.RegisterForm.setGeometry(QRect(710, 10, 501, 631))
        self.RegisterForm.setStyleSheet(u"border-radius: 20px;\n"
"border: 2px #EC8482;\n"
"background-color: #1f232a;\n"
"")
        self.passwordSignUp = QLineEdit(self.RegisterForm)
        self.passwordSignUp.setObjectName(u"passwordSignUp")
        self.passwordSignUp.setGeometry(QRect(190, 240, 281, 42))
        self.passwordSignUp.setStyleSheet(u"QLineEdit#passwordSignUp\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 2px solid #EC8482;\n"
"	padding: 10px;\n"
"	padding-left: 17px;\n"
"}\n"
"QLineEdit#passwordSignUp:hover\n"
"{\n"
"\n"
"}")
        self.passwordSignUp.setEchoMode(QLineEdit.Normal)
        self.emailSignUp = QLineEdit(self.RegisterForm)
        self.emailSignUp.setObjectName(u"emailSignUp")
        self.emailSignUp.setGeometry(QRect(190, 171, 281, 41))
        self.emailSignUp.setStyleSheet(u"QLineEdit#emailSignUp\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 2px solid #EC8482;\n"
"	padding: 10px;\n"
"	padding-left: 17px;\n"
"}")
        self.emailSignUp.setEchoMode(QLineEdit.Normal)
        self.nameSignUp = QLineEdit(self.RegisterForm)
        self.nameSignUp.setObjectName(u"nameSignUp")
        self.nameSignUp.setGeometry(QRect(190, 100, 281, 42))
        self.nameSignUp.setStyleSheet(u"QLineEdit#nameSignUp\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 2px solid #EC8482;\n"
"	padding: 10px;\n"
"	padding-left: 17px;\n"
"}\n"
"QLineEdit#nameSignUp:hover\n"
"{\n"
"\n"
"}")
        self.nameSignUp.setEchoMode(QLineEdit.Normal)
        self.SignUpBtn = QPushButton(self.RegisterForm)
        self.SignUpBtn.setObjectName(u"SignUpBtn")
        self.SignUpBtn.setGeometry(QRect(310, 490, 141, 41))
        self.SignUpBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.SignUpBtn.setStyleSheet(u"QPushButton#SignUpBtn\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 2px solid #EC8482;\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgba(0,0,0)\n"
"}\n"
"QPushButton#SignUpBtn:hover\n"
"{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgba(236, 132, 130, 255);\n"
"}")
        self.ResetBtn = QPushButton(self.RegisterForm)
        self.ResetBtn.setObjectName(u"ResetBtn")
        self.ResetBtn.setGeometry(QRect(70, 490, 141, 41))
        self.ResetBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ResetBtn.setStyleSheet(u"QPushButton#ResetBtn\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 2px solid #ff0000;\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgba(0,0,0)\n"
"}\n"
"QPushButton#ResetBtn:hover\n"
"{\n"
"	color: rgb(255,255,255);\n"
"	background-color: #ff0000;\n"
"}")
        self.repasswordSignUp = QLineEdit(self.RegisterForm)
        self.repasswordSignUp.setObjectName(u"repasswordSignUp")
        self.repasswordSignUp.setGeometry(QRect(190, 310, 281, 42))
        self.repasswordSignUp.setStyleSheet(u"QLineEdit#repasswordSignUp\n"
"{\n"
"	border-radius: 20px;\n"
"	border: 2px solid #EC8482;\n"
"	padding: 10px;\n"
"	padding-left: 17px;\n"
"}\n"
"QLineEdit#repasswordSignUp:hover\n"
"{\n"
"\n"
"}")
        self.repasswordSignUp.setEchoMode(QLineEdit.Normal)
        self.signUpLabel = QLabel(self.RegisterForm)
        self.signUpLabel.setObjectName(u"signUpLabel")
        self.signUpLabel.setGeometry(QRect(180, 20, 161, 51))
        self.signUpLabel.setFont(font17)
        self.signUpLabel.setStyleSheet(u"")
        self.signUpLabel.setAlignment(Qt.AlignCenter)
        self.nameSignUpLabel = QLabel(self.RegisterForm)
        self.nameSignUpLabel.setObjectName(u"nameSignUpLabel")
        self.nameSignUpLabel.setGeometry(QRect(20, 110, 161, 31))
        font19 = QFont()
        font19.setFamily(u"MS Shell Dlg 2")
        font19.setPointSize(12)
        font19.setBold(False)
        font19.setWeight(50)
        self.nameSignUpLabel.setFont(font19)
        self.nameSignUpLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.emailSignUpLabel = QLabel(self.RegisterForm)
        self.emailSignUpLabel.setObjectName(u"emailSignUpLabel")
        self.emailSignUpLabel.setGeometry(QRect(20, 180, 161, 31))
        self.emailSignUpLabel.setFont(font19)
        self.emailSignUpLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.passwordSignUpLabel = QLabel(self.RegisterForm)
        self.passwordSignUpLabel.setObjectName(u"passwordSignUpLabel")
        self.passwordSignUpLabel.setGeometry(QRect(20, 250, 161, 31))
        self.passwordSignUpLabel.setFont(font19)
        self.passwordSignUpLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.repasswordSignUpLabel = QLabel(self.RegisterForm)
        self.repasswordSignUpLabel.setObjectName(u"repasswordSignUpLabel")
        self.repasswordSignUpLabel.setGeometry(QRect(10, 320, 171, 31))
        self.repasswordSignUpLabel.setFont(font19)
        self.repasswordSignUpLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.headerLogin = QWidget(self.centralwidget)
        self.headerLogin.setObjectName(u"headerLogin")
        self.headerLogin.setGeometry(QRect(11, 11, 1101, 47))
        self.headerLogin.setStyleSheet(u"background-color: #2c313c;")
        self.headerLoginLabel = QLabel(self.headerLogin)
        self.headerLoginLabel.setObjectName(u"headerLoginLabel")
        self.headerLoginLabel.setGeometry(QRect(44, 15, 171, 21))
        font20 = QFont()
        font20.setFamily(u"Arial")
        font20.setPointSize(11)
        font20.setBold(True)
        font20.setWeight(75)
        self.headerLoginLabel.setFont(font20)
        self.appIconLogin = QLabel(self.headerLogin)
        self.appIconLogin.setObjectName(u"appIconLogin")
        self.appIconLogin.setGeometry(QRect(10, 10, 25, 25))
        self.appIconLogin.setMaximumSize(QSize(30, 30))
        self.appIconLogin.setStyleSheet(u"")
        self.appIconLogin.setPixmap(QPixmap(u":/icons/Assets/images/icons/icon.png"))
        self.appIconLogin.setScaledContents(True)
        self.appIconLogin.setAlignment(Qt.AlignCenter)
        self.hidExpand = QWidget(self.centralwidget)
        self.hidExpand.setObjectName(u"hidExpand")
        self.hidExpand.setGeometry(QRect(1168, 11, 41, 47))
        self.hidExpand.setStyleSheet(u"background-color: rgba(0,0,0, 50);")
        UserWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserWindow)

        self.centerMenuPages.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(0)
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
        self.homeBtn.setText(QCoreApplication.translate("UserWindow", u"  Trang ch\u1ee7", None))
#if QT_CONFIG(tooltip)
        self.libraryBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Library", None))
#endif // QT_CONFIG(tooltip)
        self.libraryBtn.setText(QCoreApplication.translate("UserWindow", u"  Kho game", None))
#if QT_CONFIG(tooltip)
        self.cartsBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Carts", None))
#endif // QT_CONFIG(tooltip)
        self.cartsBtn.setText(QCoreApplication.translate("UserWindow", u"  Gi\u1ecf h\u00e0ng", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Go to Setting", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("UserWindow", u"  C\u00e0i \u0111\u1eb7t", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Information for App", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("UserWindow", u"  Th\u00f4ng tin", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Any Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("UserWindow", u"  H\u1ed7 tr\u1ee3", None))
        self.titleCenterMenu.setText(QCoreApplication.translate("UserWindow", u"   Details", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.logOutBtn.setToolTip(QCoreApplication.translate("UserWindow", u"Go to Setting", None))
#endif // QT_CONFIG(tooltip)
        self.logOutBtn.setText(QCoreApplication.translate("UserWindow", u"   \u0110\u0103ng xu\u1ea5t", None))
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
        self.home_search_btn.setText(QCoreApplication.translate("UserWindow", u" Search", None))
        self.home_search_line.setText("")
        self.home_search_label.setText(QCoreApplication.translate("UserWindow", u"T\u00ecm ki\u1ebfm:", None))
        self.home_game_btn4.setText("")
        self.home_game_btn1.setText("")
        self.home_game_btn3.setText("")
        self.home_game_btn5.setText("")
        self.home_game_btn6.setText("")
        self.home_game_btn2.setText("")
        self.home_more_game_btn.setText("")
        self.library_search_btn.setText(QCoreApplication.translate("UserWindow", u" Search", None))
        self.library_search_line.setText("")
        self.library_search_label.setText(QCoreApplication.translate("UserWindow", u"T\u00ecm ki\u1ebfm:", None))
        self.library_game_btn4.setText("")
        self.library_game_btn2.setText("")
        self.library_game_btn6.setText("")
        self.library_game_btn1.setText("")
        self.library_game_btn3.setText("")
        self.library_game_btn5.setText("")
        self.library_more_game_btn.setText("")
        self.payMethodBox.setItemText(0, QCoreApplication.translate("UserWindow", u"Cash", None))
        self.payMethodBox.setItemText(1, QCoreApplication.translate("UserWindow", u"Credit card", None))
        self.payMethodBox.setItemText(2, QCoreApplication.translate("UserWindow", u"Visa", None))
        self.payMethodBox.setItemText(3, QCoreApplication.translate("UserWindow", u"Paypal", None))

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
        self.payBtn.setText(QCoreApplication.translate("UserWindow", u"Pay $", None))
        self.totalCost.setText(QCoreApplication.translate("UserWindow", u"0", None))
        self.idGameLabel.setText(QCoreApplication.translate("UserWindow", u"ID:", None))
        self.nameGameLabel.setText(QCoreApplication.translate("UserWindow", u"Name:", None))
        self.priceGameLabel.setText(QCoreApplication.translate("UserWindow", u"Price:", None))
        self.avtGame.setText("")
        self.vidGame.setText("")
        self.PlayBuyBtn.setText(QCoreApplication.translate("UserWindow", u" Play", None))
        self.descriptionGame.setText(QCoreApplication.translate("UserWindow", u"Descriptions", None))
        self.idGameText.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.nameGameText.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
        self.priceGameText.setText(QCoreApplication.translate("UserWindow", u"TextLabel", None))
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
        self.copyRightTitle.setText(QCoreApplication.translate("UserWindow", u"Copyright By Nhom 3", None))
        self.RegisterButton.setText(QCoreApplication.translate("UserWindow", u"Register", None))
        self.LoginButton.setText(QCoreApplication.translate("UserWindow", u"Login", None))
        self.PasswordInput.setText("")
        self.emailLoginLabel.setText(QCoreApplication.translate("UserWindow", u"Email", None))
        self.passwordLoginLabel.setText(QCoreApplication.translate("UserWindow", u"M\u1eadt kh\u1ea9u", None))
        self.signUpLabel_2.setText(QCoreApplication.translate("UserWindow", u"LOG IN", None))
        self.wrongUserInputLabel.setText(QCoreApplication.translate("UserWindow", u"SAI TH\u00d4NG TIN \u0110\u0102NG NH\u1eacP!", None))
        self.passwordSignUp.setInputMask("")
        self.passwordSignUp.setText("")
        self.emailSignUp.setInputMask("")
        self.nameSignUp.setInputMask("")
        self.nameSignUp.setText("")
        self.SignUpBtn.setText(QCoreApplication.translate("UserWindow", u"Sign Up", None))
        self.ResetBtn.setText(QCoreApplication.translate("UserWindow", u"Cancel", None))
        self.repasswordSignUp.setInputMask("")
        self.repasswordSignUp.setText("")
        self.signUpLabel.setText(QCoreApplication.translate("UserWindow", u"SIGN UP", None))
        self.nameSignUpLabel.setText(QCoreApplication.translate("UserWindow", u"H\u1ecd v\u00e0 t\u00ean", None))
        self.emailSignUpLabel.setText(QCoreApplication.translate("UserWindow", u"Email", None))
        self.passwordSignUpLabel.setText(QCoreApplication.translate("UserWindow", u"M\u1eadt kh\u1ea9u", None))
        self.repasswordSignUpLabel.setText(QCoreApplication.translate("UserWindow", u"Nh\u1eadp l\u1ea1i m\u1eadt kh\u1ea9u", None))
        self.headerLoginLabel.setText(QCoreApplication.translate("UserWindow", u"HOME MADE 2D...", None))
        self.appIconLogin.setText("")
    # retranslateUi


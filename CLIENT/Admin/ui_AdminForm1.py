# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminFormRyXhrY.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1072, 603)
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
        self.leftMenuContainer.setMinimumSize(QSize(0, 0))
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

        self.mainBar = QFrame(self.leftMenuSubContainer)
        self.mainBar.setObjectName(u"mainBar")
        self.mainBar.setStyleSheet(u"")
        self.mainBar.setFrameShape(QFrame.StyledPanel)
        self.mainBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.mainBar)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Nav_H_Spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.Nav_H_Spacer)

        self.usersBtn = QPushButton(self.mainBar)
        self.usersBtn.setObjectName(u"usersBtn")
        font1 = QFont()
        font1.setPointSize(10)
        self.usersBtn.setFont(font1)
        self.usersBtn.setAutoFillBackground(False)
        self.usersBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/EC8482/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.usersBtn.setIcon(icon1)
        self.usersBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.usersBtn)

        self.gamesBtn = QPushButton(self.mainBar)
        self.gamesBtn.setObjectName(u"gamesBtn")
        self.gamesBtn.setFont(font1)
        self.gamesBtn.setAutoFillBackground(False)
        self.gamesBtn.setStyleSheet(u"backgound-color: #1f232a;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/EC8482/zap.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.gamesBtn.setIcon(icon2)
        self.gamesBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.gamesBtn)

        self.transactionsBtn = QPushButton(self.mainBar)
        self.transactionsBtn.setObjectName(u"transactionsBtn")
        self.transactionsBtn.setFont(font1)
        self.transactionsBtn.setAutoFillBackground(False)
        self.transactionsBtn.setStyleSheet(u"backgound-color: #1f232a;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/EC8482/layers.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.transactionsBtn.setIcon(icon3)
        self.transactionsBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.transactionsBtn)

        self.paymentsBtn = QPushButton(self.mainBar)
        self.paymentsBtn.setObjectName(u"paymentsBtn")
        self.paymentsBtn.setFont(font1)
        self.paymentsBtn.setAutoFillBackground(False)
        self.paymentsBtn.setStyleSheet(u"backgound-color: #1f232a;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/EC8482/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.paymentsBtn.setIcon(icon4)
        self.paymentsBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.paymentsBtn)


        self.verticalLayout_2.addWidget(self.mainBar, 0, Qt.AlignTop)

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

        self.verticalLayout_2.addWidget(self.optionsBar, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer)

        self.centerMenuContainer = QWidget(self.centralwidget)
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/EC8482/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon5)
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
        sizePolicy.setHeightForWidth(self.appInfo.sizePolicy().hasHeightForWidth())
        self.appInfo.setSizePolicy(sizePolicy)
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
        self.appIcon.setPixmap(QPixmap(u":/icons/EC8482/airplay.svg"))
        self.appIcon.setScaledContents(True)
        self.appIcon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.appIcon)

        self.appTitle = QLabel(self.appInfo)
        self.appTitle.setObjectName(u"appTitle")
        sizePolicy.setHeightForWidth(self.appTitle.sizePolicy().hasHeightForWidth())
        self.appTitle.setSizePolicy(sizePolicy)
        self.appTitle.setFont(font2)
        self.appTitle.setScaledContents(False)
        self.appTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.appTitle)


        self.horizontalLayout_7.addWidget(self.appInfo)

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
        icon6 = QIcon()
        icon6.addFile(u":/icons/EC8482/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon6)
        self.minimizeBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.windowOptions)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/EC8482/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon7)
        self.restoreBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.windowOptions)
        self.closeBtn.setObjectName(u"closeBtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/EC8482/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon8)
        self.closeBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.closeBtn)


        self.horizontalLayout_7.addWidget(self.windowOptions)


        self.verticalLayout_8.addWidget(self.headerContainer)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy1)
        self.mainBodyContent.setMinimumSize(QSize(931, 518))
        self.mainBodyContent.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.mainContentsContainer.setMinimumSize(QSize(0, 0))
        self.mainContentsContainer.setMaximumSize(QSize(1000, 16777215))
        self.mainContentsContainer.setStyleSheet(u"")
        self.verticalLayout_19 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.mainPages = QCustomQStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.mainPages.setEnabled(True)
        self.mainPages.setMinimumSize(QSize(0, 0))
        self.mainPages.setStyleSheet(u"")
        self.usersPage = QWidget()
        self.usersPage.setObjectName(u"usersPage")
        self.usersPage.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.usersPage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.userContent = QWidget(self.usersPage)
        self.userContent.setObjectName(u"userContent")
        self.userContent.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.userContent)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.userBtns = QWidget(self.userContent)
        self.userBtns.setObjectName(u"userBtns")
        self.delUserBtn = QPushButton(self.userBtns)
        self.delUserBtn.setObjectName(u"delUserBtn")
        self.delUserBtn.setGeometry(QRect(760, 20, 151, 41))
        font4 = QFont()
        font4.setPointSize(11)
        self.delUserBtn.setFont(font4)
        self.delUserBtn.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid rgb(255,255,255);\n"
"background-color: rgb(255, 0, 0);")
        self.editUserBtn = QPushButton(self.userBtns)
        self.editUserBtn.setObjectName(u"editUserBtn")
        self.editUserBtn.setGeometry(QRect(600, 20, 151, 41))
        self.editUserBtn.setFont(font4)
        self.editUserBtn.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid rgb(255,255,255);\n"
"background-color: rgb(255, 255, 0);\n"
"color: #000\n"
"")
        self.addUserBtn = QPushButton(self.userBtns)
        self.addUserBtn.setObjectName(u"addUserBtn")
        self.addUserBtn.setGeometry(QRect(440, 20, 151, 41))
        self.addUserBtn.setFont(font4)
        self.addUserBtn.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid rgb(255,255,255);\n"
"background-color: rgb(0, 255, 0);\n"
"color: #000")
        self.userLabel = QLabel(self.userBtns)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setGeometry(QRect(10, 10, 161, 51))
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setWeight(75)
        self.userLabel.setFont(font5)

        self.verticalLayout_13.addWidget(self.userBtns)

        self.userView = QTableWidget(self.userContent)
        if (self.userView.columnCount() < 4):
            self.userView.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font2);
        self.userView.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font2);
        self.userView.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font2);
        self.userView.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font2);
        self.userView.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.userView.setObjectName(u"userView")
        self.userView.setEnabled(True)
        font6 = QFont()
        font6.setFamily(u"MS Shell Dlg 2")
        font6.setPointSize(11)
        self.userView.setFont(font6)
        self.userView.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 191, 64);")

        self.verticalLayout_13.addWidget(self.userView)

        self.verticalLayout_13.setStretch(0, 1)
        self.verticalLayout_13.setStretch(1, 5)

        self.verticalLayout_14.addWidget(self.userContent)

        self.mainPages.addWidget(self.usersPage)
        self.gamesPage = QWidget()
        self.gamesPage.setObjectName(u"gamesPage")
        self.verticalLayout_18 = QVBoxLayout(self.gamesPage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.gameContent = QWidget(self.gamesPage)
        self.gameContent.setObjectName(u"gameContent")
        self.gameContent.setStyleSheet(u"")
        self.verticalLayout_15 = QVBoxLayout(self.gameContent)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.gameBtns = QWidget(self.gameContent)
        self.gameBtns.setObjectName(u"gameBtns")
        self.delGameBtn = QPushButton(self.gameBtns)
        self.delGameBtn.setObjectName(u"delGameBtn")
        self.delGameBtn.setGeometry(QRect(760, 20, 151, 41))
        self.delGameBtn.setFont(font4)
        self.delGameBtn.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid rgb(255,255,255);\n"
"background-color: rgb(255, 0, 0);")
        self.editGameBtn = QPushButton(self.gameBtns)
        self.editGameBtn.setObjectName(u"editGameBtn")
        self.editGameBtn.setGeometry(QRect(600, 20, 151, 41))
        self.editGameBtn.setFont(font4)
        self.editGameBtn.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid rgb(255,255,255);\n"
"background-color: rgb(255, 255, 0);\n"
"color: #000\n"
"")
        self.addGameBtn = QPushButton(self.gameBtns)
        self.addGameBtn.setObjectName(u"addGameBtn")
        self.addGameBtn.setGeometry(QRect(440, 20, 151, 41))
        self.addGameBtn.setFont(font4)
        self.addGameBtn.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid rgb(255,255,255);\n"
"background-color: rgb(0, 255, 0);\n"
"color: #000")
        self.userLabel_2 = QLabel(self.gameBtns)
        self.userLabel_2.setObjectName(u"userLabel_2")
        self.userLabel_2.setGeometry(QRect(10, 10, 161, 51))
        self.userLabel_2.setFont(font5)

        self.verticalLayout_15.addWidget(self.gameBtns)

        self.gameView = QTableWidget(self.gameContent)
        if (self.gameView.columnCount() < 7):
            self.gameView.setColumnCount(7)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font2);
        self.gameView.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font2);
        self.gameView.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font2);
        self.gameView.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font2);
        self.gameView.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font2);
        self.gameView.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font2);
        self.gameView.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font2);
        self.gameView.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        self.gameView.setObjectName(u"gameView")
        self.gameView.setEnabled(True)
        self.gameView.setFont(font6)
        self.gameView.setStyleSheet(u"color: #000;\n"
"background-color: rgb(255, 133, 133);")

        self.verticalLayout_15.addWidget(self.gameView)

        self.verticalLayout_15.setStretch(0, 1)
        self.verticalLayout_15.setStretch(1, 5)

        self.verticalLayout_18.addWidget(self.gameContent)

        self.mainPages.addWidget(self.gamesPage)
        self.transactionsPage = QWidget()
        self.transactionsPage.setObjectName(u"transactionsPage")
        self.verticalLayout_20 = QVBoxLayout(self.transactionsPage)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.transactionContent = QWidget(self.transactionsPage)
        self.transactionContent.setObjectName(u"transactionContent")
        self.transactionContent.setStyleSheet(u"")
        self.verticalLayout_16 = QVBoxLayout(self.transactionContent)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.transactionBtns = QWidget(self.transactionContent)
        self.transactionBtns.setObjectName(u"transactionBtns")
        self.delTransactionBtn = QPushButton(self.transactionBtns)
        self.delTransactionBtn.setObjectName(u"delTransactionBtn")
        self.delTransactionBtn.setGeometry(QRect(760, 20, 151, 41))
        self.delTransactionBtn.setFont(font4)
        self.delTransactionBtn.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid rgb(255,255,255);\n"
"background-color: rgb(255, 0, 0);")
        self.userLabel_3 = QLabel(self.transactionBtns)
        self.userLabel_3.setObjectName(u"userLabel_3")
        self.userLabel_3.setGeometry(QRect(10, 10, 231, 51))
        self.userLabel_3.setFont(font5)

        self.verticalLayout_16.addWidget(self.transactionBtns)

        self.transactionView = QTableWidget(self.transactionContent)
        if (self.transactionView.columnCount() < 7):
            self.transactionView.setColumnCount(7)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font2);
        self.transactionView.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFont(font2);
        self.transactionView.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font2);
        self.transactionView.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font2);
        self.transactionView.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFont(font2);
        self.transactionView.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setFont(font2);
        self.transactionView.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem17.setFont(font2);
        self.transactionView.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        self.transactionView.setObjectName(u"transactionView")
        self.transactionView.setEnabled(False)
        self.transactionView.setFont(font6)
        self.transactionView.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 102, 255);")

        self.verticalLayout_16.addWidget(self.transactionView)

        self.verticalLayout_16.setStretch(0, 1)
        self.verticalLayout_16.setStretch(1, 5)

        self.verticalLayout_20.addWidget(self.transactionContent)

        self.mainPages.addWidget(self.transactionsPage)
        self.paymentsPage = QWidget()
        self.paymentsPage.setObjectName(u"paymentsPage")
        self.verticalLayout_21 = QVBoxLayout(self.paymentsPage)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.paymentContent = QWidget(self.paymentsPage)
        self.paymentContent.setObjectName(u"paymentContent")
        self.paymentContent.setStyleSheet(u"")
        self.verticalLayout_17 = QVBoxLayout(self.paymentContent)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.paymentBtns = QWidget(self.paymentContent)
        self.paymentBtns.setObjectName(u"paymentBtns")
        self.paymentBtns.setFont(font4)
        self.paymentBtns.setStyleSheet(u"")
        self.delPaymentBtn = QPushButton(self.paymentBtns)
        self.delPaymentBtn.setObjectName(u"delPaymentBtn")
        self.delPaymentBtn.setGeometry(QRect(760, 20, 151, 41))
        self.delPaymentBtn.setFont(font4)
        self.delPaymentBtn.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid rgb(255,255,255);\n"
"background-color: rgb(255, 0, 0);")
        self.userLabel_4 = QLabel(self.paymentBtns)
        self.userLabel_4.setObjectName(u"userLabel_4")
        self.userLabel_4.setGeometry(QRect(10, 10, 161, 51))
        self.userLabel_4.setFont(font5)

        self.verticalLayout_17.addWidget(self.paymentBtns)

        self.paymentView = QTableWidget(self.paymentContent)
        if (self.paymentView.columnCount() < 5):
            self.paymentView.setColumnCount(5)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFont(font2);
        self.paymentView.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setFont(font2);
        self.paymentView.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem20.setFont(font2);
        self.paymentView.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setFont(font2);
        self.paymentView.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFont(font2);
        self.paymentView.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        self.paymentView.setObjectName(u"paymentView")
        self.paymentView.setEnabled(False)
        self.paymentView.setFont(font6)
        self.paymentView.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 217, 0);")

        self.verticalLayout_17.addWidget(self.paymentView)

        self.verticalLayout_17.setStretch(0, 1)
        self.verticalLayout_17.setStretch(1, 5)

        self.verticalLayout_21.addWidget(self.paymentContent)

        self.mainPages.addWidget(self.paymentsPage)

        self.verticalLayout_19.addWidget(self.mainPages)


        self.horizontalLayout_10.addWidget(self.mainContentsContainer)


        self.verticalLayout_8.addWidget(self.mainBodyContent)

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

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 8)
        self.verticalLayout_8.setStretch(2, 1)

        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText(QCoreApplication.translate("MainWindow", u"  Main Menu", None))
#if QT_CONFIG(tooltip)
        self.usersBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Users", None))
#endif // QT_CONFIG(tooltip)
        self.usersBtn.setText(QCoreApplication.translate("MainWindow", u"   Users", None))
#if QT_CONFIG(tooltip)
        self.gamesBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Games", None))
#endif // QT_CONFIG(tooltip)
        self.gamesBtn.setText(QCoreApplication.translate("MainWindow", u"   Games", None))
#if QT_CONFIG(tooltip)
        self.transactionsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Transactions", None))
#endif // QT_CONFIG(tooltip)
        self.transactionsBtn.setText(QCoreApplication.translate("MainWindow", u"   Transactions", None))
#if QT_CONFIG(tooltip)
        self.paymentsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Payments", None))
#endif // QT_CONFIG(tooltip)
        self.paymentsBtn.setText(QCoreApplication.translate("MainWindow", u"   Payments", None))
        self.titleCenterMenu.setText(QCoreApplication.translate("MainWindow", u"   Details", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.settingsLabel.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.helpLabel.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.infoLabel.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.appIcon.setText("")
        self.appTitle.setText(QCoreApplication.translate("MainWindow", u"HomeMader-Admin", None))
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
        self.delUserBtn.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a", None))
        self.editUserBtn.setText(QCoreApplication.translate("MainWindow", u"S\u1eeda", None))
        self.addUserBtn.setText(QCoreApplication.translate("MainWindow", u"Th\u00eam", None))
        self.userLabel.setText(QCoreApplication.translate("MainWindow", u"USERS", None))
        ___qtablewidgetitem = self.userView.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.userView.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd t\u00ean", None));
        ___qtablewidgetitem2 = self.userView.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem3 = self.userView.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        self.delGameBtn.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a", None))
        self.editGameBtn.setText(QCoreApplication.translate("MainWindow", u"S\u1eeda", None))
        self.addGameBtn.setText(QCoreApplication.translate("MainWindow", u"Th\u00eam", None))
        self.userLabel_2.setText(QCoreApplication.translate("MainWindow", u"GAMES", None))
        ___qtablewidgetitem4 = self.gameView.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem5 = self.gameView.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"T\u00ean", None));
        ___qtablewidgetitem6 = self.gameView.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Th\u1ec3 lo\u1ea1i", None));
        ___qtablewidgetitem7 = self.gameView.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1", None));
        ___qtablewidgetitem8 = self.gameView.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u1ea2nh", None));
        ___qtablewidgetitem9 = self.gameView.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Video", None));
        ___qtablewidgetitem10 = self.gameView.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"M\u00f4 t\u1ea3", None));
        self.delTransactionBtn.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a", None))
        self.userLabel_3.setText(QCoreApplication.translate("MainWindow", u"TRANSACTIONS", None))
        ___qtablewidgetitem11 = self.transactionView.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem12 = self.transactionView.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 Ng\u01b0\u1eddi d\u00f9ng", None));
        ___qtablewidgetitem13 = self.transactionView.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 Game", None));
        ___qtablewidgetitem14 = self.transactionView.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Gi\u00e1 game", None));
        ___qtablewidgetitem15 = self.transactionView.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng th\u00e1i", None));
        ___qtablewidgetitem16 = self.transactionView.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y t\u1ea1o", None));
        ___qtablewidgetitem17 = self.transactionView.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y s\u1eeda \u0111\u1ed5i", None));
        self.delPaymentBtn.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a", None))
        self.userLabel_4.setText(QCoreApplication.translate("MainWindow", u"PAYMENTS", None))
        ___qtablewidgetitem18 = self.paymentView.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem19 = self.paymentView.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 giao d\u1ecbch", None));
        ___qtablewidgetitem20 = self.paymentView.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 ti\u1ec1n", None));
        ___qtablewidgetitem21 = self.paymentView.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Ph\u01b0\u01a1ng th\u1ee9c thanh to\u00e1n", None));
        ___qtablewidgetitem22 = self.paymentView.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 giao d\u1ecbch ph\u1ee5", None));
        self.copyRightTitle.setText(QCoreApplication.translate("MainWindow", u"Copyright By Nhom 3", None))
    # retranslateUi


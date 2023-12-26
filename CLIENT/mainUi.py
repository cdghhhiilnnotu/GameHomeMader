import os
import sys
from mainCLIENT import *
from Ui.ui_UserForm import *
from Models.Game import *
from PySide2.QtWidgets import QMainWindow, QApplication
from Custom_Widgets.Widgets import *

class MainWindowApp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        # self.client = CLIENT()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui)

        self.show()
        # self.init_Home_Page()
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.collapseMenu())

        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
     
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())

    def init_Home_Page(self):
        self.listGames = []
        self.listGamesBtn = [
            self.ui.game1,
            self.ui.game2,
            self.ui.game3,
            self.ui.game4,
            self.ui.game5,
            self.ui.game6,
            self.ui.game7,
            self.ui.game8,
            self.ui.game9,
            self.ui.game10,
            self.ui.game11,
            self.ui.game12
        ]
        gamesJson = self.client.getGame()
        # self.ui.listGamesBtn[0].clicked.connect(lambda: self.ui.mainPages.setCurrentWidget(self.ui.gameInfoPage))

        for item in gamesJson:
            # game1 = Game('daf', 'daf', 'dsafa', 34, 'sdf', 'adsf', 3.4, 'adf')
            self.listGames.append(gamesJson[item])
            # print(item)
        # print(self.client.getGame())
            
    def show_Game_Info(self, gameInfo):
        self.ui.descriptionGameLine = gameInfo["description"]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowApp()
    window.show()
    sys.exit(app.exec_())


import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mainCLIENT import *
from ui_UserForm3 import *
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2 import QtGui
from Custom_Widgets.Widgets import *

class MainWindowApp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.client = CLIENT()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui)
        self.show()
        # self.initHomePage()
        self.initListGames()

        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.collapseMenu())

        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
     
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())
        self.ui.searchBtn.clicked.connect(lambda: self.initListGames(str(self.ui.searchLine.text())))

    def initListGames(self, searchStr=''):
        self.listGames = []
        if searchStr == '':
            gamesJson = self.client.getGame()
            for item in gamesJson:
                self.listGames.append(gamesJson[item])
        else:
            gamesJson = self.client.getGameByStr(searchStr)
            for item in gamesJson:
                self.listGames.append(gamesJson[item])
        self.initHomePage()


    def initHomePage(self):
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
        for i in range(len(self.listGamesBtn)):
            self.initGameBtn(i, i)
        if len(self.listGames) <= 12:
            self.ui.moreGameBtn.hide()

    def initGameBtn(self, thisIndex, gameIdx):
        if thisIndex >= len(self.listGames):
            self.listGamesBtn[thisIndex].hide()
        else:
            self.listGamesBtn[thisIndex].show()
            iconBtn = QtGui.QPixmap(self.client.get_game_image_path(self.listGames[gameIdx]["images"]))
            self.listGamesBtn[thisIndex].setIcon(QtGui.QIcon(iconBtn))
        self.listGamesBtn[thisIndex].clicked.connect(lambda: self.show_Game_Info(gameIdx))
        
    def show_Game_Info(self, idx):
        if idx < len(self.listGames):
            self.ui.mainPages.setCurrentWidget(self.ui.gameInfoPage)
            self.ui.descriptionGame.setText(self.listGames[idx]["description"])
            self.ui.idGame.setText(str(self.listGames[idx]["id"]))
            self.ui.nameGame.setText(self.listGames[idx]["name"])
            self.ui.priceGame.setText(str(self.listGames[idx]["price"]))
            pixmap = QtGui.QPixmap(self.client.get_game_image_path(self.listGames[idx]["images"]))
            self.ui.avtGame.setPixmap(pixmap)
        # print(gameInfo[0])
        # print(idx)
        # print("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowApp()
    window.show()
    sys.exit(app.exec_())


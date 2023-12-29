import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mainCLIENT import *
from ui_UserForm7 import *
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2 import QtGui
from Custom_Widgets.Widgets import *

class MainUserApp(QMainWindow):
    def __init__(self, username, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.client = CLIENT(username)
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui)
        self.show()
        # self.initHomePage()
        self.initListGames()
        self.initLibrary()
        self.initUserProfile()

        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.collapseMenu())

        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
     
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())
        self.ui.searchBtn.clicked.connect(lambda: self.initListGames(str(self.ui.searchLine.text())))
        self.ui.searchLibraryBtn.clicked.connect(lambda: self.initLibrary(str(self.ui.searchLibraryLine.text())))

        self.ui.doneBtn.clicked.connect(self.updateUser)
        self.ui.cancelBtn.clicked.connect(self.resetUser)
        self.initCartPage()

    def initDeleteBtn(self):
        pass

    def initCartPage(self):
        self.listCart = []
        trasctionsJson = self.client.getTransaction()
        print(trasctionsJson)


    def resetUser(self):
        userJson = self.client.user.toJson()
        self.ui.idLine.setText(str(userJson['id']))
        self.ui.nameLine.setText(userJson['name'])
        self.ui.emailLine.setText(userJson['email'])
        self.ui.passLine.setText(userJson['password'])

    def updateUser(self):
        userJson = self.client.user.toJson()
        userJson['name'] = self.ui.nameLine.text()
        userJson['email'] = self.ui.emailLine.text()
        userJson['password'] = self.ui.passLine.text()
        self.client.putUser(int(userJson['id']), userJson)

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

    def initLibrary(self, searchStr=''):
        self.listLibrary = []
        if searchStr == '':
            gamesJson = self.client.getLibrary()
            for item in gamesJson:
                self.listLibrary.append(item)
        else:
            gamesJson = self.client.getLibraryByStr(searchStr)
            for item in gamesJson:
                self.listLibrary.append(item)
        self.initLibraryPage()

    def initUserProfile(self):
        userJson = self.client.user.toJson()
        self.ui.idLine.setText(str(userJson['id']))
        self.ui.nameLine.setText(userJson['name'])
        self.ui.emailLine.setText(userJson['email'])
        self.ui.passLine.setText(userJson['password'])

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

    def initLibraryPage(self):
        self.listLibraryBtn = [
            self.ui.game1_2,
            self.ui.game2_2,
            self.ui.game3_2,
            self.ui.game4_2,
            self.ui.game5_2,
            self.ui.game6_2,
            self.ui.game7_2,
            self.ui.game8_2,
            self.ui.game9_2,
            self.ui.game10_2,
            self.ui.game11_2,
            self.ui.game12_2
        ]
        for i in range(len(self.listGamesBtn)):
            self.initLibraryBtn(i)
        if len(self.listGames) <= 12:
            self.ui.moreGameLibraryBtn.hide()

    def initLibraryBtn(self, idxBtn):
        if idxBtn >= len(self.listLibrary):
            self.listLibraryBtn[idxBtn].hide()
        else:
            self.listLibraryBtn[idxBtn].show()
            iconBtn = QtGui.QPixmap(self.client.get_game_image_path(self.listLibrary[idxBtn]["images"]))
            self.listLibraryBtn[idxBtn].setIcon(QtGui.QIcon(iconBtn))
        self.listLibraryBtn[idxBtn].clicked.connect(lambda: self.show_Game_Info(self.listLibrary[idxBtn]))

    def initGameBtn(self, thisIndex, gameIdx):
        if thisIndex >= len(self.listGames):
            self.listGamesBtn[thisIndex].hide()
        else:
            self.listGamesBtn[thisIndex].show()
            iconBtn = QtGui.QPixmap(self.client.get_game_image_path(self.listGames[gameIdx]["images"]))
            self.listGamesBtn[thisIndex].setIcon(QtGui.QIcon(iconBtn))
        self.listGamesBtn[thisIndex].clicked.connect(lambda: self.show_Game_Info(self.listGames[gameIdx]))
        
    def show_Game_Info(self, thisGame):
        self.ui.mainPages.setCurrentWidget(self.ui.gameInfoPage)
        self.ui.descriptionGame.setText(thisGame["description"])
        self.ui.idGame.setText(str(thisGame["id"]))
        self.ui.nameGame.setText(thisGame["name"])
        self.ui.priceGame.setText(str(thisGame["price"]))
        pixmap = QtGui.QPixmap(self.client.get_game_image_path(thisGame["images"]))
        self.ui.avtGame.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUserApp(2)
    window.show()
    sys.exit(app.exec_())


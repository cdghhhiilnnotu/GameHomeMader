import os
import sys
from datetime import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mainCLIENT import *
from ui_UserForm7 import *
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2 import QtGui
from Custom_Widgets.Widgets import *

class MainUserApp(QMainWindow):
    def __init__(self, user_email, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.client = CLIENT(user_email)
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui)
        self.show()

        self.init_default_btns()

        self.initHomeGames()
        self.initLibraryGames()
        self.initCartsGames()
        self.initUserProfile()

        # self.initHomePage()
        # self.initHomeGames()
        # self.initLibrary()
        # self.initUserProfile()

        # self.ui.searchLibraryBtn.clicked.connect(lambda: self.initLibrary(str(self.ui.searchLibraryLine.text())))
        # self.initCartPage()

    def init_default_btns(self):
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.collapseMenu())

        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
     
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())
        self.ui.libraryBtn.clicked.connect(self.initLibraryGames())
        self.ui.homeBtn.clicked.connect(self.initHomeGames())
        self.ui.cartsBtn.clicked.connect(self.initCartsGames())


    def initHomeGames(self, searchStr=''):
        self.client.resetApi()
        if searchStr == '':
            self.listHomeGames = self.client.get_home_games()
        else:
            self.listHomeGames = self.client.get_home_games_by_search(searchStr)
        self.listHomeGamesBtn = [
            self.ui.home_game_btn1,
            self.ui.home_game_btn2,
            self.ui.home_game_btn3,
            self.ui.home_game_btn4,
            self.ui.home_game_btn5,
            self.ui.home_game_btn6,
            self.ui.home_game_btn7,
            self.ui.home_game_btn8,
            self.ui.home_game_btn9,
            self.ui.home_game_btn10,
            self.ui.home_game_btn11,
            self.ui.home_game_btn12
        ]
        for i in range(len(self.listHomeGamesBtn)):
            self.initHomeGameBtns(i)
        if len(self.listHomeGames) <= 12:
            self.ui.home_more_game_btn.hide()
        self.ui.home_search_btn.clicked.connect(lambda: self.initHomeGames(str(self.ui.home_search_line.text())))

    def initHomeGameBtns(self, thisIndex):
        if thisIndex >= len(self.listHomeGames):
            self.listHomeGamesBtn[thisIndex].hide()
        else:
            self.listHomeGamesBtn[thisIndex].show()
            # iconBtn = QtGui.QPixmap(self.client.get_game_image_path(self.listHomeGames[thisIndex]["images"]))
            # self.listHomeGamesBtn[thisIndex].setIcon(QtGui.QIcon(iconBtn))
        self.listHomeGamesBtn[thisIndex].clicked.connect(lambda: self.show_Game_Info(self.listHomeGames[thisIndex], mode='Buy'))


    def initLibraryGames(self, searchStr=''):
        self.client.resetApi()
        if searchStr == '':
            self.listLibraryGames = self.client.get_library_games()
        else:
            self.listLibraryGames = self.client.get_library_games_by_search(searchStr)
        self.listLibraryGamesBtn = [
            self.ui.library_game_btn1,
            self.ui.library_game_btn2,
            self.ui.library_game_btn3,
            self.ui.library_game_btn4,
            self.ui.library_game_btn5,
            self.ui.library_game_btn6,
            self.ui.library_game_btn7,
            self.ui.library_game_btn8,
            self.ui.library_game_btn9,
            self.ui.library_game_btn10,
            self.ui.library_game_btn11,
            self.ui.library_game_btn12
        ]
        for i in range(len(self.listLibraryGamesBtn)):
            self.initLibraryGameBtns(i)
        if len(self.listLibraryGames) <= 12:
            self.ui.library_more_game_btn.hide()
        self.ui.library_search_btn.clicked.connect(lambda: self.initLibraryGames(str(self.ui.library_search_line.text())))

    def initLibraryGameBtns(self, thisIndex):
        if thisIndex >= len(self.listLibraryGames):
            self.listLibraryGamesBtn[thisIndex].hide()
        else:
            self.listLibraryGamesBtn[thisIndex].show()
            # iconBtn = QtGui.QPixmap(self.client.get_game_image_path(self.listLibraryGames[thisIndex]["images"]))
            # self.listLibraryGamesBtn[thisIndex].setIcon(QtGui.QIcon(iconBtn))
        self.listLibraryGamesBtn[thisIndex].clicked.connect(lambda: self.show_Game_Info(self.listLibraryGames[thisIndex], mode='Play'))


    def initCartsGames(self):
        self.client.resetApi()

        self.listCartsGames = self.client.get_cart_games()
        self.listCartsGameBoxes = [
            self.ui.gameOrderBox_1,
            self.ui.gameOrderBox_2,
            self.ui.gameOrderBox_3,
            self.ui.gameOrderBox_4,
            self.ui.gameOrderBox_5,
            self.ui.gameOrderBox_6,
            self.ui.gameOrderBox_7,
            self.ui.gameOrderBox_8,
            self.ui.gameOrderBox_9
        ]
        self.listCartsAvtGameBoxes = [
            self.ui.avtGameOrder_1,
            self.ui.avtGameOrder_2,
            self.ui.avtGameOrder_3,
            self.ui.avtGameOrder_4,
            self.ui.avtGameOrder_5,
            self.ui.avtGameOrder_6,
            self.ui.avtGameOrder_7,
            self.ui.avtGameOrder_8,
            self.ui.avtGameOrder_9
        ]
        self.listCartsNameGameBoxes = [
            self.ui.nameGameOrder_1,
            self.ui.nameGameOrder_2,
            self.ui.nameGameOrder_3,
            self.ui.nameGameOrder_4,
            self.ui.nameGameOrder_5,
            self.ui.nameGameOrder_6,
            self.ui.nameGameOrder_7,
            self.ui.nameGameOrder_8,
            self.ui.nameGameOrder_9
        ]
        self.listCartsDeleteGameBoxes = [
            self.ui.deleteOrder_1,
            self.ui.deleteOrder_2,
            self.ui.deleteOrder_3,
            self.ui.deleteOrder_4,
            self.ui.deleteOrder_5,
            self.ui.deleteOrder_6,
            self.ui.deleteOrder_7,
            self.ui.deleteOrder_8,
            self.ui.deleteOrder_9
        ]

        for i in range(len(self.listCartsGameBoxes)):
            self.initCartsGameBoxes(i)
        
        self.ui.payBtn.clicked.connect(self.payingGame)
        

    def initCartsGameBoxes(self, index):
        self.ui.totalCost.setText(str(self.client.totalCost))
        if index >= len(self.listCartsGames):
            self.listCartsGameBoxes[index].hide()
        else:
            self.listCartsGameBoxes[index].show()
            self.listCartsNameGameBoxes[index].setText(self.listCartsGames[index]['name'])
            self.listCartsDeleteGameBoxes[index].clicked.connect(lambda: self.removeCartsGameBox(index))
            
    def removeCartsGameBox(self, index):
        self.client.deleteTransaction(self.listCartsGames[index]['id'])
        self.initCartsGames()
        # self.listCartsGameBoxes[index].hide()
        # pass

    def payingGame(self):
        id_transacs = self.client.get_pending_id()
        amount_transacs = self.client.get_pending_amount()
        for idx in range(len(id_transacs)):
            new_payment = Payment(amount_transacs[idx], Payment.payment_number+1, self.ui.payMethodBox.currentText(),id_transacs[idx], Payment.payment_number+1)
            self.client.postPayment(new_payment.toJson())
        self.initCartsGames()
        # pass  

    def initUserProfile(self):
        userJson = self.client.user
        self.ui.idLine.setText(str(userJson['id']))
        self.ui.nameLine.setText(userJson['name'])
        self.ui.emailLine.setText(userJson['email'])
        self.ui.passLine.setText(userJson['password'])
        self.ui.doneBtn.clicked.connect(self.updateUser)
        self.ui.cancelBtn.clicked.connect(self.resetUser)

    def resetUser(self):
        userJson = self.client.user
        self.ui.idLine.setText(str(userJson['id']))
        self.ui.nameLine.setText(userJson['name'])
        self.ui.emailLine.setText(userJson['email'])
        self.ui.passLine.setText(userJson['password'])

    def updateUser(self):
        userJson = self.client.user
        userJson['name'] = self.ui.nameLine.text()
        userJson['email'] = self.ui.emailLine.text()
        userJson['password'] = self.ui.passLine.text()
        self.client.putUser(int(userJson['id']), userJson)


    def buyPlayEvent(self, game, mode):
        if mode == 'Buy':
            print(mode)
            new_transaction = Transaction(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), game['id'], Transaction.transaction_number+1,game['price'],'pending', datetime.now().strftime("%Y-%m-%d %H:%M:%S"),self.client.user_id)
            print(new_transaction.toJson())
            self.client.post_transaction(new_transaction.toJson())
        self.ui.mainPages.setCurrentWidget(self.ui.homePage)
        


    # def initDeleteBtn(self):
    #     pass

    # def initCartPage(self):
    #     self.listCart = []
    #     trasctionsJson = self.client.getTransaction()
    #     print(trasctionsJson)




    # def initLibrary(self, searchStr=''):
    #     self.listLibrary = []
    #     if searchStr == '':
    #         gamesJson = self.client.getLibrary()
    #         for item in gamesJson:
    #             self.listLibrary.append(item)
    #     else:
    #         gamesJson = self.client.getLibraryByStr(searchStr)
    #         for item in gamesJson:
    #             self.listLibrary.append(item)
    #     self.initLibraryPage()



    # def initLibraryPage(self):
    #     self.listLibraryBtn = [
    #         self.ui.game1_2,
    #         self.ui.game2_2,
    #         self.ui.game3_2,
    #         self.ui.game4_2,
    #         self.ui.game5_2,
    #         self.ui.game6_2,
    #         self.ui.game7_2,
    #         self.ui.game8_2,
    #         self.ui.game9_2,
    #         self.ui.game10_2,
    #         self.ui.game11_2,
    #         self.ui.game12_2
    #     ]
    #     for i in range(len(self.listGamesBtn)):
    #         self.initLibraryBtn(i)
    #     if len(self.listGames) <= 12:
    #         self.ui.moreGameLibraryBtn.hide()

    # def initLibraryBtn(self, idxBtn):
        # if idxBtn >= len(self.listLibrary):
        #     self.listLibraryBtn[idxBtn].hide()
        # else:
        #     self.listLibraryBtn[idxBtn].show()
        #     iconBtn = QtGui.QPixmap(self.client.get_game_image_path(self.listLibrary[idxBtn]["images"]))
        #     self.listLibraryBtn[idxBtn].setIcon(QtGui.QIcon(iconBtn))
        # self.listLibraryBtn[idxBtn].clicked.connect(lambda: self.show_Game_Info(self.listLibrary[idxBtn]))
        
    def show_Game_Info(self, thisGame, mode):
        self.ui.mainPages.setCurrentWidget(self.ui.gameInfoPage)
        self.ui.descriptionGame.setText(thisGame["description"])
        self.ui.idGame.setText(str(thisGame["id"]))
        self.ui.nameGame.setText(thisGame["name"])
        self.ui.priceGame.setText(str(thisGame["price"]))
        self.ui.PlayBuyBtn.setText(mode)
        self.ui.PlayBuyBtn.clicked.connect(lambda: self.buyPlayEvent(thisGame, mode))
        # pixmap = QtGui.QPixmap(self.client.get_game_image_path(thisGame["images"]))
        # self.ui.avtGame.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUserApp('tranthibb@exmaple.com')
    window.show()
    sys.exit(app.exec_())


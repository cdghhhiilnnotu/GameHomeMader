import os
import sys
from datetime import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mainCLIENT import *
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2 import QtGui
from ui_UserForm12 import *
from Custom_Widgets.Widgets import *
import urllib


class MainUserApp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_UserWindow()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui)
        self.initLoginForm()
        
    def loginUser(self, user_email, password):
        try:
            self.ui.wrongUserInputLabel.hide()
            self.client = CLIENT(user_email)
            if self.client.user['password'] == password:
                self.init_default_btns()
                print("In")
                self.initHomePage()
                self.initLibraryPage()
                self.initCartsPage()
                self.initUserProfile()
                self.ui.headerLogin.hide()
                self.ui.mainLogin.hide()
                self.ui.hidExpand.hide()
        except:
            self.ui.wrongUserInputLabel.show()

    def initLoginForm(self):
        self.ui.wrongUserInputLabel.hide()
        self.ui.LoginButton.clicked.connect(lambda: self.loginUser(self.ui.UsernameInput.text(), self.ui.PasswordInput.text()))
        self.ui.RegisterButton.clicked.connect(lambda: self.ui.RegisterForm.show())
        self.ui.ResetBtn.clicked.connect(self.resetRegister)
        self.ui.SignUpBtn.clicked.connect(self.signUpSummit)
        self.ui.RegisterForm.hide()

    def init_default_btns(self):
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.collapseMenu())

        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
     
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())
        self.ui.homeBtn.clicked.connect(self.initHomePage())
        self.ui.libraryBtn.clicked.connect(self.initLibraryPage())
        self.ui.cartsBtn.clicked.connect(self.initCartsPage())

    def resetRegister(self):
        self.ui.nameSignUp.setText('')
        self.ui.emailSignUp.setText('')
        self.ui.passwordSignUp.setText('')
        self.ui.repasswordSignUp.setText('')
        self.ui.RegisterForm.hide()
    
    def signUpSummit(self):
        if (self.ui.passwordSignUp.text() == self.ui.repasswordSignUp.text() 
            and self.ui.passwordSignUp.text() != '' and self.ui.nameSignUp.text() != '' 
            and self.ui.repasswordSignUp.text() != '' and self.ui.emailSignUp.text() != ''):
            new_user = User(User.usernumber+1, self.ui.nameSignUp.text(), self.ui.repasswordSignUp.text(), self.ui.emailSignUp.text())
            CLIENT.postUser(new_user.toJson())
            self.ui.RegisterForm.hide() 
            self.client.reset_api()      


    def initHomePage(self, searchStr=''):
        if searchStr == '':
            self.listHomeGames = self.client.get_list_games_home()
        else:
            self.listHomeGames = self.client.get_list_games_home_by_search(searchStr)
        self.listHomeGamesBtn = [
            self.ui.home_game_btn1,
            self.ui.home_game_btn2,
            self.ui.home_game_btn3,
            self.ui.home_game_btn4,
            self.ui.home_game_btn5,
            self.ui.home_game_btn6
        ]
        for i in range(len(self.listHomeGamesBtn)):
            self.initHomeGameBtns(i)
        if len(self.listHomeGames) <= 6:
            self.ui.home_more_game_btn.hide()
        self.ui.home_search_btn.clicked.connect(lambda: self.initHomePage(str(self.ui.home_search_line.text())))

    def initHomeGameBtns(self, thisIndex):
        if thisIndex >= len(self.listHomeGames):
            pixmapBtn = QtGui.QPixmap('Assets\images\games\empty.png')
            self.listHomeGamesBtn[thisIndex].setIcon(pixmapBtn)
            self.listHomeGamesBtn[thisIndex].setIconSize(QSize(320,165))
        else:
            pixmapBtn = QtGui.QPixmap(self.client.get_game_image_by_id(self.listHomeGames[thisIndex]['id']))
            self.listHomeGamesBtn[thisIndex].setIcon(pixmapBtn)
            self.listHomeGamesBtn[thisIndex].setIconSize(QSize(320,165))
        self.listHomeGamesBtn[thisIndex].clicked.connect(lambda: self.show_Game_Info(self.listHomeGames[thisIndex], mode='Buy'))


    def initLibraryPage(self, searchStr=''):
        if searchStr == '':
            self.listLibraryGames = self.client.get_list_games_library()
        else:
            self.listLibraryGames = self.client.get_list_games_library_by_search(searchStr)
        self.listLibraryGamesBtn = [
            self.ui.library_game_btn1,
            self.ui.library_game_btn2,
            self.ui.library_game_btn3,
            self.ui.library_game_btn4,
            self.ui.library_game_btn5,
            self.ui.library_game_btn6
        ]
        for i in range(len(self.listLibraryGamesBtn)):
            self.initLibraryGameBtns(i)
        if len(self.listLibraryGames) <= 6:
            self.ui.library_more_game_btn.hide()
        self.ui.library_search_btn.clicked.connect(lambda: self.initLibraryPage(str(self.ui.library_search_line.text())))

    def initLibraryGameBtns(self, thisIndex):
        if thisIndex >= len(self.listLibraryGames):
            pixmapBtn = QtGui.QPixmap('Assets\images\games\empty.png')
            self.listLibraryGamesBtn[thisIndex].setIcon(pixmapBtn)
            self.listLibraryGamesBtn[thisIndex].setIconSize(QSize(320,165))
        else:
            pixmapBtn = QtGui.QPixmap(self.client.get_game_image_by_id(self.listLibraryGames[thisIndex]['id']))
            self.listLibraryGamesBtn[thisIndex].setIcon(pixmapBtn)
            self.listLibraryGamesBtn[thisIndex].setIconSize(QSize(320,165))
        self.listLibraryGamesBtn[thisIndex].clicked.connect(lambda: self.show_Game_Info(self.listLibraryGames[thisIndex], mode='Play'))


    def initCartsPage(self):
        self.listCartsGames, self.totalPrice = self.client.get_list_games_carts()
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
        self.ui.totalCost.setText(str(self.totalPrice))
        if index >= len(self.listCartsGames):
            self.listCartsGameBoxes[index].hide()
            self.listCartsDeleteGameBoxes[index].clicked.connect(lambda: print("Hello"))
        else:
            self.listCartsGameBoxes[index].show()
            self.listCartsNameGameBoxes[index].setText(self.listCartsGames[index]['name'])
            icon = QtGui.QPixmap(self.client.get_game_image_by_id(self.listCartsGames[index]['id']))
            self.listCartsAvtGameBoxes[index].setPixmap(QtGui.QPixmap(icon))
            self.listCartsDeleteGameBoxes[index].clicked.connect(lambda: self.removeCartsGameBox(self.listCartsGames[index]['id']))

    # def initDeleteCartBtn(self, index):
        
            
    def removeCartsGameBox(self, id):
        self.client.deleteTransaction(id)
        self.client.reset_api()
        self.initCartsPage()
        # for i in range(len(self.listCartsGameBoxes)):
        #     self.initCartsGameBoxes(i)
        # pass

    def payingGame(self):
        id_transacs = self.client.get_pending_id()
        amount_transacs = self.client.get_pending_amount()
        for idx in range(len(id_transacs)):
            new_payment = Payment(amount_transacs[idx], Payment.payment_number+1, self.ui.payMethodBox.currentText(),id_transacs[idx], Payment.payment_number+1)
            self.client.postPayment(new_payment.toJson())
        self.client.reset_api()
        self.initCartsPage()
        self.initHomePage()
        self.initLibraryPage()
        

    def initUserProfile(self):
        userJson = self.client.user
        self.ui.idLine.setText(str(userJson['id']))
        self.ui.nameLine.setText(userJson['name'])
        self.ui.emailLine.setText(userJson['email'])
        self.ui.passLine.setText(userJson['password'])
        self.ui.doneBtn.clicked.connect(self.updateUser)
        self.ui.cancelBtn.clicked.connect(self.resetUser)
        avtImg = QtGui.QPixmap('Assets\\images\\users\\avt-user.jpg')
        self.ui.AvatarLabel.setPixmap(avtImg)

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
        self.client.reset_api()

    def buyPlayEvent(self, game, mode):
        print(game)
        if mode == 'Buy':
            new_transaction = Transaction(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), game['id'], Transaction.transaction_number+1,game['price'],'pending', datetime.now().strftime("%Y-%m-%d %H:%M:%S"),self.client.user['id'])
            self.client.post_transaction(new_transaction.toJson())
            self.client.reset_api()
            self.initCartsPage()
        self.ui.mainPages.setCurrentWidget(self.ui.homePage)
 
    def show_Game_Info(self, thisGame, mode):
        self.ui.mainPages.setCurrentWidget(self.ui.gameInfoPage)
        self.ui.descriptionGame.setText(thisGame["description"])
        self.ui.idGameText.setText(str(thisGame["id"]))
        self.ui.nameGameText.setText(thisGame["name"])
        self.ui.priceGameText.setText(str(thisGame["price"]))
        self.ui.PlayBuyBtn.setText(mode)
        pixmap = QtGui.QPixmap(self.client.get_game_image_by_id(thisGame['id']))
        self.ui.avtGame.setPixmap(pixmap)
        self.ui.PlayBuyBtn.clicked.connect(lambda: self.buyPlayEvent(thisGame, mode))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUserApp()
    window.show()
    sys.exit(app.exec_())


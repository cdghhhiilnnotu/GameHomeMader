import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mainCLIENT import *
from ui_AdminForm import *
from PySide2.QtWidgets import QMainWindow, QApplication
from Custom_Widgets.Widgets import *

class MainWindowApp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.getAPI()
        loadJsonStyle(self, self.ui)

        self.show()
        self.init_default_buttons()
        self.init_userTable()
        self.init_gameTable()
        self.init_transactionTable()
        self.init_paymentTable()

    def getAPI(self):
        CLIENT.getAPI()
        self.clientAdmin = CLIENT.readAPI()


    def init_default_buttons(self):
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.collapseMenu())

        self.ui.addUserBtn.clicked.connect(lambda: self.popAddUser())
        self.ui.editUserBtn.clicked.connect(lambda: self.popAddUser(self.ui.userView.currentRow()))
        self.ui.addGameBtn.clicked.connect(lambda: self.popAddGame())
        self.ui.editGameBtn.clicked.connect(lambda: self.popAddGame(self.ui.gameView.currentRow()))
     
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

        self.ui.delPaymentBtn.clicked.connect(self.deletePayment)
        self.ui.delUserBtn.clicked.connect(self.deleteUser)
        self.ui.delTransactionBtn.clicked.connect(self.deleteTransaction)
        self.ui.delGameBtn.clicked.connect(self.deleteGame)
    
    def init_userTable(self):
        self.ui.userView.setColumnWidth(0, 50)
        self.ui.userView.setColumnWidth(1, 400)
        self.ui.userView.setColumnWidth(2, 300)
        self.ui.userView.setColumnWidth(3, 200)
        self.load_userdata()
    
    def load_userdata(self):
        row = 0
        users = self.clientAdmin['users']
        self.ui.userView.setRowCount(len(users))
        for user in users:
            self.ui.userView.setItem(row, 0, PySide2.QtWidgets.QTableWidgetItem(str(user['id'])))
            self.ui.userView.setItem(row, 1, PySide2.QtWidgets.QTableWidgetItem(user['name']))
            self.ui.userView.setItem(row, 2, PySide2.QtWidgets.QTableWidgetItem(user['email']))
            self.ui.userView.setItem(row, 3, PySide2.QtWidgets.QTableWidgetItem(user['password']))
            row+=1

    def init_gameTable(self):
        self.ui.gameView.setColumnWidth(0, 50)
        self.ui.gameView.setColumnWidth(1, 300)
        self.ui.gameView.setColumnWidth(2, 100)
        self.ui.gameView.setColumnWidth(3, 100)
        self.ui.gameView.setColumnWidth(4, 150)
        self.ui.gameView.setColumnWidth(5, 150)
        self.ui.gameView.setColumnWidth(6, 200)
        self.ui.gameView.setColumnWidth(6, 400)
        self.load_gamedata()
    
    def load_gamedata(self):
        row = 0
        games = self.clientAdmin['games']
        self.ui.gameView.setRowCount(len(games))
        for game in games:
            self.ui.gameView.setItem(row, 0, PySide2.QtWidgets.QTableWidgetItem(str(game['id'])))
            self.ui.gameView.setItem(row, 1, PySide2.QtWidgets.QTableWidgetItem(game['name']))
            self.ui.gameView.setItem(row, 2, PySide2.QtWidgets.QTableWidgetItem(game['genre']))
            self.ui.gameView.setItem(row, 3, PySide2.QtWidgets.QTableWidgetItem(str(game['price'])))
            self.ui.gameView.setItem(row, 4, PySide2.QtWidgets.QTableWidgetItem(game['images']))
            self.ui.gameView.setItem(row, 5, PySide2.QtWidgets.QTableWidgetItem(game['videos']))
            self.ui.gameView.setItem(row, 6, PySide2.QtWidgets.QTableWidgetItem(game['demo_file']))
            self.ui.gameView.setItem(row, 7, PySide2.QtWidgets.QTableWidgetItem(game['description']))
            row+=1

    def init_transactionTable(self):
        self.ui.transactionView.setColumnWidth(0, 50)
        self.ui.transactionView.setColumnWidth(1, 150)
        self.ui.transactionView.setColumnWidth(2, 150)
        self.ui.transactionView.setColumnWidth(3, 150)
        self.ui.transactionView.setColumnWidth(4, 200)
        self.ui.transactionView.setColumnWidth(5, 200)
        self.ui.transactionView.setColumnWidth(6, 200)
        self.load_transactiondata()
    
    def load_transactiondata(self):
        row = 0
        transactions = self.clientAdmin['transactions']
        self.ui.transactionView.setRowCount(len(transactions))
        for transaction in transactions:
            self.ui.transactionView.setItem(row, 0, PySide2.QtWidgets.QTableWidgetItem(str(transaction['id'])))
            self.ui.transactionView.setItem(row, 1, PySide2.QtWidgets.QTableWidgetItem(str(transaction['user_id'])))
            self.ui.transactionView.setItem(row, 2, PySide2.QtWidgets.QTableWidgetItem(str(transaction['game_id'])))
            self.ui.transactionView.setItem(row, 3, PySide2.QtWidgets.QTableWidgetItem(str(transaction['price'])))
            self.ui.transactionView.setItem(row, 4, PySide2.QtWidgets.QTableWidgetItem(transaction['status']))
            self.ui.transactionView.setItem(row, 5, PySide2.QtWidgets.QTableWidgetItem(transaction['created_at']))
            self.ui.transactionView.setItem(row, 6, PySide2.QtWidgets.QTableWidgetItem(transaction['updated_at']))
            row+=1

    def init_paymentTable(self):
        self.ui.paymentView.setColumnWidth(0, 50)
        self.ui.paymentView.setColumnWidth(1, 200)
        self.ui.paymentView.setColumnWidth(2, 150)
        self.ui.paymentView.setColumnWidth(3, 250)
        self.ui.paymentView.setColumnWidth(4, 300)
        self.load_paymentdata()
    
    def load_paymentdata(self):
        row = 0
        payments = self.clientAdmin['payments']
        self.ui.paymentView.setRowCount(len(payments))
        for payment in payments:
            self.ui.paymentView.setItem(row, 0, PySide2.QtWidgets.QTableWidgetItem(str(payment['id'])))
            self.ui.paymentView.setItem(row, 1, PySide2.QtWidgets.QTableWidgetItem(str(payment['transaction_id'])))
            self.ui.paymentView.setItem(row, 2, PySide2.QtWidgets.QTableWidgetItem(str(payment['amount'])))
            self.ui.paymentView.setItem(row, 3, PySide2.QtWidgets.QTableWidgetItem(payment['payment_method']))
            self.ui.paymentView.setItem(row, 4, PySide2.QtWidgets.QTableWidgetItem(str(payment['transaction_id_number'])))
            row+=1

    def deletePayment(self):
        if self.ui.paymentView.currentRow() >= 0:
            paymentId = self.ui.paymentView.currentRow()
            payment = self.clientAdmin['payments'][paymentId]
            CLIENT.deletePayment(payment['id'])
            CLIENT.getAPI()
            self.clientAdmin = CLIENT.readAPI()
            self.init_paymentTable()

    def deleteTransaction(self):
        if self.ui.transactionView.currentRow() >= 0:
            transactionId = self.ui.transactionView.currentRow()
            transaction = self.clientAdmin['transactions'][transactionId]
            CLIENT.deleteTransaction(transaction['id'])
            CLIENT.getAPI()
            self.clientAdmin = CLIENT.readAPI()
            self.init_transactionTable()

    def popAddGame(self, id_game=-1):
        self.ui.rightMenuContainer.expandMenu()
        if id_game != -1:
            self.ui.cancelGameBtn.hide()
            self.ui.doneGameBtn.show()
            gameId = self.ui.gameView.currentRow()
            game = self.clientAdmin['games'][gameId]
            self.ui.idGameText.setText(str(game['id']))
            self.ui.nameGameText.setText(game['name'])
            self.ui.genreGameText.setText(game['genre'])
            self.ui.priceGameText.setText(str(game['price']))
            self.ui.imageGameText.setText(game['images'])
            self.ui.videoGameText.setText(game['videos'])
            self.ui.descriptionGameText.setText(game['description'])
            self.ui.demoGameText.setText(game['demo_file'])
            self.ui.doneGameBtn.clicked.connect(lambda: self.putGame())
        else:
            #post
            self.ui.cancelGameBtn.show()
            self.ui.doneGameBtn.hide()
            self.clearGame()
            self.ui.cancelGameBtn.clicked.connect(lambda: self.postGame())

    def clearGame(self):
        self.ui.idGameText.setText('')
        self.ui.nameGameText.setText('')
        self.ui.genreGameText.setText('')
        self.ui.priceGameText.setText('')
        self.ui.imageGameText.setText('')
        self.ui.videoGameText.setText('')
        self.ui.descriptionGameText.setText('')
        self.ui.demoGameText.setText('')

    def popAddUser(self, id_User=-1):
        self.ui.rightMenuContainer.expandMenu()
        if id_User != -1:
            self.ui.cancelBtn.hide()
            self.ui.doneBtn.show()
            UserId = self.ui.userView.currentRow()
            user = self.clientAdmin['users'][UserId]
            self.ui.idText.setText(str(user['id']))
            self.ui.nameText.setText(user['name'])
            self.ui.emailText.setText(user['email'])
            self.ui.passwordText.setText(str(user['password']))
            self.ui.doneBtn.clicked.connect(lambda: self.putUser())
        else:
            self.ui.cancelBtn.show()
            self.ui.doneBtn.hide()
            self.clearUser()
            self.ui.cancelBtn.clicked.connect(lambda: self.postUser())

    def clearUser(self):
        self.ui.idText.setText('')
        self.ui.nameText.setText('')
        self.ui.passwordText.setText('')
        self.ui.emailText.setText('')

    def deleteGame(self):
        if self.ui.gameView.currentRow() >= 0:
            gameId = self.ui.gameView.currentRow()
            game = self.clientAdmin['games'][gameId]
            CLIENT.deleteGame(game['id'])
            CLIENT.getAPI()
            self.clientAdmin = CLIENT.readAPI()
            self.init_gameTable()

    def postGame(self):
        new_game = {}
        new_game['name'] = self.ui.nameGameText.text()
        new_game['genre'] = self.ui.genreGameText.text()
        new_game['price'] = int(self.ui.priceGameText.text())
        new_game['images'] = self.ui.imageGameText.text()
        new_game['videos'] = self.ui.videoGameText.text()
        new_game['description'] = self.ui.descriptionGameText.text()
        new_game['demo_file'] = self.ui.demoGameText.text()
        CLIENT.postGame(new_game)
        CLIENT.getAPI()
        self.clientAdmin = CLIENT.readAPI()
        self.init_gameTable()
        self.clearGame()
        self.ui.rightMenuContainer.collapseMenu()

    def putGame(self):
        new_game = {}
        new_game['id'] = int(self.ui.idGameText.text())
        new_game['name'] = self.ui.nameGameText.text()
        new_game['genre'] = self.ui.genreGameText.text()
        new_game['price'] = int(self.ui.priceGameText.text())
        new_game['images'] = self.ui.imageGameText.text()
        new_game['videos'] = self.ui.videoGameText.text()
        new_game['description'] = self.ui.descriptionGameText.text()
        new_game['demo_file'] = self.ui.demoGameText.text()
        print("New game--")
        print(new_game)
        CLIENT.putGame(new_game['id'], new_game)
        CLIENT.getAPI()
        self.clientAdmin = CLIENT.readAPI()
        self.init_gameTable()
        self.clearGame()
        self.ui.rightMenuContainer.collapseMenu()

    def deleteUser(self):
        if self.ui.userView.currentRow() >= 0:
            userId = self.ui.userView.currentRow()
            user = self.clientAdmin['users'][userId]
            CLIENT.deleteUser(user['id'])
            CLIENT.getAPI()
            self.clientAdmin = CLIENT.readAPI()
            self.init_userTable()
        
    def postUser(self):
        new_user = {}
        new_user['name'] = self.ui.nameText.text()
        new_user['email'] = self.ui.emailText.text()
        new_user['password'] = self.ui.passwordText.text()
        CLIENT.postUser(new_user)
        CLIENT.getAPI()
        self.clientAdmin = CLIENT.readAPI()
        self.init_userTable()
        self.clearUser()
        self.ui.rightMenuContainer.collapseMenu()

    def putUser(self):
        new_user = {}
        new_user['id'] = int(self.ui.idText.text())
        new_user['name'] = self.ui.nameText.text()
        new_user['email'] = self.ui.emailText.text()
        new_user['password'] = self.ui.passwordText.text()
        print("New game--")
        print(new_user)
        CLIENT.putUser(new_user['id'], new_user)
        CLIENT.getAPI()
        self.clientAdmin = CLIENT.readAPI()
        self.init_userTable()
        self.clearUser()
        self.ui.rightMenuContainer.collapseMenu()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowApp()
    window.show()
    sys.exit(app.exec_())


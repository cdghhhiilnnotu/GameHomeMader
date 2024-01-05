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
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.expandMenu())
        
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuSubContainer.collapseMenu())

        self.ui.addUserBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.editUserBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.addGameBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.editGameBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
     
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

    def deleteGame(self):
        if self.ui.gameView.currentRow() >= 0:
            gameId = self.ui.gameView.currentRow()
            game = self.clientAdmin['games'][gameId]
            CLIENT.deleteGame(game['id'])
            CLIENT.getAPI()
            self.clientAdmin = CLIENT.readAPI()
            self.init_gameTable()

    def deleteUser(self):
        if self.ui.userView.currentRow() >= 0:
            userId = self.ui.userView.currentRow()
            user = self.clientAdmin['users'][userId]
            CLIENT.deleteUser(user['id'])
            CLIENT.getAPI()
            self.clientAdmin = CLIENT.readAPI()
            self.init_userTable()
        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowApp()
    window.show()
    sys.exit(app.exec_())


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
        CLIENT.getAPI()
        self.clientAdmin = CLIENT.readAPI()
        loadJsonStyle(self, self.ui)

        self.show()
        self.init_default_buttons()
        self.init_userTable()


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
            self.ui.userView.setItem(row, 0, PySide2.QtWidgets.QTableWidgetItem(user['id']))
            self.ui.userView.setItem(row, 1, PySide2.QtWidgets.QTableWidgetItem(user['name']))
            self.ui.userView.setItem(row, 2, PySide2.QtWidgets.QTableWidgetItem(user['email']))
            self.ui.userView.setItem(row, 3, PySide2.QtWidgets.QTableWidgetItem(user['password']))
            row+=1





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowApp()
    window.show()
    sys.exit(app.exec_())


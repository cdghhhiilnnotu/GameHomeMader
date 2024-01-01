import os
import sys
from datetime import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mainCLIENT import *
from ui_LoginForm import *
from userUi import *
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2 import QtGui

class MainLoginApp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_btns()
        

    def init_btns(self):
        self.ui.LoginButton.clicked.connect(lambda: self.login_with_role(self.ui.RoleComboBox.currentText(), self.ui.UsernameInput.text(), self.ui.PasswordInput.text()))

    def login_with_role(self, role, user_email, password):
        # windowUser = MainUserApp('tranthibb@exmaple.com')
        # windowUser.show()
        # self.close()
        # openWindow()
        pass
        # if role == "User":
        #     try:
        #         self.client = CLIENT(user_email)
        #         print(user_email)
        #         print(self.client.user_password == password)
        #         if self.client.user_password == password:
        #             print('help')
        #             # self.close()

        #     except:
        #         print(Exception())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainLoginApp()
    window.show()
    sys.exit(app.exec_())
    


from PyQt6 import QtWidgets, uic
import sys
from controllers.login_controller import LoginController
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPalette

class Login(QtWidgets.QMainWindow):
    login_successful = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/login.ui", self)
        self.controller = LoginController(self, self)

class Profile(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/cloudy_profile.ui", self)

class AppManager:
    def __init__(self):
        self.login_window = Login()
        self.profile_window = Profile()
        self.login_window.login_successful.connect(self.show_main_window)
        self.login_window.show()
    def show_main_window(self):
        self.profile_window.show()
        self.login_window.close()
        
app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())
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

class Library(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.load_ui("./views/cloudy_library.ui,self")

class AppManager:
    def __init__(self):
        self.login_window = Login()
        self.cloudy_profile_window = Profile()
        self.login_window.login_successful.connect(self.show_main_window)
        self.login_window.show()
    def show_main_window(self):
        self.cloudy_profile_window.show()
        self.login_window.close()

class AppManager:
    def __init__(self):
        self.cloudy_profile_window = Profile()
        self.library_window = Library()
        self.cloudy_profile_window.profile_successful.connect(self.show_main_window)
        self.cloudy_profile_window.show()
    def show_main_window(self):
        self.library_window.show()
        self.cloudy_profile_window.close()

app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())
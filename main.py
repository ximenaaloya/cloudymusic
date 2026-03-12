from PyQt6 import QtWidgets, uic
import sys
from controllers.login_controller import LoginController
from controllers.playlist_controller import PlaylistController
from controllers.library_controller import LibraryController
from controllers.perfil_controller import PerfilController
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPalette

class Login(QtWidgets.QMainWindow):
    login_successful = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/login.ui", self)
        self.controller = LoginController(self, self)

class Library(QtWidgets.QMainWindow):
    library_successful = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/library.ui", self)
        self.controller = LibraryController(self, self)

class Profile(QtWidgets.QMainWindow):
    perfil_successful = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/cloudy_profile.ui", self)
        self.controller = PerfilController(self, self)

class Playlist(QtWidgets.QMainWindow):
    playlist_successful = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/playlist.ui", self)
        self.controller = PlaylistController(self, self)
class AppManager:
    def __init__(self):
        self.login_window = Login()
        self.cloudy_profile_window = Profile()
        self.library_window = Library()
        self.playlist_window= Playlist()

        #dar de alta las seniales
        self.login_window.login_successful.connect(self.show_main_window)
        self.cloudy_profile_window.perfil_successful.connect(self.show_library_window)
        self.library_window.library_successful.connect(self.show_playlist_window)
        self.cloudy_profile_window.show()#cambiar a login_window
        
    def show_main_window(self):
        self.library_window.show()
        self.login_window.close()
         
    def show_library_window(self):
        self.library_window.show()
        self.cloudy_profile_window.close()
    def show_playlist_window(self):
        self.playlist_window.show()
        self.library_window.close()
        print("HOLA")


app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())
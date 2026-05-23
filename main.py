from PyQt6 import QtWidgets, uic
import sys
from controllers.login_controller import LoginController
from controllers.playlist_controller import PlaylistController
from controllers.library_controller import LibraryController
from controllers.profile_controller import ProfileController
from controllers.song_controller import SongController
from controllers.delete_controller import DeleteController
from controllers.modificar_controller import ModificarController

#from controllers.main_controller import MainController
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
    add_song_successful = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/library.ui", self)
        self.controller = LibraryController(self, self)

class Profile(QtWidgets.QMainWindow):
    profile_successful = pyqtSignal()
    agregar_perfil = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/cloudy_profile.ui", self)
        self.controller = ProfileController(self, self)

class Playlist(QtWidgets.QMainWindow):
    playlist_successful = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/playlist.ui", self)
        self.controller = PlaylistController(self, self)
class Song(QtWidgets.QMainWindow):
    song_succesful = pyqtSignal()
    modificar_successful = pyqtSignal()
    back_song_successful = pyqtSignal()
    agregar_song = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/song.ui", self)
        self.controller = SongController(self, self)
class Delete(QtWidgets.QMainWindow):
    delete_successful = pyqtSignal()
    cancion_eliminada = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/delete.ui", self)
        self.controller = DeleteController(self, self)
class Modificar(QtWidgets.QMainWindow):
    modificar_successful = pyqtSignal()
    mod_song = pyqtSignal()
    #
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/modificar.ui", self)
        self.controller = ModificarController(self, self)


class AppManager:
    def __init__(self):
        self.login_window = Login()
        self.cloudy_profile_window = Profile()
        self.library_window = Library()
        self.playlist_window= Playlist()
        self.song_window= Song()
        self.delete_window = Delete()
        self.modificar_window = Modificar()

        #dar de alta las seniales
        self.login_window.login_successful.connect(self.show_main_window)
        self.cloudy_profile_window.profile_successful.connect(self.show_library_window)
        self.library_window.library_successful.connect(self.show_playlist_window)
        self.playlist_window.playlist_successful.connect(self.show_song_window)
        self.song_window.song_succesful.connect(self.show_delete_window)
        self.song_window.modificar_successful.connect(self.show_modificar_window)
        self.modificar_window.modificar_successful.connect(self.back_modificar)
        self.library_window.add_song_successful.connect(self.add_song)
        self.song_window.back_song_successful.connect(self.back_song)
        self.delete_window.delete_successful.connect(self.back_delete)

        self.delete_window.cancion_eliminada.connect(self.song_window.controller.act_tabla)
        
        self.song_window.agregar_song.connect(self.library_window.controller.act_tabla)
        self.cloudy_profile_window.agregar_perfil.connect(self.library_window.controller.agregar_perfil)

        self.delete_window.cancion_eliminada.connect(self.library_window.controller.act_tabla)

        self.song_window.modificar_successful.connect(self.modificar_window.controller.mod_song)
        self.modificar_window.mod_song.connect(self.song_window.controller.act_tabla)
        #self.modificar_window.cancion_eliminada.connect(self.song_window.controller.eliminar_cancion)
        self.login_window.show()#cambiar
        
    def show_main_window(self):
        self.cloudy_profile_window.show()
        self.login_window.close()
    def show_library_window(self):
        self.library_window.show()
        self.cloudy_profile_window.close()
    def show_playlist_window(self):
        self.playlist_window.show()
        self.library_window.close()
    def show_song_window(self):
        self.playlist_window.close()
        self.song_window.show()
    def show_delete_window(self):
        self.song_window.close()
        self.delete_window.show()
    def show_modificar_window(self):
        self.song_window.close()
        self.modificar_window.show()
    def back_delete(self):
        self.delete_window.close()
        self.song_window.show()
    def back_modificar(self):
        self.modificar_window.close()
        self.song_window.show()
    def back_song(self):
        self.song_window.close()
        self.library_window.show()
    def add_song(self):
        self.library_window.close()
        self.song_window.show()
    


app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())
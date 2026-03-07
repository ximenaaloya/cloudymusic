from PyQt6 import QtWidgets, uic
import sys
from controllers.login_controller import LoginController
from PyQt6.QtCore import Qt, pyqtSignal
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
        self.cmb_gen.addItems(["", "Pop", "Hip-Hop", "Rock", "Reggaetón","R&B"])
        self.btn_m.clicked.connect(self.change_m)
        self.btn_h.clicked.connect(self.change_h)

        self.btn_v.clicked.connect(self.change_color)
        self.btn_a.clicked.connect(self.change_color)
        self.btn_r.clicked.connect(self.change_color)
        self.btn_mo.clicked.connect(self.change_color)

    def change_m(self):
        ruta = "./img/woman.png"
        ruta = ruta.replace("\\", "/")
        self.lbl_pic.setStyleSheet(f"border-image: url({ruta});")

    def change_h(self):
        ruta = "./img/men.png"
        ruta = ruta.replace("\\", "/")
        self.lbl_pic.setStyleSheet(f"border-image: url({ruta});")

    def change_color(self):
        boton = self.sender()
        if boton == self.btn_v:
            self.lbl_name.setStyleSheet("color: #55ff00;")
            print("verde")
        elif boton == self.btn_r:
            self.lbl_name.setStyleSheet("color: #ff0080;")
            print("rosa")
        elif boton == self.btn_a:
            self.lbl_name.setStyleSheet("color: #00aaff;")
            print("azul")
        elif boton == self.btn_mo:
            self.lbl_name.setStyleSheet("color: #aa00ff;")
            print("morado")
    



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
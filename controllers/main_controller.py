import sys
from PyQt6 import QtWidgets, uic
from conexion import Conexion

class MainController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("window.ui", self)
        self.btn_add.clicked.connect(self.add_user)
    def add_user(self):
        self.connection = Conexion()
        self.connection.conectar()
        name = self.txt_name.text()
        last = self.txt_last_name.text()
        email = self.txt_email.text()
        password = self.txt_password.text()
        pass_c = self.txt_pass.text()
        #.strip borra los espacios de las orillas
        if name.strip() == "" or last.strip() == "" or email.strip() == "" or password.strip() == "" or pass_c.strip() == "":
            QtWidgets.QMessageBox.warning(self, "Favor de llenar todos los campos.")
        elif password.strip() != pass_c.strip():
            QtWidgets.QMessageBox.warning(self, "Las contraseñas no coinciden.")
        else:
            sql = "INSERT INTO users VALUES (%s,%s,%s,%s,%s,%s)"
            values = (0, name, last, email, password, 'default.jpg')
            self.connection.insertar(sql,values)
            QtWidgets.QMessageBox.information(self, "Registro insertado correctamente.", None)
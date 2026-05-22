from PyQt6 import QtWidgets, uic
import sys
from controllers.conexion import Conexion
sys.path.append('.')           

class ProfileController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        #self.window.cmb_gen.addItems(["", "Pop", "Hip-Hop", "Rock", "Reggaetón","R&B"])
        self.window.btn_m.clicked.connect(self.change_m)
        self.window.btn_h.clicked.connect(self.change_h)

        self.window.btn_aceptar.clicked.connect(self.add_user)
        #self.window.btn_aceptar.clicked.connect(self.handle_lib)

        self.window.btn_name.clicked.connect(self.set_name)

        self.window.btn_v.clicked.connect(self.change_color)
        self.window.btn_a.clicked.connect(self.change_color)
        self.window.btn_r.clicked.connect(self.change_color)
        self.window.btn_mo.clicked.connect(self.change_color)

    def add_user(self):
        self.connection = Conexion()
        self.connection.conectar()

        #id = self.window.txt_id.text()
        nombre = self.window.txt_name.text()
        desc = self.window.txt_desc.text()
        gen = self.window.txt_gen.text()
        
        #.strip borra los espacios de las orillas
        #id.strip() == "" or 
        if nombre.strip() == "" or desc.strip() == "" or gen.strip() == "":
            QtWidgets.QMessageBox.warning(self.window, "Error", "Favor de llenar todos los campos.")
        else:
            sql = "INSERT INTO perfiles VALUES (%s,%s,%s,%s)"
            values = (0, nombre, desc, gen)
            self.connection.insertar(sql, values)
            self.window.profile_successful.emit()

            row_position = self.window.table.rowCount()
            self.window.table.insertRow(row_position)

            self.window.table.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(nombre)))
            self.window.table.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(desc)))
            self.window.table.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(gen)))

    def change_m(self):
        ruta = "./img/woman.png"
        ruta = ruta.replace("\\", "/")
        self.window.lbl_pic.setStyleSheet(f"border-image: url({ruta});")

    def change_h(self):
        ruta = "./img/men.png"
        ruta = ruta.replace("\\", "/")
        self.window.lbl_pic.setStyleSheet(f"border-image: url({ruta});")

    def change_color(self):
        boton = self.window.sender()
        if boton == self.window.btn_v:
            self.window.lbl_name.setStyleSheet("color: #55ff00;")
        elif boton == self.window.btn_r:
            self.window.lbl_name.setStyleSheet("color: #ff0080;")
        elif boton == self.window.btn_a:
            self.window.lbl_name.setStyleSheet("color: #00aaff;")
        elif boton == self.window.btn_mo:
            self.window.lbl_name.setStyleSheet("color: #aa00ff;")
    def set_name(self):
        name = self.window.txt_name.text()
        self.window.lbl_name.setText(name)


    '''def handle_lib(self):
        self.window.profile_successful.emit()'''
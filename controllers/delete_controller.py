from PyQt6 import QtWidgets, uic
import sys     
from controllers.conexion import Conexion 

class DeleteController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_delete.clicked.connect(self.delete_song)

    def delete_song(self):
        self.connection = Conexion()
        self.connection.conectar()
        cancion = self.window.txt_delete.text()
        print(cancion)
        if cancion.strip() == "" :
            QtWidgets.QMessageBox.warning(self.window, "ERROR", "Favor de llenar todos los campos.")
        else:
            sql = "DELETE FROM songs WHERE nombre = %s"
            values = (cancion,)
            self.connection.insertar(sql, values)
            QtWidgets.QMessageBox.information(self.window, None, "Canción eliminada correctamente.")

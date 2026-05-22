from PyQt6 import QtWidgets, uic
import sys
from PyQt6.QtWidgets import QTableWidgetItem        
from controllers.conexion import Conexion


class ModificarController:
    def __init__(self, window, model):
        self.window = window
        self.model = model

        self.window.btn_mod.hide()
        self.window.lbl_n.hide()
        self.window.lbl_nombre.hide()
        self.window.lbl_artista.hide()
        self.window.lbl_album.hide()
        self.window.lbl_duracion.hide()
        self.window.lbl_genero.hide()
        self.window.lbl_likes.hide()
        self.window.lbl_favoritos.hide()

        self.window.txt_nombre.hide()
        self.window.txt_artista.hide()
        self.window.txt_album.hide()
        self.window.txt_duracion.hide()
        self.window.txt_genero.hide()
        self.window.txt_likes.hide()
        self.window.txt_favoritos.hide()

        self.window.btn_aceptar.clicked.connect(self.modificar_song)
        self.window.btn_mod.clicked.connect(self.mod_song)
        self.window.btn_back.clicked.connect(self.back_modificar)

    def back_modificar(self):
        self.window.modificar_successful.emit()

    def modificar_song(self):
        db = Conexion()
        cursor = db.cursor
        self.conexion = Conexion()
        self.conexion.conectar()


        song = self.window.txt_song.text()
        sql = "SELECT * FROM songs WHERE nombre = %s"
        resultado = self.conexion.seleccionar(sql, (song,))

        if resultado:
            print("Existe")
            self.nombre_original = song
            QtWidgets.QMessageBox.information(self.window, "Canción encontrada", "Insertar nuevos datos.")
            self.window.lbl_n.show()
            self.window.btn_mod.show()
            self.window.lbl_nombre.show()
            self.window.lbl_artista.show()
            self.window.lbl_album.show()
            self.window.lbl_duracion.show()
            self.window.lbl_genero.show()
            self.window.lbl_likes.show()
            self.window.lbl_favoritos.show()

            self.window.txt_nombre.show()
            self.window.txt_artista.show()
            self.window.txt_album.show()
            self.window.txt_duracion.show()
            self.window.txt_genero.show()
            self.window.txt_likes.show()
            self.window.txt_favoritos.show()

            

        else:
            print("No existe")
            QtWidgets.QMessageBox.information(self.window, None, "Canción no encontrada")
       
    def mod_song(self):
        new_nombre = self.window.txt_nombre.text()
        new_artista = self.window.txt_artista.text()
        new_album = self.window.txt_album.text()
        new_duracion = self.window.txt_duracion.text()
        new_genero = self.window.txt_genero.text()
        new_likes = self.window.txt_likes.text()
        new_favorito = self.window.txt_favoritos.text()
        name = self.window.txt_nombre.text()

        
        if new_nombre.strip() == "" or new_artista.strip() == "" or new_album.strip() == "" or new_duracion.strip() == "" or new_genero.strip() == "" or new_likes.strip() == "" or new_favorito.strip() == "":
            QtWidgets.QMessageBox.warning(self.window, "ERROR", "Favor de llenar todos los campos.")
        else:
            sql = "UPDATE songs SET nombre = %s, artista = %s, album = %s, duracion = %s, genero = %s, likes = %s, favorito = %s WHERE nombre = %s"
            values = (new_nombre, new_artista, new_album, new_duracion, new_genero, new_likes, new_favorito, self.nombre_original)
            self.conexion.insertar(sql, values)
            self.name = name
            QtWidgets.QMessageBox.warning(self.window, None, "Canción modificada correctamente.")
            self.window.txt_nombre.clear()
            self.window.txt_artista.clear()
            self.window.txt_album.clear()
            self.window.txt_duracion.clear()
            self.window.txt_genero.clear()
            self.window.txt_likes.clear()
            self.window.txt_favoritos.clear()
            self.window.txt_song.clear()
            self.window.modifi_song.emit()
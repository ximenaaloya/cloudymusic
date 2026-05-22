from PyQt6 import QtWidgets, uic
import sys
from PyQt6.QtWidgets import QTableWidgetItem
from controllers.conexion import Conexion


class SongController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_add_song.clicked.connect(self.add_song)
        self.window.btn_modificar.clicked.connect(self.modificar_song)
        self.window.btn_mod.clicked.connect(self.mod_song)
        self.window.btn_back.clicked.connect(self.back_song)
        #self.window.btn_back.clicked.connect(self.back)
        #self.conexion = Conexion()
        #self.conexion.conectar()

        
    def add_song(self):
        self.connection = Conexion()
        self.connection.conectar()

        #id = self.window.txt_id.text()
        nombre = self.window.txt_name.text()
        artista = self.window.txt_artist.text()
        album = self.window.txt_album.text()
        duracion = self.window.txt_duracion.text()
        genero = self.window.txt_genero.text()
        likes = self.window.txt_likes.text()
        favoritos = self.window.txt_favoritos.text()

        
        '''self.window.lbl_name.setText(nombre)
        self.window.lbl_artist.setText(artista)'''
        
        #.strip borra los espacios de las orillas
        #id.strip() == "" or 
        if nombre.strip() == "" or artista.strip() == "" or album.strip() == "" or duracion.strip() == "" or genero.strip() == "" or likes.strip() == "" or favoritos.strip() == "":
            QtWidgets.QMessageBox.warning(self.window, "ERROR", "Favor de llenar todos los campos.")
        else:
            sql = "INSERT INTO songs VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (0, nombre, artista, album, duracion, genero, likes, favoritos)
            self.connection.insertar(sql, values)
            QtWidgets.QMessageBox.information(self.window, "Registro exitoso", "Canción registrada correctamente.")

            row_position = self.window.table.rowCount()
            self.window.table.insertRow(row_position)

            self.window.table.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(nombre)))
            self.window.table.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(artista)))
            self.window.table.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(album)))
            self.window.table.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(duracion)))
            self.window.table.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(genero)))
            self.window.table.setItem(row_position, 5, QtWidgets.QTableWidgetItem(str(likes)))
            self.window.table.setItem(row_position, 6, QtWidgets.QTableWidgetItem(str(favoritos)))

    def modificar_song(self):
        self.window.song_succesful.emit()
        
    def mod_song(self):
        self.window.modificar_successful.emit()
    
    def back_song(self):
        self.window.back_song_successful.emit()

    
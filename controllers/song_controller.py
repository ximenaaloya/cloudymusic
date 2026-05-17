import sys
from PyQt6 import QtWidgets, uic
from conexion import Conexion


class SongController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_aceptar.clicked.connect(self.add_song)
        self.conexion = Conexion()
        self.conexion.conectar()

        self.window.btn_aceptar.clicked.connect(self.mostrar_cancion)

        self.window.btn_agregar.clicked.connect(self.agregar_cancion)

        
    def add_song(self):
        name = self.window.txt_name.text()
        artist = self.window.txt_artist.text()
        self.window.lbl_name.setText(name)
        self.window.lbl_artist.setText(artist)
        song = [name, artist]
        print(song)

    def agregar_cancion(self):
        nombre  = self.window.txt_nombre.text().strip()
        artista = self.window.txt_artista.text().strip()
 
        if nombre == "" or artista == "":
            QtWidgets.QMessageBox.warning(self.window, "CloudyMusic", "Llena los campos Nombre y Artista.")
            return
 

        sql    = "INSERT INTO canciones (nombre, artista) VALUES (%s, %s)"
        valores = (nombre, artista)
        self.conexion.insertar(sql, valores)
 
        QtWidgets.QMessageBox.information(self.window, "CloudyMusic", f"'{nombre}' agregada correctamente.")
        self.window.txt_nombre.clear()
        self.window.txt_artista.clear()
 
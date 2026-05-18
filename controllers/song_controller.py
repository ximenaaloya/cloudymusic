from PyQt6 import QtWidgets, uic
import sys
sys.path.append('.')            
from controllers.conexion import Conexion


class SongController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_add_song.clicked.connect(self.add_song)
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

        
        self.window.lbl_name.setText(nombre)
        self.window.lbl_artist.setText(artista)
        
        #.strip borra los espacios de las orillas
        #id.strip() == "" or 
        if nombre.strip() == "" or artista.strip() == "" or album.strip() == "" or duracion.strip() == "" or genero.strip() == "" or likes.strip() == "" or favoritos.strip() == "":
            QtWidgets.QMessageBox.warning(self, "Favor de llenar todos los campos.")
        else:
            sql = "INSERT INTO songs VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (0, nombre, artista, album, duracion, genero, likes, favoritos)
            self.connection.insertar(sql, values)
            #QtWidgets.QMessageBox.information(self, "Canción registrada correctamente.", None)
        
        
        
        
        '''nombre  = self.window.txt_nombre.text().strip()
        artista = self.window.txt_artista.text().strip()
 
        if nombre == "" or artista == "":
            QtWidgets.QMessageBox.warning(self.window, "CloudyMusic", "Llena los campos Nombre y Artista.")
            return
 

        sql    = "INSERT INTO canciones (nombre, artista) VALUES (%s, %s)"
        valores = (nombre, artista)
        self.conexion.insertar(sql, valores)
 
        QtWidgets.QMessageBox.information(self.window, "CloudyMusic", f"'{nombre}' agregada correctamente.")
        self.window.txt_nombre.clear()
        self.window.txt_artista.clear()'''
 
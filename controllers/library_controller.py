from PyQt6 import QtWidgets, uic
import sys         
from controllers.conexion import Conexion 
from PyQt6.QtWidgets import QTableWidgetItem

class LibraryController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        #self.window.btn_playlist.clicked.connect(self.handle_playlist)
        self.window.btn_add.clicked.connect(self.add_song)
        
        self.conexion = Conexion()
        self.conexion.conectar()
        self.cargar_canciones()
        
    def act_tabla(self):
        self.cargar_canciones()

    def cargar_canciones(self):
        self.connection = Conexion()
        self.connection.conectar()
        self.window.table_L.setRowCount(0)

        sql = "SELECT nombre, artista, album, duracion, genero, likes, favorito FROM songs"
        canciones = self.connection.seleccionar(sql)

        if canciones:
            for row_n, row_d in enumerate(canciones):
                self.window.table_L.insertRow(row_n)
                for column_n, data in enumerate(row_d):
                    self.window.table_L.setItem(row_n, column_n, QTableWidgetItem(str(data)))
    
    def agregar_perfil(self):
        self.connection = Conexion()
        self.connection.conectar()
        self.window.tabla_perfil.setRowCount(0)

        sql = "SELECT nombre, descripcion, genero_pref FROM perfiles"
        canciones = self.connection.seleccionar(sql)

        if canciones:
            for row_n, row_d in enumerate(canciones):
                self.window.tabla_perfil.insertRow(row_n)
                for column_n, data in enumerate(row_d):
                    self.window.tabla_perfil.setItem(row_n, column_n, QTableWidgetItem(str(data)))


    def handle_playlist(self):
        self.window.library_successful.emit()
    def add_song(self):
        self.window.add_song_successful.emit()

    '''def cargar_canciones(self):

        sql       = "SELECT nombre, artista, album, duracion, genero, likes, favorito FROM canciones"
        resultado = self.conexion.seleccionar(sql)

        tabla = self.window.tableWidget
        tabla.setRowCount(len(resultado))
        tabla.setColumnCount(8)
        tabla.setHorizontalHeaderLabels(
            ["Imagen", "Canción", "Artista", "Álbum", "Duración", "Género", "Likes", "Favorito"])
        
        for i, fila in enumerate(resultado):
            nombre, artista, album, duracion, genero, likes, favorito = fila
            tabla.setItem(i, 0, QtWidgets.QTableWidgetItem(""))
            tabla.setItem(i, 1, QtWidgets.QTableWidgetItem(nombre   or ""))
            tabla.setItem(i, 2, QtWidgets.QTableWidgetItem(artista  or ""))
            tabla.setItem(i, 3, QtWidgets.QTableWidgetItem(album    or ""))
            tabla.setItem(i, 4, QtWidgets.QTableWidgetItem(duracion or ""))
            tabla.setItem(i, 5, QtWidgets.QTableWidgetItem(genero   or ""))
            tabla.setItem(i, 6, QtWidgets.QTableWidgetItem(str(likes or 0)))
            tabla.setItem(i, 7, QtWidgets.QTableWidgetItem("Sí" if favorito else "No"))'''
        
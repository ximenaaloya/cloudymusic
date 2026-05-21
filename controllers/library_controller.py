from PyQt6 import QtWidgets, uic
import sys
sys.path.append('.')            
from controllers.conexion import Conexion 

class LibraryController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_playlist.clicked.connect(self.handle_playlist)
        self.conexion = Conexion()
        self.conexion.conectar()

        #self.cargar_canciones()

    def handle_playlist(self):
        self.window.library_successful.emit()

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
        
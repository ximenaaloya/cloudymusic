from PyQt6 import QtWidgets, uic
import sys
from conexion import Conexion

class PlaylistController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_add.clicked.connect(self.handle_song)
        self.conexion = Conexion()
        self.conexion.conectar()

        self.cargar_canciones()

    def handle_song(self):
        self.window.playlist_successful.emit()

    def cargar_canciones(self):
        sql       = "SELECT id_cancion, nombre, artista, album, duracion, genero, likes, favorito FROM canciones"
        resultado = self.conexion.seleccionar(sql)
 
        tabla = self.window.tableWidget
        tabla.setRowCount(len(resultado))
        tabla.setColumnCount(8)
        tabla.setHorizontalHeaderLabels(
            ["ID", "Canción", "Artista", "Álbum", "Duración", "Género", "Likes", "Favorito"]
        )
 
        for i, fila in enumerate(resultado):
            id_c, nombre, artista, album, duracion, genero, likes, favorito = fila
            tabla.setItem(i, 0, QtWidgets.QTableWidgetItem(str(id_c)))
            tabla.setItem(i, 1, QtWidgets.QTableWidgetItem(nombre   or ""))
            tabla.setItem(i, 2, QtWidgets.QTableWidgetItem(artista  or ""))
            tabla.setItem(i, 3, QtWidgets.QTableWidgetItem(album    or ""))
            tabla.setItem(i, 4, QtWidgets.QTableWidgetItem(duracion or ""))
            tabla.setItem(i, 5, QtWidgets.QTableWidgetItem(genero   or ""))
            tabla.setItem(i, 6, QtWidgets.QTableWidgetItem(str(likes or 0)))
            tabla.setItem(i, 7, QtWidgets.QTableWidgetItem("Sí" if favorito else "No"))
 

    def actualizar_cancion(self):
        id_str, ok1 = QtWidgets.QInputDialog.getText(
            self.window, "Modificar", "ID de la canción a modificar:"
        )
        if not ok1 or not id_str.strip().isdigit():
            return
 
        nuevo_nombre, ok2 = QtWidgets.QInputDialog.getText(
            self.window, "Modificar", "Nuevo nombre:"
        )
        if not ok2 or nuevo_nombre.strip() == "":
            return
 
        sql    = "UPDATE canciones SET nombre = %s WHERE id_cancion = %s"
        valores = (nuevo_nombre.strip(), int(id_str.strip()))
        self.conexion.insertar(sql, valores)
 
        QtWidgets.QMessageBox.information(self.window, "CloudyMusic", "Canción actualizada correctamente.")
        self.cargar_canciones()
 
    def eliminar_cancion(self):
        id_str, ok = QtWidgets.QInputDialog.getText(
            self.window, "Eliminar", "ID de la canción a eliminar:"
        )
        if not ok or not id_str.strip().isdigit():
            return
 
        sql    = "DELETE FROM canciones WHERE id_cancion = %s"
        valores = (int(id_str.strip()),)
        self.conexion.insertar(sql, valores)
 
        QtWidgets.QMessageBox.information(self.window, "CloudyMusic", "Canción eliminada correctamente.")
        self.cargar_canciones() 

      
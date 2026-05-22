from PyQt6 import QtWidgets, uic
import sys
from PyQt6.QtWidgets import QTableWidgetItem        
from controllers.conexion import Conexion


class ModificarController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        #self.window.btn_add_song.clicked.connect(self.add_song)
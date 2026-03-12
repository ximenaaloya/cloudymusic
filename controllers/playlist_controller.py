from PyQt6 import QtWidgets, uic

class PlaylistController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_agregar.clicked.connect(self.handle_agregar)

    def handle_agregar(self):
        self.window.playlist_successful.emit()
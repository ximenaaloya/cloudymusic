from PyQt6 import QtWidgets, uic

class PlaylistController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_add.clicked.connect(self.handle_song)
    def handle_song(self):
        self.window.playlist_successful.emit()

      
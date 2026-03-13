from PyQt6 import QtWidgets, uic

class LibraryController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_playlist.clicked.connect(self.handle_playlist)

    def handle_playlist(self):
        self.window.library_successful.emit()
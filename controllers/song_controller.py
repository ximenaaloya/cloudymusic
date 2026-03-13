class SongController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_aceptar.clicked.connect(self.add_song)
        
    def add_song(self):
        name = self.window.txt_name.text()
        artist = self.window.txt_artist.text()
        self.window.lbl_name.setText(name)
        self.window.lbl_artist.setText(artist)
        song = [name, artist]
        print(song)
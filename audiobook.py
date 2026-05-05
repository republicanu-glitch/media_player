from MediaItem import MediaItem

class AudioBook(MediaItem):
    
    def __init__(self, titlu, autor, durata,capitol):
        super().__init__(titlu, autor, durata)
        self.capitl= capitol
    
    def reda(self):
        print('Audiobookul este redat')

    def tip(self):
        print('AudioBook')
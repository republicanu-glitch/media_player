from MediaItem import MediaItem

class Podcast(MediaItem):
    
    def __init__(self, titlu, autor, durata, episod):
        super().__init__(titlu, autor, durata)
        self.episod = episod
    
    def reda(self):
        print('Podcastul este redata')

    def tip(self):
        print('Podcast')
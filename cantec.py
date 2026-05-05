from MediaItem import MediaItem

class Cantec(MediaItem):
    
    def __init__(self, titlu, autor, durata, gen):
        super().__init__(titlu, autor, durata)
        self.gen = gen
    
    def reda(self):
        print('Melodia este redata')

    def tip(self):
        print('Cantec')
    


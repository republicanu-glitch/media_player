from abc import ABC, abstractmethod

class MediaItem(ABC):

    def __init__(self, titlu, autor, durata):
        self.titlu = titlu
        self.autor = autor
        self.durata = durata

    @abstractmethod
    def reda(self):
        pass

    @abstractmethod
    def tip(self):
        pass

    def durata_formatata(self):
        secunde = self.durata % 60
        minute = self.durata // 60
        timp = str(minute) + ':' + str(secunde)
        return timp
        #print(f'MediaItem are {minute} minut/e si/sau {secunde} secunde')

    def __str__(self):
        return f'MediaItem {self.titlu}, creat de {self.autor}, are o durata {self.durata_formatata()}'
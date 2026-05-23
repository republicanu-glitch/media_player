class Playlist:

    def __init__(self, nume):
        self.nume = nume
        self.elemente = []

    def adauga(self, item):
        self.elemente.append(item)
        print(f'MediaItem-ul {item} a fost adaugat si functioneaza')
    
    def sterge(self, titlu):
        
        for item in self.elemente:
            if item.titlu == titlu:
                self.elemente.remove(item)
                print(f"'{titlu}' a fost sters din playlist '{self.nume}'.")

        print(f"'{titlu}' nu a fost gasit in playlist '{self.nume}'.")


    def reda_tot(self):
        for i in self.elemente:
            i.reda()

    def durata_totala(self):
        durata_t = 0
        for item in self.elemente:
            self.durata_t += item.durata
        
        ore = durata_t // 3600
        minute = (durata_t % 3600) // 60
        secunde = (durata_t % 3600) % 60
        return f"{ore} h, {minute} m, {secunde} s"
    
    def __len__(self):
        return len(self.elemente)
    
    def __str__(self):
        return f'Playlist-ul {self.nume} are {self.lista} elemente cu o durata totala de {self.durata_totala}'


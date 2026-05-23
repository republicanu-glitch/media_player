from MediaItem import MediaItem
from cantec import Cantec
from podcast import Podcast
from audiobook import AudioBook
from playlist import Playlist

c = Cantec('Taraful Joi', ' Salamior', 234, 'manea')
a = AudioBook('Ion', 'Liviu Rebreanu', 134090, 20)
p = Podcast('Importanta programarii', 'Negrea Cristian', 5670, 3)
pl = Playlist('Playlistul meu') 


#lista = [c, a, p]
#for i in lista:
    #print(i)
    #i.reda()
    #i.tip()
def interogare(o):
    global pl
    titlu = input('titlu :')
    autor = input('autor: ')
    durata = int(input('Durata: '))
    if o == '2':
        gen = input('Gen: ')
        pl.adauga(Cantec(titlu, autor, durata, gen))
    elif o == '3':
        capitole = int(input('capitole: '))
        pl.adauga(AudioBook(titlu, autor, durata, capitole))
    elif o =='4':
        episoade = int(input('episoade: '))
        pl.adauga(Podcast(titlu, autor, durata, episoade))
    
def meniu():
 while True:
    print('----------------------')
    print(" 1. Reda tot ")
    print(" 2. Adauga cantec ")
    print(" 3. Adauga audiobook ")
    print(" 4. Adauga podcast ")
    print(" 5. Sterge media item ")
    print(" 6. Afiseaza toata media ")
    print(" 0. Iesire ")
    print('----------------------')
 
    opt = input('Alegerea ta: ')
 
    if opt =='1':
        pl.reda_tot()
     
    elif opt == '2' or opt == '3' or opt == '4':
        interogare(opt)
              
    elif opt == '5':
         titlu = input('titlu: ')
         pl.sterge(titlu)
 
    elif opt == '6':
         for elem in pl.elemente:
             print(elem)
     
    elif opt =='0':
         print('Salut!')
         break

if __name__ == '__main__':
    meniu()
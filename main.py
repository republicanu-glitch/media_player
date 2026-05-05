from MediaItem import MediaItem
from cantec import Cantec
from podcast import Podcast
from audiobook import AudioBook

c = Cantec('Taraful Joi', ' Salamior', 234, 'manea')
a = AudioBook('Ion', 'Liviu Rebreanu', 134090, 20)
p = Podcast('Importanta programarii', 'Negrea Cristian', 5670, 3)

lista = [c, a, p]
for i in lista:
    print(i)
    i.reda()
    i.tip()
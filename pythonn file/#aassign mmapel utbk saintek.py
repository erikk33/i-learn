#aassign mmapel utbk saintek
from gzip import BadGzipFile
from unittest import result


mapelutbk_saintek = ['matematika saintek', 'fisika', 'kimia', 'biologi', 'tps', 'bahasa inggris', 'tka']
pembatas = ['-----------------------------------------------------------------------------------------------']
materiutbk_saintek = ['matriks', 'peluang', 'statiska', 'persamaan garis', 'termodinamika', 
'kinematika gerak', 'bunyi', 'kalor', 
'fluida', 'fisika atom dan inti', 'elektrokimia', 'evolusi', 'bioteknologi', 'plantae', 'animalia']


#mapel harus dipelajari secepatnya
for u in range(len(mapelutbk_saintek)):
    print("by miku nakano : hallo erik kamu harus belajar lebih giat", "GANBATEガンバッテ💪", mapelutbk_saintek[u])
 
#pemabatas
for p in range(len(pembatas)):
    print("___----------------------", pembatas[p])
   

#materi yang sudah dipelajari dengan lengkap
for e in range(len(materiutbk_saintek)):
    print("by miku nakano : hallo erik kamu sudah belajar materi", "GANBATEガンバッテ💪",  materiutbk_saintek[e])

#hasil
e = 2416
b = 10
bagi_kaalivolume = e * b
bagi_volume = e / b

print("by miku chan persentage erikkun lulus", bagi_kaalivolume)
print(bagi_volume)
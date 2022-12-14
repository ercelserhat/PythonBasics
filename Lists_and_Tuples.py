liste1 = ["eleman1", "eleman2", "eleman3"]
print(type(liste1)) #<class 'list'>

liste2 = ["Ahmet", "Mehmet", 23, 65, 3.2]

liste3 = ["Ahmet", "Mehmet", ["Ali", "Veli"], 23, 65, 3.2]

print(len(liste3)) #6

liste4 = [[0, 10], [6, 60], [12, 54], [67, 99]]
for i in liste4:
    print(*range(*i))

#list() fonksiyonu
liste5 = list()
print(liste5) # []

print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
harfListesi = list(alfabe)
print(harfListesi) #['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']

meyveler = ["elma", "armut", "çilek", "kiraz"]
print(meyveler[0]) #elma
print(meyveler[1]) #armut
print(meyveler[2]) #çilek
print(meyveler[3]) #kiraz

for meyve in meyveler:
    print(meyve)

for index in range(len(meyveler)):
    print("{}. {}".format(index, meyveler[index]))
#0. elma
#1. armut
#2. çilek
#3. kiraz

for index, meyve in enumerate(meyveler, 1):
    print("{}. {}".format(index, meyve))
#0. elma
#1. armut
#2. çilek
#3. kiraz

print(meyveler[-1]) #kiraz
print(meyveler[0:2]) #['elma', 'armut']
print(meyveler[::-1]) #['kiraz', 'çilek', 'armut', 'elma']

renkler = ["kırmızı", "sarı", "mavi", "yeşil", "beyaz"]
print(renkler) #['kırmızı', 'sarı', 'mavi', 'yeşil', 'beyaz']
renkler[0] = "siyah"
print(renkler) #['siyah', 'sarı', 'mavi', 'yeşil', 'beyaz']

liste6 = [1, 2, 3]
liste6[0:len(liste6)] = 5, 6, 7
print(liste6) #[5, 6, 7]
liste6[:] = 8, 9, 10
print(liste6) #[8, 9, 10]

liste7 = [0, 2, 4]
liste7 = liste7 + [6, 8, 10]
print(liste7) #[0, 2, 4, 6, 8, 10]

derlenenDiller = ["C", "C++", "C#", "Java"]
yorumlananDiller = ["Python", "Perl", "Ruby"]
programlamaDilleri = derlenenDiller + yorumlananDiller
print(programlamaDilleri) #['C', 'C++', 'C#', 'Java', 'Python', 'Perl', 'Ruby']

notToplam = 0
notlar = []
for i in range(5):
    veri = int(input("{}. notu girin: ".format(i+1)))
    notToplam += veri
    notlar += [veri]
print("Girdiğiniz notlar: ", *notlar)
print("Not ortalamanız: ", notToplam/5)

liste8 = [1, 2, 3, 4, 5]
del liste8[-1]
print(liste8) #[1, 2, 3, 4]
del liste8
#print(liste8) #NameError: name 'liste8' is not defined

#Listeleri kopyalamak
liste9 = ["ahmet", "mehmet", "özlem"]
liste10 = liste9[:]
print(liste9) #['ahmet', 'mehmet', 'özlem']
print(liste10) #['ahmet', 'mehmet', 'özlem']
liste10[0] = "veli"
print(liste9) #['ahmet', 'mehmet', 'özlem']
print(liste10) #['veli', 'mehmet', 'özlem']

liste11 = list(liste9)
print(liste11) #['ahmet', 'mehmet', 'özlem']


#Liste Üreteçleri (List Comprehensions)
liste12 = [i for i in range(100)]
print(liste12)

liste13 = list(range(100))
print(liste13)

listeCiftSayilar = [i for i in range(100) if i % 2 == 0]
print(listeCiftSayilar)
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 
#52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

liste14 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
liste15 = []
for i in liste14:
    for x in i:
        liste15 += [x]
print(liste15) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

liste16 = [x for i in liste14 for x in i]
print(liste16)
def selamla(isim):
    print("Merhaba {}!".format(str(isim)))

selamla("Serhat") #Merhaba Serhat!


def kayitOlustur(isim, soyisim, yas):
    print("-"*30)
    print("İsim    : ", isim)
    print("Soyisim : ", soyisim)
    print("Yaş     : ", yas)
    print("-"*30)

kayitOlustur("Serhat", "Erçel", 30)


def sistemBilgisiniGoster():
    import sys
    print("\nSistemde kurulu Python'ın;")
    print("\tAna sürüm numarası: ", sys.version_info.major)
    print("\tAlt sürüm numarası: ", sys.version_info.minor)
    print("\tMinik sürüm numarası: ", sys.version_info.micro)
    print("\nKullanılan işletim sisteminin;")
    print("\tAdı: ", sys.platform)

sistemBilgisiniGoster()


def kareBul(sayi):
    print("{} sayısının karesi {} sayısıdır.".format(sayi, sayi**2))

kareBul(12) #12 sayısının karesi 144 sayısıdır.
kareBul(9)  #9 sayısının karesi 81 sayısıdır.


def uzunluk(kelime):
    c = 0
    for s in kelime:
        c += 1
    print("{} kelimesinin uzunluğu: {}".format(kelime, c))

uzunluk("Serhat") #Serhat kelimesinin uzunluğu: 6


#İSİMLİ PARAMETRELER
kayitOlustur(isim="Serap", yas=22, soyisim="Erçel")

#VARSAYILAN DEĞERLİ PARAMETRELER
def kur(kurulumDizini = "/usr/bin/"):
    print("Program {} dizinine kuruldu.".format(kurulumDizini))

kur() #Program /usr/bin/ dizinine kuruldu.
kur("C:/Users/Serhat") #Program C:/Users/Serhat dizinine kuruldu.

#RASTGELE SAYIDA İSİMSİZ PARAMETRELER
def carp(*sayilar):
    sonuc = 1
    for i in sayilar:
        sonuc *= i
    print(sonuc)

carp(1, 2, 3, 4, 5) #120

#RASTGELE SAYIDA İSİMLİ PARAMETRELER
def fonksiyon(**args):
    print(args)

fonksiyon(isim="Ahmet", soyisim="Öz", meslek="Mühendis", sehir="Ankara") #{'isim': 'Ahmet', 'soyisim': 'Öz', 'meslek': 'Mühendis', 'sehir': 'Ankara'}


def karsilikBul(*args, **kwargs):
    for sozcuk in args:
        if sozcuk in kwargs:
            print("{} = {}".format(sozcuk, kwargs[sozcuk]))
        else:
            print("{} kelimesi sözlükte yok!".format(sozcuk))

sozluk = {
    "kitap":"book",
    "bilgisayar":"computer",
    "programlama":"programming"
}

karsilikBul("kitap", "bilgisayar", "programlama", "fonksiyon", **sozluk)
#kitap = book
#bilgisayar = computer
#programlama = programming
#fonksiyon kelimesi sözlükte yok!


def yazdir(*args, start="", **kwargs):
    for oge in args:
        print(start + oge, **kwargs)
yazdir("Öğe 1", "Öğe 2", "Öğe 3", start="#-")
#-Öğe 1
#-Öğe 2
#-Öğe 3


#RETURN 
def isimAl():
    isim = input("İsminiz: ")
    return isim

ad = isimAl()
print("Merhaba {}".format(ad)) #Merhaba serhat


#ÖRNEK
import random
def sayiUret(baslangic=0, bitis=500, adet=6):
    sayilar = set()
    while len(sayilar) < adet:
        sayilar.add(random.randrange(baslangic, bitis))
    return sayilar

print(sayiUret()) #{384, 322, 71, 183, 216, 411}
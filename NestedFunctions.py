def yazici():
    def yaz(mesaj):
        print(mesaj)
    return yaz

y = yazici()
y("Merhaba")


#nonlocal
def kapsayiciFonksiyon():
    nonLocalDegisken = 1
    def icFonksiyon():
        nonlocal nonLocalDegisken
        nonLocalDegisken += 1
        print(nonLocalDegisken)
    return icFonksiyon

donusFonksiyonu = kapsayiciFonksiyon()
donusFonksiyonu() #2


def selamla(mesaj):
    def yaz():
        nonlocal mesaj
        mesaj += " Dünya"
        print(mesaj)
    return yaz

s = selamla("Merhaba")
s() #Merhaba Dünya


def sayici():
    sayi = 0
    def say():
        nonlocal sayi
        sayi += 1
        return sayi
    return say

s = sayici()
print(s()) #1
print(s()) #2
print(s()) #3
print(s()) #4



def islemYapici(*eklenenler):
    ekle = 0
    for i in eklenenler:
        ekle += i 
    def islem(sayi, bolen):
        return sayi / bolen + ekle
    return islem

islemci = islemYapici(1, 4, 5)
islemci2 = islemYapici(3, 6, 2)
print(islemci(60, 12)) #15.0
print(islemci(48, 4)) #22.0
print(islemci2(12, 6)) #13.0
print(islemci2(12, 4)) #14.0
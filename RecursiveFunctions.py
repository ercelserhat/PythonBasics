#Örnek-1

def azalt(metin):
    if len(metin) < 1:
        return metin
    else:
        print(metin)
        return azalt(metin[1:])

print(azalt("serhat"))
"""
serhat
erhat
rhat
hat
at
t"""


#Örnek-2
def tersCevir(s):
    if len(s) < 1:
        return s
    else:
        tersCevir(s[1:])
        print(s[0])
    
print(tersCevir("serhat"))


#Örnek-3
def sayac(sayi, sinir):
    print(sayi)
    if sayi == sinir:
        return "Bitti"
    else:
        return sayac(sayi+1, sinir)

print(sayac(0, 10))


#Örnek-4
karisikListe = [1, 2, 3, [4, 5, 6], [7, 8, 9, [10, 11], 12], 13, 14]
def duz_liste_yap(liste):
    if not isinstance(liste, list):
        return [liste]
    elif not liste:
        return []
    else:
        return duz_liste_yap(liste[0]) + duz_liste_yap(liste[1:])

print(duz_liste_yap(karisikListe)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


#Örnek-5
def topla(sayilar):
    if len(sayilar) < 1:
        return 0
    else:
        ilk, son = sayilar[0], sayilar[1:]
        return ilk + topla(son)

liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(topla(liste)) #55
isim = input("İsminiz nedir?")
print("Merhaba", isim)

sayi = int(input("Bir sayı girin: "))
print("Girdiğiniz sayının karesi: ", sayi ** 2)


#EXAMPLE - Daire alanı hesaplama
cap = input("Dairenin çapı: ")
yariCap = int(cap) / 2
pi = 3.14
alan = pi * (yariCap * yariCap)
print("Çapı", cap, "cm olan dairenin alanı: ", alan, "cm2'dir")

#Format() metodu
print("{} ve {} iyi bir ikilidir.".format("Python", "Django"))
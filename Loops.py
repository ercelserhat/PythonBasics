#WHILE LOOP

#example
s = 1
while s < 10:
    print(s)
    s += 1

#example
s2 = 0
while s2 < 100:
    s2 += 1
    if s2 % 10 == 0:
        print(s2)

#example
while True:
    parola = input("Bir parola berleyin: ")
    if not parola:
        print("Parola boş geçilemez!")
    elif len(parola) > 8 or len(parola) < 3:
        print("Parola 8 karakterden uzun, 3 karakterden kısa olmamalı!")
    else:
        print("Yeni parolanız: ", parola)
        break

#EXAMPLE - HESAP MAKİNESİ
giris = """
1 - TOPLA
2 - ÇIKAR
3 - ÇARP
4 - BÖL
5 - KARESİNİ HESAPLA
6 - KAREKÖK HESAPLA
"""

print(giris)

while True:
    soru = input("İşlem numarasını girin (Çıkmak için 'q'): ")
    if soru == "q":
        print("Çıkış yapılıyor...")
        break
    elif soru == "1":
        sayi1 = int(input("Birinci sayı: "))
        sayi2 = int(input("İkinci sayı: "))
        print(sayi1, " + ", sayi2, " = ", sayi1 + sayi2)
    elif soru == "2":
        sayi1 = int(input("Birinci sayı: "))
        sayi2 = int(input("İkinci sayı: "))
        print(sayi1, " - ", sayi2, " = ", sayi1 - sayi2)
    elif soru == "3":
        sayi1 = int(input("Birinci sayı: "))
        sayi2 = int(input("İkinci sayı: "))
        print(sayi1, " x ", sayi2, " = ", sayi1 * sayi2)
    elif soru == "4":
        sayi1 = int(input("Birinci sayı: "))
        sayi2 = int(input("İkinci sayı: "))
        print(sayi1, " / ", sayi2, " = ", sayi1 / sayi2)
    elif soru == "5":
        sayi1 = int(input("Karesini hesaplamak istediğiniz sayı: "))
        print(sayi1, " karesi = ", sayi1 ** 2)
    elif soru == "6":
        sayi1 = int(input("Karekökünü hesaplamak istediğiniz sayı: "))
        print(sayi1, " karekökü = ", sayi1 ** 0.5)
    else:
        print("Yanlış giriş.")
        print("Seçeneklerden birini giriniz.", giris)
    

#FOR LOOP

#example
trHarfler = "şçöğüİı"
for harf in trHarfler:
    print(harf)

#example
sayilar = "123456789"
for i in sayilar:
    if int(i) > 4:
        print(i)

#example
parola = input("Parolanız: ")
for karakter in parola:
    if karakter in trHarfler:
        print("Parolada Türkçe karakter kullanılamaz.")

for i in range(0, 10):
    print(i)

for i in range(100, 105):
    print(i)

for i in range(0, 30, 3):
    print(i)

for i in range(10, 0, -1):
    print(i)

#break, continue and pass
while True:
    sayi = int(input("Bir sayı girin: "))
    if sayi == 0:
        break
    elif sayi == 1:
        continue
        print("Girilen sayı 1'dir.")
    elif sayi < 0:
        pass
    else:
        print("Girilen sayı: ", sayi)
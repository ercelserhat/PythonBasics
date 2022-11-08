ilkSayi = input("İlk sayı: ")
ikinciSayi = input("İkinci sayı: ")

#try...except...
try:
    sayi1 = int(ilkSayi)
    sayi2 = int(ikinciSayi)
    print(sayi1, " / ", sayi2, " = ", sayi1 / sayi2)
except ValueError:
    print("Lütfen sadece sayı girin!")
except ZeroDivisionError as hata:
    print("Bir sayıyı 0'a bölemezsiniz!")
    print("Orijinal hata mesajı: ", hata)
#except (ValueError, ZeroDivisionError):
#    print("Bir hata oluştu")


#try...except...else...
try:
    bolunen = int(input("Bölünecek sayı: "))
    bolen = int(input("Bölen sayı: "))
except ValueError:
    print("Lütfen sadece sayı girin!")
else:
    try:
        print(bolunen / bolen)
    except ZeroDivisionError:
        print("Bir sayıyı 0'a bölemezsiniz!")


#try...except...finally
try:
    sayi1 = int(input("Sayı 1: "))
    sayi2 = int(input("Sayı 2: "))
    print(sayi1 / sayi2)
except (ValueError, ZeroDivisionError) as hata:
    print("Hata oluştu!\Hata mesajı: ", hata)
finally:
    print("Hata olsa da olmasa da burası çalıştı!")


#raise
try:
    sayi1 = int(input("Sayı 1: "))
    if sayi1 == 6:
        raise Exception("Bu programda 6 sayısını görmek istemiyorum!")
    sayi2 = int(input("Sayı 2: "))
    if sayi2 == 7:
        raise TypeError("Raised TypeError")
    print(sayi1 / sayi2)
except (ValueError, ZeroDivisionError) as hata:
    print("Hata oluştu!\Hata mesajı: ", hata)
finally:
    print("Hata olsa da olmasa da burası çalıştı!")


#assert
giris = input("Merhaba! Adın ne?")
assert len(giris) !=0, "İsim bölümü boş."
print("Hoşgeldiniz.")
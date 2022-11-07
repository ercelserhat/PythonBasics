#Example
parola = input("Parola: ")
if parola == "123456":
    print("Giriş başarılı!")

#Example
yas = int(input("Yaşınızı girin: "))
if yas >= 18:
    print("Reşitsiniz.")
elif yas < 18:
    print("Reşit değildiniz.")
elif yas < 0:
    print("Yaş sıfırdan küçük olamaz!")

#Example
meyve = input("Meyve adını girin: ")

if meyve == "elma":
    print("Elma bir meyvedir!")
elif meyve == "çilek":
    print("Çilek bir meyvedir!")
elif meyve == "kiraz":
    print("Kiraz bir meyvedir!")
else:
    print("Böyle bir meyve bulunmamaktadır!")

#Example
username = input("Kullanıcı adı: ")
password = input("Parola: ")

toplamUzunluk = len(username) + len(password)
print("Kullanıcı adı ve parolanız toplam {} karakterden oluşuyor.".format(toplamUzunluk))

if toplamUzunluk > 40:
    print("Kullanıcı adı ve parolanızın toplam uzunluğu 40",
    "karakterden uzun olmamalıdır!")
else:
    print("Sisteme hoşgeldiniz!")
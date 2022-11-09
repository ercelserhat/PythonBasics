import locale
locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254") #Windows için
locale.setlocale(locale.LC_ALL, "tr_TR") #GNU/Linux için

nesne = "12345"
for n in nesne:
    print(int(n) * 2)

print("------------------")

print(nesne[2])
print(nesne[len(nesne)-1])
print(nesne[-1])

print("------------------")

for i in range(len(nesne)):
    print(nesne[i])

print("------------------")

#Karakter Dizilerini Dilimlemek
site = "www.google.com"
site2 = "www.youtube.com"
print(site[4:10]) #google
print(site[0:3]) #www

for isim in site, site2:
    print("Site: ", isim[4:-4]) #Site: google Site:youtube

for isim in site, site2:
    print(isim[0:-4] + ".net") #www.google.net #www.youtube.net

print(site[::-1]) #moc.elgoog.www

sayilar = "123456789123456789"
print(sayilar[0:len(sayilar):2]) #135792468
print(sayilar[::2])              #135792468

for i in reversed("PYTHON"):
    print(i, end="") #NOHTYP

print("\n------------------")

#Karakter Dizilerini Alfabe Sırasına Dizmek
print(sorted("serhat"))

print(*sorted("serhat"))

print(sorted("çiçek", key=locale.strxfrm))

harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
cevrim = {i: harfler.index(i) for i in harfler}
print(sorted("afgdhkıi", key=cevrim.get))

print("------------------")

#Karakter Dizileri Üzerinde Değişiklik Yapmak
isim = "serhat"
isim = "S" + isim[1:]
print(isim)

sesliHarfler = "aeıioöuü"
sessizHarfler = "bcçdfgğhjklmnprsştvyz"
sesliler = ""
sessizler = ""
kelime = input("Kelime giriniz: ")
for i in kelime:
    if i in sesliHarfler:
        sesliler += i 
    else:
        sessizler += i

print("{} kelimesindeki sesli harfler: {}, sessiz harfler: {}".format(kelime, sesliler, sessizler))


#enumerate() metodu
print(*enumerate("serhat"))

for i in enumerate("serhat"):
    print(i)

for index, metod in enumerate(dir("")):
    print(index, metod)

print("------------------")

for index, harf in enumerate("serhat", 1): #numaralandırmaya 1'den başla
    print(index, harf)
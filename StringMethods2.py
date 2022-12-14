#str.maketrans(), translate()
kaynak = "şçöğüıŞÇÖĞÜİ"
hedef  = "scoguiSCOGUI"

ceviriTablosu = str.maketrans(kaynak, hedef)
metin = "Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz."
print(metin.translate(ceviriTablosu)) #Bildiginiz gibi, internet uzerinde bazen Turkce karakterleri kullanamiyoruz.

silinecek = "aeıioöuüAEIİOÖUÜ"
ceviriTablosu = str.maketrans('', '', silinecek)
print(metin.translate(ceviriTablosu)) #Bldğnz gb, ntrnt zrnd bzn Trkç krktrlr kllnmyrz.

isim = "Cem Yılmaz"
kaynak = "CY"
hedef = "cy"
silinecek = "eıa "
ceviriTablosu = str.maketrans(kaynak, hedef, silinecek)
print(isim.translate(ceviriTablosu)) #cmylmz


#isalpha()
s = "serhat"
print(s.isalpha()) #True
s = "s1e2r3h4t"
print(s.isalpha()) #False

#isdigit()
s = "12345"
print(s.isdigit()) #True
s = "ab12345"
print(s.isdigit()) #False

#isalnum()
s = "ab12345"
print(s.isalnum()) #True
s = "*ab12345"
print(s.isalnum()) #False

#isdecimal()
s = "12345"
print(s.isdecimal()) #True
s = "12.345"
print(s.isdecimal()) #False

#isidentifier()
print("1a".isidentifier()) #False
print("a1".isidentifier()) #True 
print("sayi_1".isidentifier()) #True

#isnumeric()
print("12".isnumeric()) #True
print("abc".isnumeric()) #False

#isspace()
print("  ".isspace()) #True
print("          ".isspace()) #True
print("".isspace()) #False
print("   abc   ". isspace()) #False

#isprintable()
print("a".isprintable()) #True
print("\n".isprintable()) #False
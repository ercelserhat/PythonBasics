import locale

for i in range(128):
    if i % 4 == 0:
        print("\n")
    print("{:<3}{:>8}\t".format(i, repr(chr(i))), sep="", end="")


for i in range(1, 5):
    print("{} bayt kullanırsak toplam 2**{:<2} = {:,}".format(i, i*8, (2**(i*8))))

#1 bayt kullanırsak toplam 2**8  = 256
#2 bayt kullanırsak toplam 2**16 = 65,536
#3 bayt kullanırsak toplam 2**24 = 16,777,216
#4 bayt kullanırsak toplam 2**32 = 4,294,967,296


harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
for harf in harfler:
    print("{:<5}{:<15}{:<15}".format(harf, str(harf.encode("utf-8")), len(harf.encode("utf-8"))))


#str1 = "bu Türkçe bir cümledir.".encode("ascii", errors="strict") #UnicodeEncodeError: 'ascii' codec can't encode character '\xfc' in position 4: ordinal not in range(128)

str1 = "bu Türkçe bir cümledir."

print(str1.encode("ascii", errors = "ignore"))  #b'bu Trke bir cmledir.'
print(str1.encode("ascii", errors = "replace")) #b'bu T?rk?e bir c?mledir.'
print(str1.encode("ascii", errors = "xmlcharrefreplace")) #b'bu T&#252;rk&#231;e bir c&#252;mledir.'

print(locale.getpreferredencoding()) #cp1254

f = open("deneme.txt", encoding="cp1254", errors="replace")
print(f.read())


#repr() metodu
print(" Karakter\n")       # Karakter
print(repr(" Karakter\n")) #' Karakter\n'
print(repr("\n")) #'\n'

#ascii() metodu
print(ascii("Text")) #'Text'
print(ascii("İ")) #'\u0130'
print(ascii("€")) #'\u20ac'

#ord() metodu
print(ord("\n")) #10
print(ord("€")) #8364

#chr() metodu
print(chr(100)) #d
print(chr(8364)) #€
#ESKİ YÖNTEM

# %s string, 
# %d decimal
# %i integer
# %o octal 
# %x hexadecimal
# %f float
# %c char

print("%s ve %s iyi bir ikilidir." %("Python", "Django")) #Python ve Django iyi bir ikilidir.

isim = "serhat"
for index, karakter in enumerate(isim, 1):
    print("%s. karakter: '%s'" %(index, karakter))
#1. karakter: 's'
#2. karakter: 'e'
#3. karakter: 'r'
#4. karakter: 'h'
#5. karakter: 'a'
#6. karakter: 't'

print("%%%s" %"50") #%50

for i in dir(str):
    print("->%20s" %i)
#->             __add__
#->           __class__
#->        __contains__
#->         __delattr__
#...

for i in dir(str):
    print("%-20s->" %i)
#__add__             ->
#__class__           ->
#__contains__        ->
#__delattr__         ->
#...

print("Depoda %(miktar)s kilo %(urun)s kaldı." %{"miktar":25, "urun":"elma"}) #Depoda 25 kilo elma kaldı.

print("Bir hafta %d günden oluşur." %7) #Bir hafta 7 günden oluşur.
print("%d" %7.5)    #7
print("|%7d|" %23)  #|     23|
print("|%-7d|" %23) #|23     |
print("%(sayi)d" %{"sayi":23}) #23
print("%.5d" %23) #00023
print("|%10.5d|" %23) #|     00023|

print("%i sayısının sekizli düzendeki karşılığı %o sayısıdır." %(10, 10)) #10 sayısının sekizli düzendeki karşılığı 12 sayısıdır.

print("%i sayısının onaltılı düzendeki karşılığı %x sayısıdır." %(10, 10)) #10 sayısının onaltılı düzendeki karşılığı a sayısıdır.
print("%i sayısının onaltılı düzendeki karşılığı %X sayısıdır." %(10, 10)) #10 sayısının onaltılı düzendeki karşılığı A sayısıdır.
print("%i sayısının onaltılı düzendeki karşılığı %x sayısıdır." %(20, 20)) #20 sayısının onaltılı düzendeki karşılığı 14 sayısıdır.

print("Dolar: %f TL" %18.65) #Dolar: 18.650000 TL
print("Dolar: %.2f TL" %18.65) #Dolar: 18.65 TL

print("%c" %"S") #S
print("%c" %65)  #A

for i in range(128):
    print("%s ==> %c" %(i, i))

for index, karakter in enumerate(dir(str)):
    if index % 3 == 0:
        print("\n", end="")
    print("%-20s" %karakter, end="")

for i in range(20):
    print("%5d%5o%5x" %(i, i, i))

for i in range(20):
    print("%(deger)5d%(deger)5o%(deger)5x" %({"deger":i}))


#YENİ YÖNTEM (Python 3.x)

print("{} ve {} iyi bir ikilidir.".format("Python", "Django")) #Python ve Django iyi bir ikilidir.

isim = input("İsminiz: ")
soyisim = input("Soyisminiz: ")
print("Merhaba {} {}, nasılsın?".format(isim, soyisim)) 
print("Merhaba {0} {1}, nsılsın?".format(isim, soyisim))
print("Merhaba {1} {0}, nasılsın".format(isim, soyisim))
print("{0} {0} {0} {0}".format(isim)) #serhat serhat serhat serhat

print("{dil} dersleri".format(dil="Python")) #Python dersleri

print("|{:>15}|".format("serhat")) #|         serhat|
print("|{:<15}|".format("serhat")) #|serhat         |
print("|{:^15}|".format("serhat")) #|    serhat     |

print("{:s} ve {:s} iyi bir ikilidir.".format("Python", "Django"))
print("{:c}".format(65)) #A
print("{:d}".format(65)) #65
print("{:o}".format(65)) #101
print("{:x}".format(65)) #41
print("{:X}".format(65)) #41
print("{:b}".format(2))  #10
print("{:.2f}".format(50)) #50.00
print("{:,}".format(123456789)) #123,456,789
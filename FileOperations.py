tahsilatDosyasi = open("tahsilat_dosyası.txt", "w")
tahsilatDosyasi.write("Halil Pazarlama: 120.000 TL")
tahsilatDosyasi.close()

fihrist = open("fihrist.txt", "r")
#print(fihrist.read())

#print(fihrist.readline())
#print(fihrist.readline())
#print(fihrist.readline())

print(fihrist.readlines()) #['Ahmet Ã–zbudak : 0533 123 23 34\n', 'Mehmet SÃ¼lÃ¼n  : 0532 212 22 22\n', 'Sami Sam      : 0542 333 34 34']
fihrist.close()


try:
    dosya = open("fihrist.txt", "r")
except IOError:
    print("Bir hata oluştu!")
finally:
    dosya.close()


with open("fihrist.txt", "r") as dosya: #with ile dosya açınca close() ile kapatmaya gerek yoktur, 
    print(dosya.read())                 #Python bizim yerimize dosya kapama işlemini yapacaktır.


myFile = open("fihrist.txt", "r")
print(myFile.read())
print(myFile.read()) #İmleç sona geldiği için artık burada çıktı alamayız. 
myFile.seek(0) #İmleçi 0. bayt konumuna getiriyoruz. 
print(myFile.read()) 
print(myFile.tell()) #Hangi bayt konumunda olduğunu verir. #97
myFile.close()


#Dosyanın sonuna veri eklemek
with open("fihrist.txt", "a") as dosya: #a kipi ile açarak dosya içeriğini silmeden ekleme yapabiliriz.
    dosya.write("\nSelin Özden\t: 0212 222 22 22")

#Dosyanın başına veri eklemek 
with open("fihrist.txt", "r+") as dosya: #r+ -> hem okuma hem yazma kipi
    veri = dosya.read()
    dosya.seek(0) #Dosyayı başa sarıyoruz
    dosya.write("Sedat Köz\t: 0322 234 45 45\n"+veri)

#Dosyanın ortasına veri eklemek
with open("fihrist.txt", "r+") as dosya:
    veri = dosya.readlines()
    veri.insert(14, "Sedat Köz\t: 0322 234 45 45\n")
    dosya.seek(0)
    dosya.writelines(veri)


#DOSYALARIN METOD VE NİTELİKLERİ

#closed
print(dosya.closed) #True

#readable()
f = open("test.txt", "r")
print(f.readable()) #True

#writable()
print(f.writable()) #False

#mode
print(f.mode) #r

#name
print(f.name) #test.txt

#encoding
print(f.encoding) #cp1254

#truncate()
with open("fihrist.txt", "r+") as dosya:
    dosya.readline()
    dosya.seek(f.tell())
    dosya.truncate()
    dosya.truncate(1024*3)



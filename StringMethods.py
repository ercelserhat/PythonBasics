#replace()
s1 = "elma"
print(s1.replace("e", "E")) #Elma

s2 = "memleket"
print(s2.replace("e", "")) #mmlkt
print(s2.replace("e", "", 1)) #mmleket

#split()
s3 = "İstanbul Büyükşehir Belediyesi"
for i in s3.split():
    print(i[0], end="") #İBB

s4 = "Ankara, İstanbul, İzmir, Bursa"
print(s4.split(", "))    #['Ankara', 'İstanbul', 'İzmir', 'Bursa']
print(s4.split(", ", 1)) #['Ankara', 'İstanbul, İzmir, Bursa']

#rsplit()
print(s4.rsplit(", ", 1))#['Ankara, İstanbul, İzmir', 'Bursa']

#splitlines()
s5 = """Birinci satır
İkinci satır
üçüncü satır"""
print(s5.splitlines()) #['Birinci satır', 'İkinci satır', 'üçüncü satır']

#lower()
s6 = "SERHAT"
print(s6.lower()) #serhat

s7 = "ISPARTA, ADIYAMAN, DİYARBAKIR, AYDIN, BALIKESİR, AĞRI"
s7 = s7.replace("I", "ı").replace("İ", "i").lower()
print(s7) #ısparta, adıyaman, diyarbakır, aydın, balıkesir, ağrı

#upper()
s8 = "serhat"
print(s8.upper()) #SERHAT

#islower()
print(s8.islower()) #True
print(s6.islower()) #False

#isupper()
print(s8.isupper()) #False
print(s6.isupper()) #True

#startswith()
s9 = "Python"
print(s9.startswith("P")) #True
print(s9.startswith("Z")) #False

#endswith()
print(s9.endswith("n")) #True
print(s9.endswith("a")) #False

#capitalize()
s10 = "python programming language"
print(s10.capitalize()) #Python programming language

#title()
print(s10.title()) #Python Programming Language

#swapcase()
s11 = "python"
print(s11.swapcase()) #PYTHON
s12 = "PYTHON"
print(s12.swapcase()) #python

#casefold()
print(s12.casefold()) #python

#strip()
s13 = " space "
print(s13.strip()) #space
s14 = "kazak"
print(s14.strip("k")) #aza

#lstrip()
print(s14.lstrip("k")) #azak

#rstrip()
print(s14.rstrip("k")) #kaza

#join()
s15 = "Beşiktaş Jimnastik Kulübü"
bolunmus = s15.split()
print(bolunmus) #['Beşiktaş', 'Jimnastik', 'Kulübü']
birlestirilmis = " ".join(bolunmus)
print(birlestirilmis) #Beşiktaş Jimnastik Kulübü
birlestirilmis = " - ".join(bolunmus)
print(birlestirilmis) #Beşiktaş - Jimnastik - Kulübü

#count()
s16 = "Kahramanmaraş"
print(s16.count("a")) #5

#index()
print(s16.index("a")) #1

#rindex()
print(s16.rindex("a")) #11

#find()
print(s16.find("a")) #1

#rfind()
print(s16.rfind("a")) #11 
#index(), rindex() ile find() rfind() arasındaki fark:
#index(), rindex() karakteri bulamazsa hata verirken
#find(), rfind() karakteri bulamazsa -1 çıktısını verir. 

#center()
s17 = "PYTHON"
print(s17.center(30)) #            PYTHON
print(s17.center(40)) #                 PYTHON
print(s17.center(30, "-")) #------------PYTHON------------
print(s17.center(20, "|")) #|||||||PYTHON|||||||

#rjust()
print(s17.rjust(30)) #                        PYTHON
print(s17.rjust(30, "-")) #------------------------PYTHON

#ljust()
print(s17.ljust(30)) #PYTHON
print(s17.ljust(30, "-")) #PYTHON------------------------

for i in "elma", "armut", "patlıcan":
    print(i.ljust(10, "."))
#elma......
#armut.....
#patlıcan..

#zfill()
s18 = "6"
print(s18.zfill(2)) #06
print(s18.zfill(5)) #00006

#encode()
s19 = "çilek"
print(s19.encode("cp1254")) #b'\xe7ilek'

#expandtabs()
s20 = "Elma\tbir\tmeyvedir"
print(s20)                #Elma    bir     meyvedir
print(s20.expandtabs(20)) #Elma                bir                 meyvedir
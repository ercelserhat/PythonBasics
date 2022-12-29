sozluk = {}
print(type(sozluk)) #<class 'dict'>

sozluk = {"kitap" : "book", "bilgisayar" : "computer", "dil" : "language"}
print(sozluk["bilgisayar"]) #computer

for i in sozluk:
    print(sozluk[i])


telefonDefteri = {
    "ahmet öz" : "0532 532 32 32",
    "mehmet su": "0533 533 33 33",
    "seda naz" : "0534 534 34 34",
    "eda ala"  : "0535 535 35 35"
}
kisi = input("Telefon numarasını öğrenmek istediğiniz kişi: ")
if kisi in telefonDefteri:
    cevap = "{} adlı kişinin telefon numarası: {}"
    print(cevap.format(kisi, telefonDefteri[kisi]))
else:
    print("Aradığınız kişi telefon defterinde yok.")


sozluk =  {"sıfır":0, "bir":1, "iki":2, "üç":3}

sozluk = {
    "Ahmet Özkoparan" : ["İstanbul", "Öğretmen", 34],
    "Mehmet Yağız" : ["Adana", "Mühendis", 40],
    "Eda Bayrak" : ["Mersin", "Doktor", 30]
}
print(sozluk["Eda Bayrak"]) #['Mersin', 'Doktor', 30]

kisiler = {
    "Ahmet Özkoparan":{
        "Memleket":"İstanbul",
        "Meslek":"Öğretmen",
        "Yaş":34
    },
    "Mehmet Yağız":{
        "Memleket":"Adana", 
        "Meslek": "Mühendis",
        "Yaş":40
    },
    "Eda Bayrak":{
        "Memleket":"Mersin",
        "Meslek":"Doktor",
        "Yaş":30
    }
}

print(kisiler["Mehmet Yağız"]["Memleket"]) #Adana
print(kisiler["Eda Bayrak"]["Yaş"]) #30
print(kisiler["Ahmet Özkoparan"]["Meslek"]) #Öğretmen

notlar = {}
notlar["Ahmet"] = 30
notlar["Mehmet"] = 40
notlar["Ali"] = 50
notlar["Veli"] = 60
print(notlar) #{'Ahmet': 30, 'Mehmet': 40, 'Ali': 50, 'Veli': 60}
notlar["Veli"] = 100
print(notlar) #{'Ahmet': 30, 'Mehmet': 40, 'Ali': 50, 'Veli': 100}


#Sözlük Üreteçleri (Dictionary Comprehensions)

#Örnek-1
harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'

#1
sozluk = {}
for i in harfler:
    sozluk[i] = harfler.index(i)
print(sozluk)

#2
sozluk = {}
for i in range(len(harfler)):
    sozluk[harfler[i]] = i
print(sozluk)

#3-With Dictionary Comprehensions
sozluk = {i: harfler.index(i) for i in harfler}
print(sozluk)

#Örnek-2
isimler = ["ahmet", "mehmet", "ali", "veli", "ayşe", "fatma", "abdullah"]
sozluk = {i: len(i) for i in isimler}
print(sozluk) #{'ahmet': 5, 'mehmet': 6, 'ali': 3, 'veli': 4, 'ayşe': 4, 'fatma': 5, 'abdullah': 8}


#Sözlüklerin Metodları

#keys()
print(sozluk.keys()) #dict_keys(['ahmet', 'mehmet', 'ali', 'veli', 'ayşe', 'fatma', 'abdullah'])

liste = list(sozluk.keys())
print(liste) #['ahmet', 'mehmet', 'ali', 'veli', 'ayşe', 'fatma', 'abdullah']
demet = tuple(sozluk.keys())
print(demet) #('ahmet', 'mehmet', 'ali', 'veli', 'ayşe', 'fatma', 'abdullah')
karakterDizisi = ", ".join(sozluk.keys())
print(karakterDizisi) #ahmet, mehmet, ali, veli, ayşe, fatma, abdullah


#values()
print(sozluk.values()) #dict_values([5, 6, 3, 4, 4, 5, 8])

liste = list(sozluk.values())
print(liste) #[5, 6, 3, 4, 4, 5, 8]
demet = tuple(sozluk.values())
print(demet) #(5, 6, 3, 4, 4, 5, 8)
karakterDizisi = ", ".join([str(i) for i in sozluk.values()])
print(karakterDizisi) #5, 6, 3, 4, 4, 5, 8


#items()
print(sozluk.items()) #dict_items([('ahmet', 5), ('mehmet', 6), ('ali', 3), ('veli', 4), ('ayşe', 4), ('fatma', 5), ('abdullah', 8)])

for anahtar, deger in sozluk.items():
    print("{} = {}".format(anahtar, deger))

#ahmet = 5
#mehmet = 6
#ali = 3


#get()
ingSozluk = {"dil": "language", "bilgisayar": "computer", "masa": "table"}
sorgu = input("Anlamını öğrenmek istediğiniz kelimeyi yazınız: ")
print(ingSozluk.get(sorgu, "Bu kelime veritabanımızda yoktur!"))

sorgu = input("Şehrinizin adını giriniz: ")
havaDurumu = {
    "istanbul": "gök gürültülü ve sağanak yağışlı",
    "ankara": "açık ve güneşli",
    "izmir": "bulutlu"
    }
print(havaDurumu.get(sorgu, "Bu şehre ilişkin havadurumu bilgisi bulunamadı."))


#clear()
print(sozluk) #{'ahmet': 5, 'mehmet': 6, 'ali': 3, 'veli': 4, 'ayşe': 4, 'fatma': 5, 'abdullah': 8}
sozluk.clear()
print(sozluk) #{}
del sozluk
#print(sozluk) #NameError: name 'sozluk' is not defined


#copy()
yeniHavaDurumu = havaDurumu
print(havaDurumu)       #{'istanbul': 'gök gürültülü ve sağanak yağışlı', 'ankara': 'açık ve güneşli', 'izmir': 'bulutlu'}
print(yeniHavaDurumu)   #{'istanbul': 'gök gürültülü ve sağanak yağışlı', 'ankara': 'açık ve güneşli', 'izmir': 'bulutlu'}
yeniHavaDurumu["Mersin"] = "sisli"
print(havaDurumu)       #{'istanbul': 'gök gürültülü ve sağanak yağışlı', 'ankara': 'açık ve güneşli', 'izmir': 'bulutlu', 'Mersin': 'sisli'}
print(yeniHavaDurumu)   #{'istanbul': 'gök gürültülü ve sağanak yağışlı', 'ankara': 'açık ve güneşli', 'izmir': 'bulutlu', 'Mersin': 'sisli'}

yeniHavaDurumu = havaDurumu.copy()
print(yeniHavaDurumu)   #{'istanbul': 'gök gürültülü ve sağanak yağışlı', 'ankara': 'açık ve güneşli', 'izmir': 'bulutlu', 'Mersin': 'sisli'}
print(havaDurumu)       #{'istanbul': 'gök gürültülü ve sağanak yağışlı', 'ankara': 'açık ve güneşli', 'izmir': 'bulutlu', 'Mersin': 'sisli'}
yeniHavaDurumu["Zonguldak"] = "karlı"
print(yeniHavaDurumu)   #{'istanbul': 'gök gürültülü ve sağanak yağışlı', 'ankara': 'açık ve güneşli', 'izmir': 'bulutlu', 'Mersin': 'sisli', 'Zonguldak': 'karlı'}
print(havaDurumu)       #{'istanbul': 'gök gürültülü ve sağanak yağışlı', 'ankara': 'açık ve güneşli', 'izmir': 'bulutlu', 'Mersin': 'sisli'}


#fromkeys()
elemanlar = "Ahmet", "Mehmet", "Can"
adresler = dict.fromkeys(elemanlar, "Kadıköy")
print(adresler) #{'Ahmet': 'Kadıköy', 'Mehmet': 'Kadıköy', 'Can': 'Kadıköy'}


#pop()
sepet = {
    "meyveler":("elma", "armut"),
    "sebzeler":("pırasa", "fasulye"),
    "içecekler":("su", "kola", "ayran")
}
print(sepet) #{'meyveler': ('elma', 'armut'), 'sebzeler': ('pırasa', 'fasulye'), 'içecekler': ('su', 'kola', 'ayran')}
print(sepet.pop("meyveler")) #('elma', 'armut')
#sepet.pop("tatlılar") #KeyError: 'tatlılar'
print(sepet.pop("tatlılar", "Böyle bir öğe yok.")) #Böyle bir öğe yok.


#popitem()
print(sepet)            #{'sebzeler': ('pırasa', 'fasulye'), 'içecekler': ('su', 'kola', 'ayran')}
print(sepet.popitem())  #('içecekler', ('su', 'kola', 'ayran'))
print(sepet)            #{'sebzeler': ('pırasa', 'fasulye')}


#setdefault()
sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye")}
sepet.setdefault("içecekler", ("su", "kola"))
print(sepet) #{'meyveler': ('elma', 'armut'), 'sebzeler': ('pırasa', 'fasulye'), 'içecekler': ('su', 'kola')}
sepet.setdefault("meyveler", ("erik", "çilek"))
print(sepet) #{'meyveler': ('elma', 'armut'), 'sebzeler': ('pırasa', 'fasulye'), 'içecekler': ('su', 'kola')}


#update()
stok = {"elma":5, "armut":10, "peynir":6, "sosis":15}
yeniStok = {"elma":3, "armut":20, "peynir":5, "sosis":10}
stok.update(yeniStok)
print(stok) #{'elma': 3, 'armut': 20, 'peynir': 5, 'sosis': 10}

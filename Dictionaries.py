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
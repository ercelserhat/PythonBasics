#LİSTELERİN METODLARI

print([i for i in dir(list) if not "_" in i]) #['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#append()
liste1 = ["elma", "armut", "çilek"]
liste1.append("erik")
print(liste1) #['elma', 'armut', 'çilek', 'erik']

#extend()
liste2 = [1, 2, 3]
liste3 = [4, 5, 6]
liste2.extend(liste3)
print(liste2) #[1, 2, 3, 4, 5, 6]

#insert()
liste4 = ["elma", "armut", "çilek"]
liste4.insert(0, "erik")
print(liste4) #['erik', 'elma', 'armut', 'çilek']

#remove()
liste4.remove("erik")
print(liste4) #['elma', 'armut', 'çilek']

#reverse()
liste5 = [1, 2, 3, 4, 5]
print(liste5[::-1]) #[5, 4, 3, 2, 1]
print(reversed(liste5)) #<list_reverseiterator object at 0x00000211FDF823D0>
print(*reversed(liste5)) #5 4 3 2 1
print(list(reversed(liste5))) #[5, 4, 3, 2, 1]

liste5.reverse()
print(liste5) #[5, 4, 3, 2, 1]

#pop()
print(liste5.pop()) #1
print(liste5.pop(0)) #5

#sort()
liste5.sort()
print(liste5) #[2, 3, 4]

members = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep',
          'Abdullah', 'Kadir', 'Kemal', 'Kamil', 'Selin', 'Senem',
          'Sinem', 'Tayfun', 'Tuna', 'Tolga']
members.sort()
print(members) #['Abdullah', 'Ahmet', 'Ceylan', 'Kadir', 'Kamil', 'Kemal', 'Mahmut', 'Mehmet', 'Selin', 'Senem', 'Seyhan', 'Sinem', 'Tayfun', 'Tolga', 'Tuna', 'Zeynep']

members.sort(reverse=True)
print(members) #['Zeynep', 'Tuna', 'Tolga', 'Tayfun', 'Sinem', 'Seyhan', 'Senem', 'Selin', 'Mehmet', 'Mahmut', 'Kemal', 'Kamil', 'Kadir', 'Ceylan', 'Ahmet', 'Abdullah']


harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
cevrim = {harf: harfler.index(harf) for harf in harfler}
isimler = ["ahmet", "ışık", "ismail", "çiğdem", "can", "şule"]
isimler.sort(key=lambda x: cevrim.get(x[0]))
print(isimler) #['ahmet', 'can', 'çiğdem', 'ışık', 'ismail', 'şule']


#index()
liste6 = ["Ankara", "İstanbul", "İzmir", "Bursa"]
print(liste6.index("İzmir")) #2

#count()
print(liste6.count("Ankara")) #1

#copy()
liste7 = liste6[:]
print(liste7) #['Ankara', 'İstanbul', 'İzmir', 'Bursa']

liste8 = list(liste4)
print(liste8) #['elma', 'armut', 'çilek']

liste9 = liste7.copy()
print(liste9) #['Ankara', 'İstanbul', 'İzmir', 'Bursa']

#clear()
liste9.clear()
print(liste9) #[]


#DEMETLERİN METODLARI

print([i for i in dir(tuple) if not "_" in i]) #['count', 'index']

#index()
demet1 = ("elma", "armut", "çilek", "muz")
print(demet1.index("çilek")) #2

#count()
demet2 = ("elma", "elma", "elma", "çilek", "muz")
print(demet2.count("elma")) #3
print(demet2.count("muz")) #1
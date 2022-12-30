import random

bosKume = set()
print(type(bosKume)) #<class 'set'>

kume = set(["elma", "armut", "çilek"])
print(kume) #{'elma', 'armut', 'çilek'}

kume = set(("elma", "armut", "çilek"))
print(kume) #{'çilek', 'elma', 'armut'}

bilgi = {"işletim sistemi": "GNU", "sistem çekirdeği": "Linux", "dağıtım": "Ubuntu GNU/Linux"}
kume = set(bilgi)
print(kume) #{'dağıtım', 'işletim sistemi', 'sistem çekirdeği'}

kume = {"Python", "Swift", "Kotlin", "Ruby"}
print(kume) #{'Swift', 'Ruby', 'Kotlin', 'Python'}
print(type(kume)) #<class 'set'>

kume = {}
print(type(kume)) #<class 'dict'>

bilgi = {"işletim sistemi": "GNU", "sistem çekirdeği": "Linux", "dağıtım": "Ubuntu GNU/Linux"}
liste = [(anahtar, deger) for anahtar, deger in bilgi.items()]
kume = set(liste)
print(kume) #{('dağıtım', 'Ubuntu GNU/Linux'), ('sistem çekirdeği', 'Linux'), ('işletim sistemi', 'GNU')}

liste = ["elma", "elma", "elma", "armut", "armut", "çilek", "armut", "elma"]
kume = set(liste)
print(kume) #{'elma', 'çilek', 'armut'}

for i in set(liste):
    print("{} listede {} kez geçiyor.".format(i, liste.count(i)))
#çilek listede 1 kez geçiyor.
#elma listede 4 kez geçiyor.
#armut listede 3 kez geçiyor.


#Küme Üreteçleri (Set Comprehensions)

liste = [random.randint(0, 10000) for i in range(1000)]
yuzdenKucukSayilar = {i for i in liste if i < 100}
print(yuzdenKucukSayilar) #{5, 6, 85, 24, 57}


#Kümelerin Metodları
for i in dir(set):
    if "__" not in i:
        print(i)

#clear()
sehir = set("adana")
print(sehir) #{'a', 'n', 'd'}
sehir.clear()
print(sehir) #set()


#copy()
city = set("kahramanmaraş")
sehir = city.copy()
print(sehir) #{'h', 'k', 'a', 'n', 'm', 'r', 'ş'}


#add()
kume = set(["elma", "armut", "çilek"])
kume.add("karpuz")
print(kume) #{'elma', 'çilek', 'armut', 'karpuz'}
kume.add("karpuz")
print(kume) #{'çilek', 'elma', 'karpuz', 'armut'}

sayilar = [1, 2, 3]
for i in sayilar:
    kume.add(i)
print(kume) #{1, 2, 3, 'armut', 'elma', 'karpuz', 'çilek'}


#difference()
k1 = set([1, 2, 3, 5])
k2 = set([3, 4, 2, 10])
print(k1.difference(k2)) #{1, 5}
print(k2.difference(k1)) #{10, 4}


#difference_update()
k1 = set([1, 2, 3])
k2 = set([1, 3, 5])
k1.difference_update(k2)
print(k1)    #{2}
print(k2)    #{1, 3, 5}
print(k1-k2) #{2}


#discard()
hayvanlar = set(["kedi", "köpek", "at", "kuş", "inek", "deve"])
hayvanlar.discard("kedi")
print(hayvanlar) #{'deve', 'kuş', 'köpek', 'inek', 'at'}


#remove()
hayvanlar.remove("köpek")
print(hayvanlar) #{'at', 'deve', 'kuş', 'inek'}


#intersection()
k1 = set([1, 2, 3, 4])
k2 = set([1, 3, 5, 7])
print(k1.intersection(k2)) #{1, 3}
print(k1 & k2) #{1, 3}


#intersection_update()
k1 = set([1, 2, 3])
k2 = set([1, 3, 5])
k1.intersection_update(k2)
print(k1) #{1, 3}
print(k2) #{1, 3, 5}


#isdisjoint() kesişimin boş küme olup olmadığını sorgular.
print(k1.isdisjoint(k2)) #False


#issubset() Bir kümenin bütün elemanlarının başka bir kümede yer alıp almadığını sorgular. 
a = set([1, 2, 3])
b = set([0, 1, 2, 3, 4, 5])
print(a.issubset(b)) #True -> a kümesi b kümesinin alt kümesidir
print(b.issubset(a)) #False -> b kümesi a kümesinin alt kümesi değil


#issuperset()
print(b.issuperset(a)) #True -> b kümesi a kümesini kapsar


#union() 
print(a.union(b)) #{0, 1, 2, 3, 4, 5}
print(a | b)      #{0, 1, 2, 3, 4, 5}


#update()
kume = set(["elma", "armut", "çilek"])
yeni = [1, 2, 3]
kume.update(yeni)
print(kume) #{1, 2, 3, 'armut', 'çilek', 'elma'}


#symmetric_difference()
a = set([1, 2, 5])
b = set([1, 4, 5])
print(a.difference(b)) #{2}
print(b.difference(a)) #{4}
print(a.symmetric_difference(b)) #{2, 4}


#symmetric_difference_update()
print(a) #{1, 2, 5}
a.symmetric_difference_update(b)
print(a) #{2, 4}


#pop()
meyveler = set(["elma", "armut", "çilek"])
print(meyveler.pop()) #çilek


#FROZENSET
#Üzerinde değişiklik yapılmasını istemediğimiz bir küme oluşturmak istiyorsak
#set yerine frozenset'i kullanabiliriz. 

dondurulmusKume = frozenset(["elma", "armut", "çilek"])

#Frozenset Metodları
for i in dir(dondurulmusKume):
    if "__" not in i:
        print(i) #copy difference intersection isdisjoint issubset issuperset symmetric_difference union


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


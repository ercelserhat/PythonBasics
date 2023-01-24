#1- abs()
print(abs(-20)) #20


#2- round()
print(round(12.4)) #12
print(round(12.7)) #13

print(round(22/7)) #3
print(round(22/7, 0)) #3.0
print(round(22/7, 1)) #3.1
print(round(22/7, 2)) #3.14
print(round(22/7, 3)) #3.143


#3- all() 
#Bir dizi içerisindeki tüm değerler True ise True döndürür
liste = [1, 2, 3]
print(all(liste)) #True
liste = [0, 1, 2, 3]
print(all(liste)) #False

a = 3
t1 = a == 3
t2 = a < 4
t3 = a % 2 == 1
print(all([t1, t2, t3])) #True


#4- any()
#Bir dizi içerisindeki değerlerden en az biri True ise True döndürür
liste = ["ahmet", "mehmet", ""]
print(any(liste)) #True

liste = ["", 0, [], (), set(), dict()]
print(any(liste)) #False


#5- ascii()
print(ascii("\n")) #'\n'
print(ascii("ışık")) #'\u0131\u015f\u0131k'


#6- repr()
print(ascii("şeker")) #'\u015feker'
print(repr("şeker")) #'şeker'


#7- bool()
print(bool(0)) #False
print(bool(1)) #True


#8- bin()
print(bin(12)) #0b1100


#9- bytes()
print(bytes(10)) #b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
print(bytes("ışık", "utf-8"))  #b'\xc4\xb1\xc5\x9f\xc4\xb1k'
print(bytes("ışık", "cp1254")) #b'\xfd\xfe\xfdk'
print(bytes("ışık", "cp857"))  #b'\x8d\x9f\x8dk'

print(bytes("şeker", encoding="ascii", errors="replace")) #b'?eker'
print(bytes("şeker", encoding="ascii", errors="ignore")) #b'eker'
print(bytes("şeker", encoding="ascii", errors="xmlcharrefreplace")) #b'&#351;eker'


#10- bytearray()
a = bytearray("adana", "ascii")
print(a) #bytearray(b'adana')
a[0] = 65
print(a) #bytearray(b'Adana')


#11- chr()
print(chr(10)) # '\n'
print(chr(65)) # 'A'
print(chr(305)) # 'ı'


#12- list()
#-Liste tipinde veri oluşturmak için kullanılır
#-Farklı veri tiplerini liste veri tipine dönüştürmek için kullanılır
liste = list()
print(liste) #[]

print(list("serhat")) #['s', 'e', 'r', 'h', 'a', 't']

s = {"elma":44, "armut":10, "erik":200}
print(list(s)) #['elma', 'armut', 'erik']
print(list(s.values())) #[44, 10, 200]


#13- set()
k = set()
print(k) #set()

sehir = "ankara"
print(set(sehir)) #{'a', 'r', 'n', 'k'}


#14- tuple()
print(tuple("serhat")) #('s', 'e', 'r', 'h', 'a', 't')


#15- frozenset()
s = set("serhat")
print(frozenset(s)) #frozenset({'s', 'r', 'a', 't', 'e', 'h'})


#16- complex()
print(complex(15)) #(15+0j)
print(complex(15, 2)) #(15+2j)


#17- float()
print(float("123")) #123.0
print(float(123))   #123.0


#18- int()
print(int("10")) #10
print(int(10.0)) #10
print(int("12", 8)) #10
print(int("4cf", 16)) #1231


#19- str()
print(str(12)) #12

bayt = b"serhat"
metin = str(bayt, encoding="utf-8")
print(metin) #serhat


#20- dict()
s = dict()
print(s) #{}

s = dict(a=1, b=2, c=3)
print(s) #{'a': 1, 'b': 2, 'c': 3}

elemanlar = (["a", 1], ["b", 2], ["c", 3])
print(dict(elemanlar)) #{'a': 1, 'b': 2, 'c': 3}


#21- callable()
print(callable(open)) #True
print(callable(elemanlar)) #False


#22- ord() karakterin karşılık geldiği ondalık sayıyı verir
print(ord("A")) #65
print(ord("ı")) #305


#23- oct() sayının sekizli düzendeki karşılığını verir 
print(oct(10)) #0o12


#24- hex() sayının on altılı düzendeki karşılığını verir 
print(hex(305)) #0x131


#25- copyright()
print(copyright())


#26- credits()
print(credits())
#Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
#for supporting Python development.  See www.python.org for more information.


#27- license()
print(license())


#28- dir()
print(dir()) 
#['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
#'__package__', '__spec__', 'a', 'bayt', 'elemanlar', 'k', 'liste', 'metin', 's', 'sehir', 't1', 't2', 't3']
print(dir(""))
print("------------------------")
print(dir([]))
print("------------------------")
print(dir({}))
print("------------------------")


#29- divmod()
print(divmod(10, 2)) #(5, 0)
print(divmod(10, 3)) #(3, 1)


#30- enumerate()
print(list(enumerate("serhat"))) #[(0, 's'), (1, 'e'), (2, 'r'), (3, 'h'), (4, 'a'), (5, 't')]
print(*enumerate("serhat")) #(0, 's') (1, 'e') (2, 'r') (3, 'h') (4, 'a') (5, 't')

for i in enumerate("serhat"):
    print(i)

for index, eleman in enumerate("serhat", 1):
    print("{}. {:>2}".format(index, eleman))


#31- exit()
#Çalışan programdan çıkmayı sağlar. 


#32- help()
print(help(dir))


#33- id()
a = 50
print(id(a)) #140714918153408

s = "serhat"
print(id(s)) #2920208359024


#34- isinstance()
print(isinstance("serhat", str)) #True
print(isinstance(10, bool)) #False


#35- len()
print(len("serhat")) #6


#36- map()
liste = [1, 4, 5, 4, 2, 9, 10]

def karesi(n):
    return n**2

print(list(map(karesi, liste))) #[1, 16, 25, 16, 4, 81, 100]


#37- max()
print(max(1, 2, 3)) #3
print(max(liste)) #10

def enYuksekRutbe(rutbe):
    rutbeler = {
        'er'        : 0,
        'onbaşı'    : 1,
        'çavuş'     : 2,
        'asteğmen'  : 3,
        'teğmen'    : 4,
        'üsteğmen'  : 5,
        'yüzbaşı'   : 6,
        'binbaşı'   : 7,
        'yarbay'    : 8,
        'albay'     : 9
    }
    return rutbeler[rutbe]

askerler = {
    'ahmet': 'onbaşı',
    'mehmet': 'teğmen',
    'ali': 'yüzbaşı',
    'cevat': 'albay',
    'berkay': 'üsteğmen',
    'mahmut': 'binbaşı'
}

print(max(askerler.values(), key=enYuksekRutbe)) #albay

for k, v in askerler.items():
    if askerler[k] in max(askerler.values(), key=enYuksekRutbe):
        print(v, k) #albay cevat


#38- min() 
#max() fonksiyonunun tam tersini yapar. Kullanımı aynıdır.


#39- pow()
print(pow(2, 3)) #8
print(pow(2, 3, 2)) #0 #(2**3)%2


#40- quit()


#41- range() #range(başlangıç_değeri, bitiş_değeri, atlama_değeri)
liste = range(0, 10)
print(liste) #range(0, 10)
print(type(liste)) #<class 'range'>
print(list(liste)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(tuple(liste)) #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(set(liste)) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

for i in range(10):
    print(i)

print(*range(10), sep=", ") #0, 1, 2, 3, 4, 5, 6, 7, 8, 9

print(list(range(0, 10, 2))) #[0, 2, 4, 6, 8]


#42- reversed()
isimler = ["ahmet", "mehmet", "veli", "ayşe", "çiğdem", "ışık"]
print(isimler[::-1]) #['ışık', 'çiğdem', 'ayşe', 'veli', 'mehmet', 'ahmet']
print(reversed(isimler)) #<list_reverseiterator object at 0x0000018CE94522B0>
print(list(reversed(isimler))) #['ışık', 'çiğdem', 'ayşe', 'veli', 'mehmet', 'ahmet']


#43- sorted()
print(sorted("serhat")) #['a', 'e', 'h', 'r', 's', 't']

#44- slice() #slice(başlangıç, bitiş, atlama)
liste = ["ahmet", "mehmet", "ayşe", "senem", "salih"]
print(liste[0:2]) #['ahmet', 'mehmet']
print(liste[:2])  #['ahmet', 'mehmet']
print(liste[1:])  #['mehmet', 'ayşe', 'senem', 'salih']
print(liste[::2]) #['ahmet', 'ayşe', 'salih']

dl = slice(0, 3)
print(liste[dl]) #['ahmet', 'mehmet', 'ayşe']


#44- sum()
liste = [1, 2, 3]
print(sum(liste)) #6
print(sum(liste, 10)) #16


#45- type()
print(type("elma")) #<class 'str'>


#46- zip()
a1 = ['a', 'b', 'c']
a2 = ['d', 'e', 'f']

print(zip(a1, a2)) #<zip object at 0x00000293B5DFC480>
print(*zip(a1, a2)) #('a', 'd') ('b', 'e') ('c', 'f')
print(list(zip(a1, a2))) #[('a', 'd'), ('b', 'e'), ('c', 'f')]

for a, b in zip(a1, a2):
    print(a, b)

isimler = ["ahmet", "mehmet", "zeynep", "ilker"]
yaslar = [24, 40, 35, 20]
for i, y in zip(isimler, yaslar):
    print("İsim: {} - Yaş: {}".format(i, y))
#İsim: ahmet - Yaş: 24
#İsim: mehmet - Yaş: 40
#İsim: zeynep - Yaş: 35
#İsim: ilker - Yaş: 20


#47- vars()
print(vars())
print(vars(str))
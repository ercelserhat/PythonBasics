#Example-1
def myGenerator():
    yield "Merhaba"
    yield "Dünya"

g = myGenerator()
print(next(g)) #Merhaba
print(next(g)) #Dünya
#print(next(g)) #StopIteration Error


#Example-2
def fibonacci():
    x = 1
    y = 0
    z = 0
    while True:
        z = y 
        y = x
        x = y + z
        yield x

f = fibonacci()
print(next(f)) #1
print(next(f)) #2
print(next(f)) #3
print(next(f)) #5
print(next(f)) #8
print(next(f)) #13
        

#Example-3
def fibonacci2():
    x = 1
    y = 0
    z = 0
    while not x > 100:
        z = y 
        y = x 
        x = y + z 
        yield x

for i in fibonacci2():
    print(i)
#1
#2
#3
#5
#8
#13
#21
#34
#55
#89
#144

#yield from example
def generator1():
    yield "Üreteç1 başladı."
    yield "Üreteç1 bitti."

def generator2():
    yield "Üreteç2 başladı."
    yield from generator1()
    yield "Üreteç2 bitti."

for i in generator2():
    print(i)

#Üreteç2 başladı.
#Üreteç1 başladı.
#Üreteç1 bitti.
#Üreteç2 bitti.


#LIST GENERATORS
myList = [i for i in range(10)]
print(myList) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def listGenerator():
    for i in range(3):
        yield i 

listGen = listGenerator()
myList = list(listGen)
print(myList) #[0, 1, 2]


#DICTIONARY GENERATORS
dictGen = ((str(i), i) for i in range(3))
myDict = {}
for key, value in dictGen:
    myDict[key] = value

print(myDict) #{'0': 0, '1': 1, '2': 2}
tamSayi = 3
noktaliSayi = 4.5
karmasikSayi = 6+3j

print(tamSayi, noktaliSayi, karmasikSayi) #3 4.5 (6+3j)

#INTEGER
print([i for i in dir(int) if not i.startswith("_")]) 
#['as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

for i in range(11):
    print(i, bin(i)[2:], len(bin(i)[2:]), sep="\t")

sayi = 10
print(sayi.bit_length()) #4
print((2).bit_length()) #2

#FLOAT
print([i for i in dir(float) if not i.startswith("_")])
#['as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']

#as_integer_ratio() metodu birbirine bölündüğünde kalan noktalı sayıyı veren iki adat tam sayıyı verir.
sayi2 = 4.5
print(sayi2.as_integer_ratio()) #(9, 2)

#is_integer() metodu kayan noktalı sayının ondalık kısmında 0 harici rakamın olup olmadığını kontrol eder.
print((12.0).is_integer()) #True
print((12.23).is_integer()) #False

#COMPLEX
print([i for i in dir(complex) if not i.startswith("_")]) #['conjugate', 'imag', 'real']

#imag niteliği karmaşık sayının sanal kısmını verir. 
sayi3 = 12+4j
print(sayi3.imag) #4.0

#real niteliği karmaşık sayının gerçek kısmını verir. 
print(sayi3.real) #12.0

#ARİTMETİK FONKSİYONLAR

#abs() - Bir sayının mutlak değerini verir. 
print(abs(-2)) #2

#divmod() - Bir sayının bir sayıya bölünmesi işleminde bölüm ve kalanı verir.
print(divmod(10, 2)) #(5, 0)

#max()
sayilar = [666182, 516933, 22222, 445705, 589281]
print(max(sayilar)) #666182

isimler = ["ahmet", "mehmet", "necla", "sedat", "abdullah"]
print(max(isimler, key=len)) #abdullah

#min()
print(min(sayilar)) #22222
print(min(isimler, key=len)) #ahmet

#sum()
toplanacakSayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(toplanacakSayilar)) #45

print(sum(toplanacakSayilar, 10)) #55
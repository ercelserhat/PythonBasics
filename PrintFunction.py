print("Hello World")

print('Hello World')

print("""Hello
Python
World""")

print("Python", "Programlama", "Dili", 2022)

#SEP PARAMETRESİ
print("Python", "Programlama", "Dili", 2022, sep=" - ")

#END PARAMETRESİ
print("Python", "Programlama", "Dili", 2022, end=" *** ")

#FILE PARAMETRESİ
dosya = open("python.txt", "w")
print("Python", "Programlama", "Dili", 2022, file = dosya)
dosya.close()

print(*"Python", sep = "-")


#ESCAPE SEQUENCES

#  \’ Karakter dizisi içinde tek tırnak işaretini kullanabilmemizi sağlar.
#  \” Karakter dizisi içinde çift tırnak işaretini kullanabilmemizi sağlar.
#  \\ Karakter dizisi içinde \ işaretini kullanabilmemizi sağlar.
#  \n Yeni bir satıra geçmemizi sağlar.
#  \t Karakterler arasında sekme boşluğu bırakmamızı sağlar.
#  \u UNICODE kod konumlarını gösterebilmemizi sağlar.
#  \U UNICODE kod konumlarını gösterebilmemizi sağlar.
#  \N Karakterleri UNICODE adlarına göre kullanabilmemizi sağlar.
#  \x Onaltılı sistemdeki bir sayının karakter karşılığını gösterebilmemizi sağlar.
#  \a Destekleyen sistemlerde, kasa hoparlöründen bir ‘bip’ sesi verilmesini sağlar.
#  \r Aynı satırın başına dönülmesini sağlar.
#  \v Destekleyen sistemlerde düşey sekme oluşturulmasını sağlar.
#  \b İmlecin sola doğru kaydırılmasını sağlar
#  \f Yeni bir sayfaya geçilmesini sağlar.
#  r Karakter dizisi içinde kaçış dizilerini kullanabilmemizi sağlar.,

print('Ankara\'nın havası')
print("Satır 1\nSatır 2\nSatır 3") 
print("Bir\tİki\tÜç") 
print("\a") 
print("Merhaba \rDünya") 
print("Merhaba \vDünya") 
print("yahoo.com\b.uk") 
print(r"C:\Program Files\Adobe") 
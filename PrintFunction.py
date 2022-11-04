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

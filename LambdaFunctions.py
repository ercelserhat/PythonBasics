fonk = lambda param1, param2 : param1 + param2
print(fonk(2, 4)) #6

ciftMi = lambda sayi: sayi % 2 == 0
print(ciftMi(2)) #True
print(ciftMi(3)) #False

liste = [2, 5, 10, 23, 3, 6]
for i in liste:
    print(i**2)

print([i**2 for i in liste]) #[4, 25, 100, 529, 9, 36]

def karesi(sayi):
    return sayi**2
print(*map(karesi, liste)) #4 25 100 529 9 36

print(*map(lambda sayi: sayi**2, liste)) #4 25 100 529 9 36


birlestir = lambda ifade, birlestirici: birlestirici.join(ifade.split())
print(birlestir("Ankara Büyükşehir Belediyesi", "-")) #Ankara-Büyükşehir-Belediyesi


import tkinter
import tkinter.ttk as ttk
pen = tkinter.Tk()
btn = ttk.Button(text="merhaba", command=lambda: print("merhaba"))
btn.pack(padx=210, pady=210)
pen.mainloop()
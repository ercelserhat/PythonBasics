import time
import random
import sys 

class Oyuncu():
    def __init__(self, isim, can=5, enerji=100):
        self.isim = isim
        self.darbe = 0
        self.can = can
        self.enerji = enerji

    def mevcutDurumuGoruntule(self):
        print("Darbe\t: ", self.darbe)
        print("Can\t: ", self.can)
        print("Enerji\t: ", self.enerji)

    def saldir(self, rakip):
        print("Bir saldırı gerçekleştirdiniz.")
        print("Saldırı sürüyor. Bekleyiniz.")

        for i in range(10):
            time.sleep(.3)
            print(".", end="", flush=True)
        
        sonuc = self.saldiriSonucunuHesapla()

        if sonuc == 0:
            print("\n>>>>>>>>>>SONUÇ: Kazanan Taraf Yok!\n-------------------------")
        if sonuc == 1:
            print("\n>>>>>>>>>>SONUÇ: Rakibinizi Darbelediniz!\n-------------------------")
            self.darbele(rakip)
        if sonuc == 2:
            print("\n>>>>>>>>>>SONUÇ: Rakibinizden Darbe Aldınız!\n-------------------------")
            rakip.darbele(self)

    def saldiriSonucunuHesapla(self):
        return random.randint(0, 2)

    def darbele(self, darbelenen):
        darbelenen.darbe += 1
        darbelenen.enerji -=1
        if(darbelenen.darbe % 5) == 0:
            darbelenen.can -= 1
        if darbelenen.can < 1:
            darbelenen.enerji = 0
            print("OYUNU {} KAZANDI!".format(self.isim))
            self.oyundanCik()

    def kac(self):
        print("Kaçılıyor...")
        for i in range(10):
            time.sleep(.3)
            print("\n", flush=True)
        print("Rakibiniz sizi yakaladı!")

    def oyundanCik(self):
        print("Çıkılıyor...")
        sys.exit()


siz = Oyuncu("Serhat")
rakip = Oyuncu("Mehmet")

while True:
    print("\n\nŞu anda rakiple karşı karşıyasınız.",
    "Yapmak istediğiniz hamle:",
    "Saldır\t: S",
    "Kaç\t: K",
    "Çık\t: Q", sep="\n")

    hamle = input("\n> ").lower()
    if hamle == "s":
        siz.saldir(rakip)
        print("\nRakibinizin Durumu:\n-------------------------")
        rakip.mevcutDurumuGoruntule()
        print("\nSizin Durumunuz:\n-------------------------")
        siz.mevcutDurumuGoruntule()
    
    if hamle == "k":
        siz.kac()
    
    if hamle == "q":
        siz.oyundanCik()

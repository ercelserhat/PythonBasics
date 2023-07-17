class Calisan():
    personel = []

    def __init__(self, isim):
        self.isim = isim
        self.kabiliyetler = []
        self.personelEkle()
    
    def personelEkle(self):
        self.personel.append(self.isim)
        print("{} adlı kişi personele eklendi.".format(self.isim))

    @classmethod
    def personelGoruntule(cls):
        print("Personel Listesi:")
        for kisi in cls.personel:
            print(kisi)
    
    @classmethod
    def personelSayisiniGoruntule(cls):
        print(len(cls.personel))

    def kabiliyetEkle(self, kabiliyet):
        self.kabiliyetler.append(kabiliyet)

    def kabiliyetleriGoruntule(self):
        print("{} adlı kişinin kabiliyetleri: ".format(self.isim))
        for kabiliyet in self.kabiliyetler:
            print(kabiliyet)



class HarfSayaci:
    def __init__(self):
        self.sesliHarfler = "aeıioöuü"
        self.sessizHarfler = "bcçdfgğhjklmnprsştvyz"
        self.sayacSesli = 0
        self.sayacSessiz = 0
    
    def kelimeSor(self):
        return input("Bir kelime girin: ")
    
    def seslidir(self, harf):
        return harf in self.sesliHarfler
    
    def sessizdir(self, harf):
        return harf in self.sessizHarfler
    
    def arttir(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayacSesli += 1
            if self.sessizdir(harf):
                self.sayacSessiz += 1
        return (self.sayacSesli, self.sayacSessiz)

    def ekranaBas(self):
        sesli, sessiz = self.arttir()
        mesaj = "{} kelimesinde {} sesli, {} sessiz harf var."
        print(mesaj.format(self.kelime, sesli, sessiz))

    def calistir(self):
        self.kelime = self.kelimeSor()
        self.ekranaBas()

if __name__ == "__main__":
    sayac = HarfSayaci()
    sayac.calistir()
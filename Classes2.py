class Calisan():
    #Private members
    __personel = []

    def __init__(self, isim):
        self.isim = isim
        self.kabiliyetleri = []
        self.__personele_ekle()

    @classmethod
    def personel_sayisini_goruntule(cls):
        print(len(cls.__personel))

    #Private members
    def __personele_ekle(self):
        self.__personel.append(self.isim)
        print('{} adlı kişi personele eklendi'.format(self.isim))

    def personeli_goruntule(self):
        print('Personel Listesi:')
        for kisi in self.__personel:
            print(kisi)

    def kabiliyet_ekle(self, kabiliyet):
        self.kabiliyetleri.append(kabiliyet)

    def kabiliyetleri_goruntule(self):
        print('{} adlı kişinin kabiliyetleri: '.format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)
        
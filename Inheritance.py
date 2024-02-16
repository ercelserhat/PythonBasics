class Oyuncu():
    def __init__(self, isim, rutbe):
        self.isim = isim
        self.rutbe = rutbe
        self.guc = 0

    def hareket_et(self):
        print("Hareket ediliyor...")

    def puan_kazan(self):
        print("Puan kazanıldı...")

    def puan_kaybet(self):
        print("Puan kaybedildi...")

class Asker(Oyuncu):
    def __init__(self, isim, rutbe):
        super().__init__(isim, rutbe)
        self.guc = 100

class Isci(Oyuncu):
    def __init__(self, isim, rutbe):
        super().__init__(isim, rutbe)
        self.guc = 70

class Yonetici(Oyuncu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.guc = 50

    def hareket_et(self):
        super().hareket_et()
        print("Hedefe ulaşıldı...")
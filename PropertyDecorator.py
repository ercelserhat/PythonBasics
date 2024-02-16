class Program():
    def __init__(self):
        self._sayi = 0

    @property
    def sayi(self):
        return self._sayi
    
    @sayi.setter
    def sayi(self, yeni_deger):
        self._sayi = yeni_deger
        return self._sayi
    

p = Program()
print(p.sayi)   # 0

p.sayi = 5
print(p.sayi)   # 0
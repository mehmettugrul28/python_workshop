class Calisan:
    
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim 
        self.maas = maas
        self.email = isim + soyisim + "@sirket.com"


    def bilgileri_goster(self):
        return "Ad: {} , Soyad: {} , Maas: {} , Email: {}".format(self.isim , self.soyisim,self.maas , self.email)


class Yazilimci(Calisan):
    def __init__(self, isim, soyisim, maas , bildigiDil):
        super().__init__(isim , soyisim , maas)
        self.bildigiDil = bildigiDil
    def bilgileri_goster(self):
        return  "Ad: {} , Soyad: {} , Maas: {} , Email: {} , Bildiği dil: {} ".format(self.isim , self.soyisim,self.maas , self.email , self.bildigiDil)
    
    def diliniSoyle(self):
        return f"Dil: {self.bildigiDil}"

class Yonetici(Calisan):
   def __init__(self, isim, soyisim, maas , calisanlar = None):
       super().__init__(isim, soyisim, maas)
       if calisanlar == None:
         self.calisanlar = []
       else:
        self.calisanlar.calisanlar
   def calisanEkle(self , calisan):
    pass


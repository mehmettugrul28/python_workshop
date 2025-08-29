class Calisan:
    
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim 
        self.maas = maas
        self.email = isim + soyisim + "@sirket.com"


    def bilgileri_goster(self):
        return "Ad: {} , Soyad: {} , Maas: {} , Email: {}".format(self.isim , self.soyisim,self.maas , self.email)

calisan1 = Calisan("Ahmet" , "Dede" , 5000)

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
        self.calisanlar = calisanlar
   def calisanEkle(self , calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)

   def calisanSil(self , calisan):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)
   def calisanlariGoster(self):
        for calisan in self.calisanlar:
            print(calisan.bilgileri_goster())

calisan1 = Calisan("Ahmet" , "Dede" , 5000)
yazilimci1 = Yazilimci("Şevket" , "Sivri" , 6000 , "Python")

yonetici1 = Yonetici("Metin" , "Durmuş" , 10000)
yonetici1.calisanEkle(calisan1)
yonetici1.calisanEkle(yazilimci1)
yonetici1.calisanlariGoster()

print("************")

yonetici1.calisanSil(calisan1)
yonetici1.calisanlariGoster()

print(isinstance(yazilimci1 , Calisan)) #? yazilimci1 Calisan dan mı geldi(True)





class Person:
    def __init__(self, isim, yas, cinsiyet, boy, agirlik):
        self.isim = isim
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.boy = boy
        self.agirlik = agirlik

isim = input("İsminiz nedir?: ")
yas = int(input("Yaşınız kaç?: "))
cinsiyet = input("Cinsiyetiniz nedir?: ")
boy = int(input("Boy uzunluğunuz nedir?: "))
agirlik = int(input("Ağırlığınız kaç kg?: "))

kisi = Person(isim, yas, cinsiyet, boy, agirlik)

print("\nKişi Bilgileri:")
print(f"İsim: {kisi.isim}")
print(f"Yaş: {kisi.yas}")
print(f"Cinsiyet: {kisi.cinsiyet}")
print(f"Boy: {kisi.boy} cm")
print(f"Ağırlık: {kisi.agirlik} kg\n")
print("Kayıt açma işleminiz başarıyla tamamlandı :)")
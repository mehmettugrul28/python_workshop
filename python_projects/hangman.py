print("Tahmin etmeniz gerekn kelime ya meyvedir ya da ülke.")
import random

random_letters = ["Almanya", "Amerika", "Belçika", "Bulgaristan", "Danimarka", "Türkiye", "Hindistan" , "Venezuela"]
random_letters2 = ["Elma", "Muz", "Çilek", "Portakal", "Üzüm", "Ananas", "Karpuz", "Şeftali", "Kiraz", "Mango"]

bilgisayar_secim = random.choice(random_letters).strip().lower()
bilgisayar_secim = random.choice(random_letters2).strip().lower()
kalan_hak = 5  
tahmin_edilenler = list()
guncel_kelime = ["_"] * len(bilgisayar_secim)

print("Adam asmaca oyununa hoşgeldiniz. Seçilen kelimeler ya ülkedir ya da meyvedir.")
print(" ".join(guncel_kelime))

while True:
    
    if bilgisayar_secim in random_letters :
        print("Seçim ülkeler arasında yapılmıştır.")
    else:
        print("Seçim meyveler arasnında yapıldı.")    
        
    tahmin = input("Harf tahmini yapın: ").lower()
    
    if tahmin in tahmin_edilenler:
        print("Bu harfi daha önceden tahmin ettin")
    elif tahmin in bilgisayar_secim:
        print("Tebrikler, doğru tahmin")
        tahmin_edilenler.append(tahmin)
        
        for i in range(len(bilgisayar_secim)):
            if bilgisayar_secim[i] == tahmin:
                guncel_kelime[i] = tahmin
        
        print(" ".join(guncel_kelime))
    else:
        kalan_hak -= 1
        print(f"Yanlış tahmin. Kalan hak: {kalan_hak}")
        tahmin_edilenler.append(tahmin)
        print(" ".join(guncel_kelime))
    
    if kalan_hak == 0:
        print("Kaybettin maalesef. Tuttuğum kelime:", bilgisayar_secim)
        break
    
    if "_" not in guncel_kelime:
        print(f"Bravo, tuttuğum kelimeyi bildin! Doğru kelime: {bilgisayar_secim}")
        break

print("Tahmin edilen harfler:", ", ".join(tahmin_edilenler))

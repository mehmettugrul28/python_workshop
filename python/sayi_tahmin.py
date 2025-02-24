print("Hangi sayılar arasında tahmin yapmak istediğinizi girin")

import random
istenilen_tahmin1 = int(input("İlk sayıyı giriniz: "))
istenilen_tahmin2 = int(input("İkinci sayıyı giriniz: "))


if istenilen_tahmin2 > istenilen_tahmin1:
    x = random.randint(istenilen_tahmin1,istenilen_tahmin2)
else:
    x = random.randint(istenilen_tahmin2,istenilen_tahmin1)


sayi = 0
kac_kez = 0


while x != sayi:
    sayi = int(input("Sayı giriniz: "))
    print(sayi,end=' girdin.')
    if sayi>x:
        print("Daha küçük bir sayı giriniz.")
        kac_kez += 1
    elif sayi<x:
        print("Daha büyük bir sayı giriniz.")
        kac_kez += 1
    else:
        print("Başardınız!")
        kac_kez += 1
else:
    print("\n",kac_kez," kerede bildin")
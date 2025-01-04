import random
x = random.randint(1,10)
sayi = 0
kac_kez = 0


while x != sayi:
    sayi = int(input("Sayı giriniz: "))
    print(sayi,end=' girdin.')
    if sayi>x:
        print("Daha küçük bir sayı giriniz.")
    elif sayi<x:
        print("Daha büyük bir sayı giriniz.")
    else:
        print("Başardınız!")
        kac_kez += 1
else:
    print("\n",kac_kez," kerede bildin")
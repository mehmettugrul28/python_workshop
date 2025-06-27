import random
soru = int(input("Kaç atışta gelen zar olasılığını hesaplamak istersiniz?: "))

zarlar = {1:0 , 2:0 , 3:0 , 4:0 , 5:0 , 6:0}

for i in range(soru):
    zar = random.randint(1 , 6)
    zarlar[zar] += 1

for zar in zarlar:
    print(f"{zar} gelme olasılığı -> {zarlar[zar] / soru}") 
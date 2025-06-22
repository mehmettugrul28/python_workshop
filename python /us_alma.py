taban = int(input("Üssünü almak istediğiniz sayının tabanını giriniz: "))
us = int(input("Tabanını girdiğiniz sayının üssünü giriniz: "))

sonuc = taban

for i in range(us - 1):
    sonuc *= taban

print(f"{taban}^{us} = {sonuc}")

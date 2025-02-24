print("Asal sayılar sadece kendine ve 1' e bölünebile sayılardır")

def asal_mi(sayi):
    if sayi < 2:
        return False, []
    
    carpanlar = []
    carpanlar.append(1)
    carpanlar.append(sayi)

    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            carpanlar.append(i)
            if sayi // i != i:
                carpanlar.append(sayi // i)
    
    if len(carpanlar) > 2:  # Eğer çarpanlar listesi 2'den fazla eleman içeriyorsa, sayı asal değildir.
        return False, sorted(carpanlar)
    
    return True, []

while True:
    sayi = int(input("Asal olup olmadığını öğrenmek istediğiniz sayıyı girin:\n "))

    asal, carpanlar = asal_mi(sayi)
    
    if asal:
        print(f"{sayi} sayısı bir asal sayıdır.")
    else:
        print(f"{sayi} sayısı asal değildir.")
        print(f"{sayi} sayısının çarpanları -> {carpanlar}")
        
    tekrar = input("Yeniden sormak ister misiniz[e/h]: ").strip().lower()

    if tekrar == "e":
        continue
    else:
        print("Çıkış yapılıyor...")
        break

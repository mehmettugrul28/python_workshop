import math

def karekok_hesapla(sayi):
    if sayi < 0:
        return "Negatif sayının karekökü hesaplanamaz."
    return math.sqrt(sayi)

while True:
    sayi = float(input("Karekökünü almak istediğiniz bir sayı girin: "))
    print("Karekökü:", karekok_hesapla(sayi))
    
    tekrar = input("Başka bir sayı girmek ister misiniz? (e/h): ").strip().lower()
    if tekrar != 'e':
        break

print("Program sonlandı.")
  
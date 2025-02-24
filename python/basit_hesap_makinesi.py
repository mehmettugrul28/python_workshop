
def topla(sayi1 , sayi2):
    return sayi1 + sayi2

def cikar(sayi1 , sayi2):
    return sayi1 + sayi2

def carp(sayi1 , sayi2):
    return sayi1 * sayi2

def bol(sayi1 , sayi2):
    if sayi2 != 0:
        return sayi1 / sayi2
    else:
        return "Hata , hiçbir sayı 0'a bölünemez!"
    
while True:
    islem = input("Yapmak istediğiniz işlemi giriniz , çıkmak için 'a' giriniz: ")
    
    if islem == 'a':
        break
    
    sayi1 = int(input("İlk sayıyı giriniz: "))
    sayi2 = int(input("İkinci sayıyı giriniz: "))
    
    
    if islem == '+':
        sonuc = (topla(sayi1 , sayi2))

    elif islem == '-':
     sonuc = (cikar(sayi1 , sayi2))

    elif islem == '*':
        sonuc = (carp(sayi1 , sayi2))

    elif islem == '/':
        sonuc = (bol(sayi1 , sayi2)) 

    else:
        print("Geçersiz işlem")
    
    print(sonuc)   
    
    devam = input("Yeniden işlem yapmak ister misiniz[e/h]:").strip().lower()
    
    if devam != 'h':
        continue
    else:
        print("Programdan çıkış yapıldı...")
        break
    
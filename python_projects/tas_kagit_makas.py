import random

print("Lütfen sadece taş, makas veya kağıt yazın !!")

def tas_kagit_makas():
    kullanici_skor = 0
    bilgisayar_skor = 0
    secenekler = ["taş", "kağıt", "makas"]
    
    while True:
        kullanici_cevap = input("Taş mı, kağıt mı, makas mı? ").lower()
        
        
        while kullanici_cevap not in secenekler:
            kullanici_cevap = input("Lütfen sadece taş, makas veya kağıt yazın: ").lower()
        
        bilgisayar_cevap = random.choice(secenekler)
        
        if kullanici_cevap == bilgisayar_cevap:
            print(f"Berabere kaldık maalesef, gel bir daha. Benim cevabım şuydu: {bilgisayar_cevap}")
        elif (kullanici_cevap == "taş" and bilgisayar_cevap == "makas") or \
             (kullanici_cevap == "makas" and bilgisayar_cevap == "kağıt") or \
             (kullanici_cevap == "kağıt" and bilgisayar_cevap == "taş"):
            print(f"Tebrikler, bu turu sen kazandın. Benim cevabım: {bilgisayar_cevap}")
            kullanici_skor += 1
        else:
            print(f"Üzgünüm, bu turu ben kazandım. Benim cevabım: {bilgisayar_cevap}")
            bilgisayar_skor += 1
        
        print(f"Kullanıcının skoru: {kullanici_skor} - Bilgisayar skoru: {bilgisayar_skor}")
        if kullanici_skor == 5:
            print("Tebrikler, beni yendin. :((")
            break
        elif bilgisayar_skor == 5:
            print("Üzgünüm canım ezdim seni :)) ")
            break

tas_kagit_makas()

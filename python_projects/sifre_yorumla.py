def puanlandir(sifre):
    min_karakter_sayisi = 4
    puan = 0
    buyuk_harfler = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z']
    rakamlar = ['1', '2' , '3' , '4' ,'5' , '6' ,'7' ,'8' ,'9' ,'0']
    farkli_isaretler = ['/','#','!','?','*','(',')','@' ]
    if(len(sifre) >= min_karakter_sayisi ):
        puan += 1
    for karakter in sifre:
        if karakter in buyuk_harfler:
            puan += 1
            break
    for karakter in sifre:
        if karakter in rakamlar:  
            puan += 2
            break
    for karakter in sifre:
        if karakter in farkli_isaretler:
            puan += 3
            break
    return puan
        

sifre = input("Şifrenizi giriniz: ")
puan = puanlandir(sifre)
print("Puanınız: " , puan)

if puan <= 2:
    print("Şifreniz geçersiz, şifreniz değiştirin.")
elif puan <= 4  :
    print("Şifreniz geçerli.")
else:
    print("Şifreniz gerçekten güçlü")
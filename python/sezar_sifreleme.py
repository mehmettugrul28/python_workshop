print("Bu program ile sezar şifreleme yapabilirsiniz.")

def sezar_sifrele(metin, anahtar):
    alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    sifreli_metin = ""
    for karakter in metin:
        if not karakter in alfabe:
            sifreli_metin += " "
            continue
        index = alfabe.index(karakter)
        sifreli_metin += alfabe[(index + anahtar)%len(alfabe)]
    return sifreli_metin
orjinal_metin = input("Şifrelencek metninizi giriniz: ").lower()
anahtar = int(input("Kaç karakter ilerleyerek şifrelenmesini istiyorsunuz?:"))
sifreli_metin = sezar_sifrele(orjinal_metin , anahtar)
print(sifreli_metin)
print("Orjinal metin: " + orjinal_metin + "\n Şifreli metin:"+ sifreli_metin )
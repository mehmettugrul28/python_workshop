bakiye = 0

while True:
    print("""
1) Bakiyemi göster
2) Para çek
3) Para yatır
4) Sistemden çıkış
    """)

    secim = input("Seçiminiz: ")

    if secim == "1":
        print(f"Bakiyeniz : {bakiye}TL")
        print("----------------------------")

    elif secim == "2":
        paraCek = int(input("Kaç para çekmek istersiniz: "))
        if paraCek > bakiye:
            print("Bakiyeniz bu parayı çekmek için yeterli değil.")
            print("----------------------------")
        else:
            bakiye -= paraCek
            print(f"Paranız çekildi. Mevcut bakiyeniz: {bakiye}")
            print("----------------------------")

    elif secim == "3":
        paraYatir = int(input("Kaç para yatırmak istersiniz: "))
        bakiye += paraYatir
        print(f"Paranız yatırıldı. Mevcut bakiyeniz: {bakiye}")
        print("----------------------------")

    elif secim == "4":
        print("Çıkış yaplıyor...")
        break

    else:
        print("Geçersiz işlem , sistemden atıldınız")
        break
    

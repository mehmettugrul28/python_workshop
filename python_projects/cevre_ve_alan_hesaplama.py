print("Bu program ile herhangi bir şeklin çevre uzunluğunu veya alanını hesaplayabilirsiniz\n")

while True:
    sekil = int(input("""Hangi şeklin çevre uzunluğunu veya alanını hesaplamak istersiniz (lütfen yazarken harf hatası yapmayınız ve şeklin numarasını giriniz!):
1-) Kare
2-) Dikdörtgen
3-) Üçgen 
4-) Paralelkenar: """))  

    cevap = input("Çevre mi hesaplamak istersiniz alan mı?[a/ç]: ").strip().lower()

    if sekil == 2:
        kisa_kenar = int(input("Şeklin kısa kenar uzunluğunu giriniz: "))
        uzun_kenar = int(input("Şeklin uzun kenar uzunluğunu giriniz: "))
        if kisa_kenar > uzun_kenar:
            print("Ben hayatımda uzun kenarın kısa kenardan uzun olduğunu görmedim :D")
        if cevap == "a":
            print(f"Şeklin alanı = {kisa_kenar * uzun_kenar}")
        elif cevap == "ç":
            print(f"Şeklin çevre uzunluğu = {(kisa_kenar + uzun_kenar) * 2}")
        else:
            print("Hatalı giriş yaptınız!")

    elif sekil == 1:
        kenar = int(input("Karenin bir kenar uzunluğunu giriniz: "))
        if cevap == "a":
            print(f"Şeklin alanı = {kenar ** 2}")
        elif cevap == "ç":
            print(f"Şeklin çevre uzunluğu = {kenar * 4}")
        else:
            print("Hatalı giriş yaptınız!")

    elif sekil == 3:
        kenar1 = int(input("Üçgenin birinci kenar uzunluğunu giriniz: "))
        kenar2 = int(input("Üçgenin ikinci kenar uzunluğunu giriniz: "))
        kenar3 = int(input("Üçgenin üçüncü kenar uzunluğunu giriniz: "))
        if cevap == "ç":
            print(f"Üçgenin çevre uzunluğu = {kenar1 + kenar2 + kenar3}")
        else:
            print("Alan hesaplaması için üçgenin yüksekliği eklenmeli. Şu anda desteklenmiyor.")

    elif sekil == 4:
        taban = int(input("Paralelkenarın taban uzunluğunu giriniz: "))
        yukseklik = int(input("Paralelkenarın yüksekliğini giriniz: "))
        kenar = int(input("Paralelkenarın diğer kenar uzunluğunu giriniz: "))
        if cevap == "a":
            print(f"Paralelkenarın alanı = {taban * yukseklik}")
        elif cevap == "ç":
            print(f"Paralelkenarın çevre uzunluğu = {(taban + kenar) * 2}")
        else:
            print("Hatalı giriş yaptınız!")

    else:
        print("Yanlış giriş yaptınız!")
        continue

    yeniden = input("Başka bir işlem yapmak ister misiniz? [e/h]: ").strip().lower()
    if yeniden != "e":
        print("Programdan çıkılıyor. İyi günler!")
        break

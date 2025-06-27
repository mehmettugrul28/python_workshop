import random

kelimeler = ["motive", "ilham", "sezgi", "çelişki", "denge", "öngörü", "sükunet", "aidiyet", "dürtü", "anlam", "empati", "tutarlılık", "merak", "beklenti", "bilinç", "umut", "içgörü", "sezmek", "yöntem", "algı"]

while True:
    secilen_kelime = random.choice(kelimeler)
    karisik_kelime = " ".join(random.sample(secilen_kelime, len(secilen_kelime)))

    print(f"Karışık kelime: {karisik_kelime}")
    print("Kelimeyi tahmin edin (çıkmak için 'q' yazın):")

    while True:
        tahmin = input("Tahmininiz: ").lower()  

        if tahmin == 'q':
            print("Oyundan çıkılıyor...")
            break

        if tahmin == secilen_kelime:
            print(f"Tebrikler! Doğru tahmin: {secilen_kelime}")
            break
        else:
            print("Yanlış tahmin, tekrar deneyin.")

    cevap = input("Başka bir kelime tahmin etmek ister misiniz? (e/h): ").lower()
    if cevap == 'h':
        print("Oyundan çıkılıyor...")
        break
    elif cevap != 'e':
        print("Geçersiz cevap, oyundan çıkılıyor...")
        break
import random

secim = input("Yazı mı tura mı?(y/t): ").lower().strip()

sonuc = random.choice(["y" , "t"]).lower().strip()

skor = 0
while True:

    sonuc = random.choice(["y" , "t"]).lower().strip()
    if secim == sonuc:
        print("Bravo! Doğru bildin.")
        skor += 1  
        print(f"Güncel skorunuz => {skor}")

    else:
        print("Üzgünüm bilemedin")
        print(f"Güncel skorunuz =>  {skor}")

    cevap = input("Yeniden devam etmek ister misiniz? (e/h): ").lower().strip()

    if cevap == "e":
        secim = input("Yazı mı tura mı?(y/t): ").lower().strip()
    elif cevap == "h":
        print("İyi günler dileriz.")
        print(f"Güncel skorunuz => {skor}")
        break
    else:
        print("Geçersiz cevap")
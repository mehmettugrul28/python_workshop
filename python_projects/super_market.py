class Urun:
    def __init__(self, isim, fiyat, stok, birim="adet"):
        self.isim = isim
        self.fiyat = fiyat
        self.stok = stok
        self.birim = birim

    def __str__(self):
        return f"{self.isim} -> Fiyat: {self.fiyat} TL/{self.birim}, Stok: {self.stok} {self.birim}"

class Reyon:
    def __init__(self, isim):
        self.isim = isim  
        self.urunler = []

    def urun_ekle(self, urun):
        self.urunler.append(urun)

    def urunleri_goster(self):
        print(f"{self.isim} Reyonu Ürünleri:")
        for i, urun in enumerate(self.urunler, 1):
            print(f"{i}. {urun}")

class Market:
    def __init__(self, isim):
        self.isim = isim
        self.reyonlar = []
        self.sepet = []

    def reyon_ekle(self, reyon):
        self.reyonlar.append(reyon)

    def reyon_goster(self):
        print(f"{self.isim} Market Reyonları:")
        for i, reyon in enumerate(self.reyonlar, 1):
            print(f"{i}. {reyon.isim}")

    def reyon_sec(self, reyon_adi):
        for reyon in self.reyonlar:
            if reyon.isim.lower() == reyon_adi.lower().strip():
                return reyon
        return None

    def sepete_ekle(self, urun, miktar):
        self.sepet.append((urun, miktar))

    def toplam_fiyat(self):
        return sum(urun.fiyat * miktar for urun, miktar in self.sepet)

    def sepeti_goster(self):
        print("Sepetinizdeki Ürünler:")
        for urun, miktar in self.sepet:
            print(f"{miktar} {urun.birim} {urun.isim} -> Toplam: {urun.fiyat * miktar} TL")
        print(f"Toplam Fiyat: {self.toplam_fiyat()} TL")

# Ürün oluşturma
elma = Urun("Elma", 15, 300, "kg")
muz = Urun("Muz", 25, 200, "kg")
portakal = Urun("Portakal", 20, 245, "kg")
uzum = Urun("Üzüm", 27, 198, "kg")
armut = Urun("Armut", 17, 234, "kg")

dana_kıyma = Urun("Dana kıyma", 500, 450, "kg")
kuzu_pirzola = Urun("Kuzu pirzola", 515, 398, "kg")
tavuk_gogsu = Urun("Tavuk göğsü", 587, 453, "kg")
sucuk = Urun("Sucuk", 60, 650, "adet")
salam = Urun("Salam", 26, 700, "adet")

sut = Urun("Süt", 14, 245, "L")
yogurt = Urun("Yoğurt", 26, 246, "kg")
peynir = Urun("Peynir", 27, 217, "kg")
tereyagi = Urun("Tereyağı", 300, 287, "kg")
ayran = Urun("Ayran", 18, 187, "L")

su = Urun("Su", 10, 400, "adet")
gazli_icecek = Urun("Gazlı içecek", 21, 160, "adet")
meyve_suyu = Urun("Meyve suyu", 18, 165, "adet")
enerji_icecegi = Urun("Enerji içeceği", 42, 100, "adet")
soda = Urun("Soda", 11, 170, "adet")

deterjan = Urun("Toz deterjan", 94, 230, "kg")
camasir_suyu = Urun("Çamaşır suyu", 79, 240, "L")
bulasik_deterjani = Urun("Bulaşık deterjanı", 83, 215, "L")
temizlik_bezi = Urun("Temizlik bezi", 28, 198, "adet")
yuzey_temizleyici = Urun("Yüzey temizleyici", 36, 200, "adet")

cips = Urun("Cips", 30, 190, "adet")
cikolata = Urun("Toblerone çikolata", 25, 180, "adet")
kraker = Urun("Çubuk kraker", 16, 178, "adet")
kuruyemis = Urun("Karışık kuruyemiş", 126, 210, "kg")
biskuvi = Urun("Bisküvi", 19, 165, "adet")

un = Urun("Un", 27, 140, "kg")
makarna = Urun("Makarna", 47, 215, "kg")
ekmek = Urun("Ekmek", 7, 270, "adet")
kek = Urun("Kek", 64, 90, "adet")
simit = Urun("Simit", 5, 78, "adet")

sampuan = Urun("Şampuan", 43, 140, "adet")
dis_macunu = Urun("Diş macunu", 38, 139, "adet")
sabun = Urun("Sabun", 23, 134, "adet")
dedorant = Urun("Deodorant", 123, 189, "adet")
tiras_kopugu = Urun("Tıraş köpüğü", 68, 110, "adet")

# Reyonları oluşturma
meyve_reyonu = Reyon("Meyve")
meyve_reyonu.urun_ekle(elma)
meyve_reyonu.urun_ekle(muz)
meyve_reyonu.urun_ekle(portakal)
meyve_reyonu.urun_ekle(uzum)
meyve_reyonu.urun_ekle(armut)

et_reyonu = Reyon("Et ve Et Ürünleri")
et_reyonu.urun_ekle(dana_kıyma)
et_reyonu.urun_ekle(kuzu_pirzola)
et_reyonu.urun_ekle(tavuk_gogsu)
et_reyonu.urun_ekle(sucuk)
et_reyonu.urun_ekle(salam)

sut_reyonu = Reyon("Süt ve Süt Ürünleri")
sut_reyonu.urun_ekle(sut)
sut_reyonu.urun_ekle(yogurt)
sut_reyonu.urun_ekle(peynir)
sut_reyonu.urun_ekle(tereyagi)
sut_reyonu.urun_ekle(ayran)

icecek_reyonu = Reyon("Içecekler")
icecek_reyonu.urun_ekle(su)
icecek_reyonu.urun_ekle(gazli_icecek)
icecek_reyonu.urun_ekle(meyve_suyu)
icecek_reyonu.urun_ekle(enerji_icecegi)
icecek_reyonu.urun_ekle(soda)

temizlik_reyonu = Reyon("Temizlik Ürünleri")
temizlik_reyonu.urun_ekle(deterjan)
temizlik_reyonu.urun_ekle(camasir_suyu)
temizlik_reyonu.urun_ekle(bulasik_deterjani)
temizlik_reyonu.urun_ekle(temizlik_bezi)
temizlik_reyonu.urun_ekle(yuzey_temizleyici)

atistirmalik_reyonu = Reyon("Atıştırmalıklar")
atistirmalik_reyonu.urun_ekle(cips)
atistirmalik_reyonu.urun_ekle(cikolata)
atistirmalik_reyonu.urun_ekle(kraker)
atistirmalik_reyonu.urun_ekle(kuruyemis)
atistirmalik_reyonu.urun_ekle(biskuvi)

un_mamulleri_reyonu = Reyon("Un Mamulleri")
un_mamulleri_reyonu.urun_ekle(un)
un_mamulleri_reyonu.urun_ekle(makarna)
un_mamulleri_reyonu.urun_ekle(ekmek)
un_mamulleri_reyonu.urun_ekle(kek)
un_mamulleri_reyonu.urun_ekle(simit)

kisisel_bakim_reyonu = Reyon("Kişisel Bakım Ürünleri")
kisisel_bakim_reyonu.urun_ekle(sampuan)
kisisel_bakim_reyonu.urun_ekle(dis_macunu)
kisisel_bakim_reyonu.urun_ekle(sabun)
kisisel_bakim_reyonu.urun_ekle(dedorant)
kisisel_bakim_reyonu.urun_ekle(tiras_kopugu)

# Marketi oluşturma
market = Market("Alpaş")
market.reyon_ekle(meyve_reyonu)
market.reyon_ekle(et_reyonu)
market.reyon_ekle(sut_reyonu)
market.reyon_ekle(icecek_reyonu)
market.reyon_ekle(temizlik_reyonu)
market.reyon_ekle(atistirmalik_reyonu)
market.reyon_ekle(un_mamulleri_reyonu)
market.reyon_ekle(kisisel_bakim_reyonu)

# Marketin işleyişi
while True:
    market.reyon_goster()
    secilen_reyon_adi = input("Hangi reyondan alışveriş yapmak istersiniz? (Çıkmak için 'çıkış' yazın): ").strip().lower()

    if secilen_reyon_adi == "çıkış":
        print("")
        break

    secilen_reyon = market.reyon_sec(secilen_reyon_adi)

    if secilen_reyon:
        while True:
            secilen_reyon.urunleri_goster()
            urun_no = input("Bir ürün seçin (ürün numarasını girin) veya çıkmak için 'çıkış' yazın: ").strip().lower()

            if urun_no == "çıkış":
                break

            try:
                urun_no = int(urun_no)
                if 1 <= urun_no <= len(secilen_reyon.urunler):
                    secilen_urun = secilen_reyon.urunler[urun_no - 1]
                    miktar = input(f"Kaç {secilen_urun.birim} almak istersiniz? (Çıkmak için 'çıkış' yazın): ").strip().lower()

                    if miktar == "çıkış":
                        break

                    try:
                        miktar = float(miktar)
                        if miktar <= secilen_urun.stok:
                            secilen_urun.stok -= miktar
                            market.sepete_ekle(secilen_urun, miktar)
                            print(f"{miktar} {secilen_urun.birim} {secilen_urun.isim} satın aldınız.")
                        else:
                            print("Üzgünüz, yeterli stok bulunmamaktadır.")
                    except ValueError:
                        print("Geçersiz giriş. Lütfen miktarı sayı olarak girin.")
                else:
                    print("Geçersiz ürün numarası.")
            except ValueError:
                print("Geçersiz giriş. Lütfen geçerli bir numara girin.")
    else:
        print("Geçersiz reyon adı. Lütfen listeden bir reyon seçin.")
   
def urun_cikar(market):
    
    if not market.sepet:
        print("Sepetinizde ürün yok.")
        return

    while True:
        urun_no = input("Çıkarmak istediğiniz ürünün numarasını giriniz [yukarısı 1](Çıkmak için 'çıkış' yazın): ").strip().lower()
        if urun_no == "çıkış":
            break

        try:
            urun_no = int(urun_no)
            if 1 <= urun_no <= len(market.sepet):
                secilen_urun, secilen_miktar = market.sepet[urun_no - 1]
                miktar = input(f"Kaç {secilen_urun.birim} {secilen_urun.isim} çıkarmak istersiniz? (Çıkmak için 'çıkış' yazın): ").strip().lower()

                if miktar == "çıkış":
                    break

                try:
                    miktar = float(miktar)
                    if miktar <= secilen_miktar:
                        secilen_urun.stok += miktar
                        if miktar == secilen_miktar:
                            market.sepet.pop(urun_no - 1)
                        else:
                            market.sepet[urun_no - 1] = (secilen_urun, secilen_miktar - miktar)
                        print(f"{miktar} {secilen_urun.birim} {secilen_urun.isim} sepetten çıkarıldı.")
                    else:
                        print(f"Sepette bu üründen sadece {secilen_miktar} {secilen_urun.birim} mevcut.")
                except ValueError:
                    print("Geçersiz giriş. Lütfen miktarı sayı olarak girin.")
            else:
                print("Lütfen geçerli ürün numarası girin.")
        except ValueError:
            print("Lütfen geçerli bir numara girin.")

def odeme_al(market):
    toplam_tutar = market.toplam_fiyat()
    kalan_tutar = toplam_tutar
    print(f"Lütfen ödenecek tutarı giriniz -> {toplam_tutar} TL:")

    while kalan_tutar > 0:  
        try:
            odeme = float(input("Ödeme miktarınızı girin: "))
            if odeme < kalan_tutar:
                kalan_tutar -= odeme
                print(f"Ödediğiniz miktar eksik. Lütfen şu kadar daha ödeyin -> {kalan_tutar} TL")
            elif odeme > kalan_tutar:
                print(f"Ödemeniz toplam tutardan fazla. Para üstünüz: {odeme - kalan_tutar} TL. İyi günler dileriz, yine bekleriz :D")
                kalan_tutar = 0  
            else:
                print("Ödemeniz başarıyla alınmıştır. İyi günler dileriz, yine bekleriz :)")
                kalan_tutar = 0  
        except ValueError:
            print("Geçersiz giriş yapıldı. Lütfen geçerli bir miktar girin.")
        

market.sepeti_goster()
urun_cikar(market)
odeme_al(market)
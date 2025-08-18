with open("mini_project.txt" , "r") as dosya:
    with open("gecenler.txt" , "r+") as gecenler:
        with open("kalanlar.txt" , "r+") as kalanlar:
            icerik = dosya.readlines()
            atla = 0
            for satir in icerik:
                if atla == 0:
                    atla += 1
                    continue
                satir = satir.replace("\n" , "")

                bosluk_sayisi = 0
                bosluk_indexleri = []
                index = 0
                for karakter in satir:
                    if karakter == " ":
                        bosluk_sayisi += 1 
                        bosluk_indexleri.append(index)
                    index += 1
                isim_soyisim = satir[:bosluk_indexleri[0]]
                soyisim = isim_soyisim.split("-")[-1]
                isim = isim_soyisim[:isim_soyisim.index(soyisim) - 1].replace("-" , " ")
                
                
                notlar = satir.strip().split(" ")[-1]
                notlar = notlar.split("/") 
                birini_vize = int(notlar[0])
                ikinci_vize = int(notlar[1])
                final = int(notlar[2])
                ortalama = birini_vize * 0.3 + ikinci_vize * 0.3 + final * 0.4

                alan = satir[bosluk_indexleri[0] + 1:bosluk_indexleri[len(bosluk_indexleri) - 1]]
                
               
                if ortalama >= 70 and final >= 70:
                    gecenler.write(isim)
                    gecenler.write(" " * (25 - len(isim)))
                    gecenler.write(soyisim)
                    gecenler.write(" " * (25 - len(soyisim)))
                    gecenler.write(alan)
                    gecenler.write(" " * (25 - len(alan)))
                    gecenler.write(str(round(ortalama , 1)))
                    gecenler.write(" " * 21)
                    gecenler.write("Geçti")
                    gecenler.write("\n")


                else:
                    kalanlar.write(isim)
                    kalanlar.write(" " * (25 - len(isim)))
                    kalanlar.write(soyisim)
                    kalanlar.write(" " * (25 - len(soyisim)))
                    kalanlar.write(alan)
                    kalanlar.write(" " * (25 - len(alan)))
                    kalanlar.write(str(round(ortalama , 1)))
                    kalanlar.write(" " * 20)
                    kalanlar.write("Geçti")
                    kalanlar.write("\n")


not1=int(input("1. Notunuzu Giriniz:"))
not2=int(input("2. Notunuzu Giriniz:"))
not3=int(input("3. Notunuzu Giriniz:"))

ortalama=(not1 + not2 + not3)/3

print("Not Ortalamanız:",ortalama)

if ortalama>70:
    print("Dersten Geçtiniz :)")
elif ortalama<70:
    print("Dersten Kaldınız :(")  
else:
    print("Bütünlemeye Kaldınız :|")
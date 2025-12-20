def hesaplamlar(x):
    def kareAl(a):
        return a**2
    def karekokAl(a):
        return a**0.5
    def faktoriyelAl(a):
        carpim = 1
        for i in range(1 , a + 1):
            carpim *= i
        return carpim

    kare = kareAl(x)
    karekok = karekokAl(x)
    faktoriyel = faktoriyelAl(x)
    return f" Karesi: {kare}\n Karekökü: {karekok}\n Faktoriyeli: {faktoriyel}"

print(hesaplamlar(6))
print("***************")

def toplamCarpim(*args):
    def toplama(demet):
        return sum(demet)
    def carpma(demet):
        carpim = 1
        for i in demet:
            carpim *= i
        return carpim
    return f"Toplamları: {toplama(args)} , Çarpım: {carpma(args)}"

print(toplamCarpim(2,4,6))
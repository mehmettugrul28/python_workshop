

class MyList(list):
    def __add__(self , other): #! TOPLAMA
        if len(self) != len(other):
            return "Eleman sayısı eşit olmadığı için toplanamaz"
        else:
            result = MyList()
            for i in range(len(other)):
                result.append(self[i] + other[i])
        return result

    def __sub__(self , other): #! ÇIKARMA
        if len(self) != len(other):
            return "Eleman sayısı eşit olmadığı için çıkarılamaz"
        else:
            result = MyList()
            for i in range(len(other)):
                result.append(self[i] - other[i])
        return result

    def __eq__(self, other): #!EŞİTLİK KONTROLÜ
        if sum(self) == sum(other):
            return True 
        return False

    def __abs__(self):  #! MUTLAK DEĞER 
        result = MyList()
        for i in self:
            if i >= 0:
                result.append(i)
            else:
                result.append(-1 * i)

        return result



liste1 = MyList([1,-2,3])
liste2 = MyList([-4,-5,-6])

print(liste1 + liste2)
print(liste1 - liste2)
print(liste1 == liste2)
print(abs(liste1))
print(abs(liste2))



class Futbolcu:
    def __init__(self,isim,soyisim,yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas

    def __eq__(self,other):
        if self.isim == other.isim and self.soyisim == other.soyisim and self.yas == other.yas:
            return True
        return False

    def __add__(self,other):
        isim = self.isim[0] + other.isim[0]
        soyisim = self.soyisim[0] + other.soyisim[0]
        yas = self.yas + other.yas
        return Futbolcu(isim , soyisim , yas)

    def __lt__(self,other):
        if self.yas < other.yas:
            return True
        return False

    def __gt__(self,other):
        if self.yas > other.yas:
            return True
        return False


futbolcu1 = Futbolcu("Ali" , "Veli" , 25)
futbolcu2 = Futbolcu("Hakan" , "Çalışkan" , 30)

print(futbolcu1 == futbolcu2)

futbolcu3 = futbolcu1+futbolcu2
print(futbolcu2 > futbolcu1)
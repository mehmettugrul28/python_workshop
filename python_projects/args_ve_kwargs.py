def topla(*args):
    for arg in args:
        print(arg)



def carp(*args):
    carpim = 1
    for arg in args:
        carpim *= arg
    return carpim
    
# print(carp(5,6))

def ortalama(*args):
    return sum(args) / len(args)

# print(ortalama(6,4))

def selamla(mesaj , *args):
    selam = ""
    selam += mesaj
    selam += " "
    for arg in args:
        selam += arg
        selam += " "
    return selam

# print(selamla("Merhaba" , "Nasılsın"))

def fonk(**kwargs):
    print(kwargs)

fonk(ad = "Ali" , soyad = "Çalışkan") #? istediğimiz sayıda keyword argument girebiliriz


def fonk2(zorunlu , *args , **kwargs):
    print(zorunlu)
    print("*********")
    for arg in args:
        print(arg)
    print("**********")
    for key,value in kwargs.items():
        print(key , "->" , value)

fonk2(2,3,4,5,6,7 , ad = "Ali" , soyad = "Çalışkan" , yas = 25)



#! fonksiyonları yazarken * dan sonra ne geldiği önemli değildir isimler yazılımcı tarafından belirlerinir.
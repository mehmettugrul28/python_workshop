from datetime import date
class Person:
    
    kisi_sayisi = 0
    def __init__(self , name , age):
        self.name = name
        self.age = age
        Person.kisi_sayisi += 1


    def showInfo(self):
        return f"Ad: {self.name} Yaş: {self.age}"

    @classmethod
    def numberOfpeople(cls):
        return cls.kisi_sayisi
    
    @classmethod
    def stringİleolustur(cls , str_):
        name,age = str_.split("-")
        return cls(name,age)
    @classmethod
    def dogumYiliİleolustur(cls , name , dogum_yili):
        return cls(name , date.today().year - dogum_yili)

person1 = Person("Ali" , 20)
person2 = Person("Veli" , 30)
person3 = Person.stringİleolustur("Ayşe-25")
person4 = Person.dogumYiliİleolustur("Elif" , 1990)
print(Person.numberOfpeople())
print(person4.name , person4.age)
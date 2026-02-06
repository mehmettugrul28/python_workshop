class Footballer: 
    def __init__(self , name , surname , age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"Name: {self.name} , Surname: {self.surname} , Age: {self.age}"

    def __repr__(self):
        return "repr çalışıyor"
        

footballer1 = Footballer("Ali" , "Veli" , 20) 
print(footballer1) #python nesneyi tanıyamadı class ' ın içinde de __str__ bulamadı ve sonuç: <__main__.Footballer object at 0x1038de900>
print(footballer1.__repr__()) #repr kullanılmak isterse ayrıca belirtilmeli çünkü öncelik str
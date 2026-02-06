class Worker:
    zam_orani = 1.3
    def __init__(self , name , surname , salary ):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.email = name + surname + "@company.com"

    
    def showInfo(self):
        return f"Name: {self.name} , Surname: {self.surname} , Salary: {self.salary} , Email: {self.email}"

worker1 = Worker("Ali" , "Çalışkan" , 5000 )
worker2 = Worker("Veli" , "Uzun" , 6000 )

class Programmer(Worker):
    zam_orani = 1.2
    def __init__(self, name, surname, salary , knownLanguage):
        super().__init__(name , surname , salary)
        self.knownLanguage = knownLanguage
    
    def showInfo(self):
        return f"Name: {self.name} , Surname: {self.surname} , Salary: {self.salary} , Email: {self.email} , Known Language: {self.knownLanguage}"
      

programmer1 = Programmer("Ayşe" , "Yıldız" , 7000 , "Python")
programmer2 = Programmer("Fatma" , "Ay" , 8000 , "Javascript")

class Manager(Worker):

    def __init__(self, name, surname, salary , workers = None):
        super().__init__(name, surname, salary)
        if workers == None:
            self.workers = []
        else:
            self.workers = workers

    def addWorker(self , worker):
        if worker not in self.workers:
            self.workers.append(worker)

    def deleteWorker(self , worker):
        if worker in self.workers:
            self.workers.remove(worker)

    def showWorkers(self):
        for worker in self.workers:
            print(worker.showInfo())

manager1 = Manager("Metin" , "Ali" , 10000)         

manager1.addWorker(worker1)
manager1.addWorker(programmer1)
manager1.deleteWorker(worker1)



manager2 = Manager("Feyyaz" , "Beşiktaş" , 11000 , [programmer1 , programmer2 , worker1])
manager2.showWorkers()

print(isinstance(programmer1 , Manager)) #programmer1 , Manager class ' ından mı gelir?(hayır)
print(issubclass(Programmer , Worker)) #Programmer , Worker'dan mı türedi
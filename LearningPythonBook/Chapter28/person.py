#%%
from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1+percent))

    
#%%
    
class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'Manager', pay)
        
    def giveRaise(self, percent, bonus=0.10):
        Person.giveRaise(self, percent+bonus)
        # self.giveRaise(percent+bonus)    


if __name__ == "__main__":
    person_1 = Person("melwin jose", "SE", 97000)
    person_2 = Person("tom richmond")
    print(person_1)
    print(person_2)
    
    print(person_1.lastName(), person_2.lastName())
    
    person_1.giveRaise(0.10)
    print(person_1.pay)
    
    person_3 = Manager('Mr Manager', 10000)
    person_3.giveRaise(0.10)
    print(person_3)


#%% Delegation/Composite Pattern : embedding objects
    
class Manager2:
    def __init__(self, name, pay):
        self.person = Person(name, 'Manager', pay)
        
    def giveRaise(self, percent, bonus=0.10):
        self.person.giveRaise(percent+bonus)
        
    def __getattribute__(self, attr):
        # intercept undefined attribute fetches
        return getattr(self.person, attr)
        
    def __str__(self):
        return str(self.person)
    

#%% pg 847
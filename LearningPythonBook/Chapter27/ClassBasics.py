#%% Baics

# class names should begin with uppercase letter

class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

# Functions inside a class are usually called methods.
# Instance attributes - members

x = FirstClass()
y = FirstClass()

x.setdata("melwin jose")
y.setdata(3.14)

x.display()
y.display()

x.data = "Melwin Jose"
x.display()

y.new_data = 100
y.display()


#%% Inheritance

class SecondClass(FirstClass):
    def display(self):
        print("SecondClass() :: ", self.data)

z = SecondClass()
z.setdata("Susha Jose")
z.display()


#%% Operator Overloading
#       also overloaded.

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return 'data :: ' + self.data
    def mul(self, other):
        self.data *= other
    
a = ThirdClass('melwin')
print(a)

b = a + ' jose'
b.display()

a.mul(3)
print(a)


#%% A Simple Class

class rec: pass

rec.name = "rec_name"

a = rec()
b = rec()

a.name = "a_name"
a.age = 26

print(rec.name, a.name, b.name)

print(list(a.__dict__.keys()))
print(list(b.__dict__.keys())) # Note : Indexing doesn't kick-off tree search

print(a.__dict__['age']) 
# print(b.__dict__['name']) # Note : Indexing doesn't kick-off tree search


#%%
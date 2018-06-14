#%% NewStyle Class Extensions - pg 1010



# Slots - basics
# - special CLASS level attribute
# - limit the set of legal attr that instance of class will have
# - optimize memory usage and possibly speed
# - must be assigned before they can be referenced

print("\n=== limiter1 ===")
class limiter(object):
    __slots__ = ['age', 'name', 'job']
    c = 4
    def __init__(self):
        print("limiter's __init__()")
        # self.d = 4                                           # AttributeError
        
x = limiter()
# x.age                                                   # AttributeError: age
x.age = 40 
print('age : ', x.age)

setattr(x, 'name', 'melwin jose')
print('name : ', getattr(x, 'name'))   # set/getattr works on both slots & dict
print('c : ', getattr(x, 'c'))

x2 = limiter()
print(x2.c) 
# getattr(x2, 'age'), getattr(x2, 'name')                   # <= AttributeError
x2.age = 41
print(x.age, x2.age)

print(limiter.__dict__)

# AttributeError: 'limiter' object has no attribute ... 
# x.ape = 1000
# setattr(x, 'c', 2)
# x.__dict__        



#%% pg 1013 - __dict__ inside ___slots__
print("\n=== limiter2 ===")
class limiter2():
    __slots__ = ['a', '__dict__']
    b = 2
    def __init__(self):
        self.c = 3
        
y = limiter2()
y.a = 1
print(getattr(y, 'a'), getattr(y, 'b'), getattr(y, 'c'))

for attr in list(getattr(y, '__dict__', [])):
    print('from __dict__ : ', attr, '=>', getattr(y, attr))
for attr in getattr(y, '__slots__', []):
    print('from __slots__ : ', attr, '=>', getattr(y, attr))



#%% pg 1014 - slots and inheritance
print("\n=== Super/Sub ===")
class Super:
    __slots__ = ['a']
    a2 = 'a2-value'

class Sub(Super):
    __slots__ = ['b', '__dict__']
    
X = Sub()
X.a = 1
X.b = 2
X.c = 3

print('\n>> __slots__')    
print(Super.__slots__)     # class __slots__ just store slot attr of that class
print(Sub.__slots__)    
print(X.__slots__)  # instance __slots__ inherits lowest __slots__ i.e from Sub

print('\n>> __dict__')
print(Super.__dict__)
print(Sub.__dict__)
print(X.__dict__)

print('\n>> getattr from dict & slots')
for attr in list(getattr(X, '__dict__', [])):
    print('from __dict__ : ', attr, '=>', getattr(X, attr))
for attr in getattr(X, '__slots__', []):
    print('from __slots__ : ', attr, '=>', getattr(X, attr))
# Missed superclass slots i.e var a !!!

print('\n>> dir + getattr')
# dir + getattr is broader than __dict__
for a in (x for x in dir(X) if not x.startswith('__')):
    print(a, getattr(X, a))



#%% pg 1016 : Slots rules
    
#1 : __slots__ not in super
class A: pass
class B(A): __slots__ = ['a']

X = B()
X.a = 1
X.b = 2                                                       # __dict__ from A
print(X.__dict__)
print(B.__dict__)


#2 : __slots__ not in sub
class A: __slots__ = ['a']
class B(A): pass

X = B()
X.a = 1
X.b = 2                                                       # __dict__ from B
print(X.__dict__)
print(B.__dict__)

#3 : __slot__ redefined in sub
class C: __slots__ = ['a']
class D(C): __slots__ = ['a']

X = D()
X.a = 1
print(X.a)



#%%

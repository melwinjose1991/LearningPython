#%% The New Style Class - pg 983

# Any class derived from object, or any other built-in type, is automatically 
# treated as a new-style class.


#%% New-Style Class Changes - pg 985

#%% Attribute Fetch for Built-ins Skips Instances - pg 987 ??? 

# %%Type Model Changes - pg 992
class C: pass
I = C()

# Classes are types, but types are also classes
print(type(I), I.__class__)
print(type(C), C.__class__)

print(type([1,2,3]), [1,2,3].__class__)
print(type(list), list.__class__)

print(isinstance(I, object))
print(isinstance(C, object))

print(isinstance(type, object))
print(isinstance(object, type))


#%% Diamond Inheritence Change - pg 997

# Classic classes - DFLR - Depth First, then Left to Right
# New-Style Classes - MRO - breadth-first
# For both attributes and methods of instances/classes

class A(): 
    attr = 1
    def createA(self):
        self.var_A = 1
        
#
class B(A): 
    attr2 = 2

class C(A): 
    attr = 3
    def createC(self):
        self.var_C = 3

#        
class D(B,C):
    # attr = B.attr           # Would choose A.attr
    def createD(self):
        self.var_D = 4
        
    def __init__(self, name="melwin jose"):
        self.name = name


x = D()
x.createA()
print(x.attr)               # Searches x, D, B, C


#%% MRO : Method Resolution order - pg 1001

print(D.__mro__)
# DFLR for non-diamond
# MRO for diamond ( exclude object while looking for diamond shapes )

# Example - pg 1004
def filterdictvals(D, V):
    return {K: V2 for (K, V2) in D.items() if V2 != V}

def invertdict(D):
    def keysof(V):
        return sorted(K for K in D.keys() if D[K] == V)
    return {V: keysof(V) for V in set(D.values())}

def dflr(cls):
    here = [cls]
    for sup in cls.__bases__:
        here += dflr(sup)
    return here

def inheritance(instance):
    if hasattr(instance.__class__, '__mro__'):
        return (instance,) + instance.__class__.__mro__
    else:
        return [instance] + dflr(instance.__class__)
    
def mapattrs(instance, withobject=False, bysource=False):
    """
    dict with keys giving all inherited attributes of instance,
    with values giving the object that each is inherited from.
    
    withobject  : False = remove 'object' built-in class attributes.
    bysource    : True  = group result by objects instead of attributes.
    
    """
    attr2obj = {}
    inherits = inheritance(instance)
    
    for attr in dir(instance):
        for obj in inherits:
            if hasattr(obj, '__dict__') and attr in obj.__dict__: # See slots
                attr2obj[attr] = obj
                break
            
    if not withobject:
        attr2obj = filterdictvals(attr2obj, object)
        
    return attr2obj if not bysource else invertdict(attr2obj)


from pprint import pformat

print("\n"+pformat(mapattrs(x))+"\n")

print(pformat(mapattrs(x, bysource=True))+"\n")



#%%

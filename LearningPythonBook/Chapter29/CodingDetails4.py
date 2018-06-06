#%% Namespace Dictionaries : Review - pg 878

class Super:
    data0 = "ham"
    def hello(self):
        self.data1 = "spam"
        
class Sub(Super):
    data3 = "foo"
    def hola(self):
        self.data2 = "eggs"

X = Sub()
print(X.__dict__)

X.hello()
print(X.__dict__)

X.hola()
print(X.__dict__)
# As classes assign to self attributes, they populate the instance 
# objects—that is, attributes wind up in the instances’ attribute namespace 
# dictionaries, not in the classes’.

Y = Sub()
print(Y.__dict__)
# Again, each instance has an independent namespace dictionary, which starts 
# out empty and can record completely different attributes than those
# recorded by the namespace dictionaries of other instances of the same class.

print(Super.__dict__.keys())
print(Sub.__dict__.keys())


#%% Namespace Links: A Tree Climber - pg 880

def classtree(cls, indent):
    print('.' * indent + cls.__name__)      # Print class name here
    for supercls in cls.__bases__:          # Recur to all superclasses
        classtree(supercls, indent+3)       # May visit super > once

def instancetree(inst):
    print('Tree of %s' % inst)      # Show instance
    classtree(inst.__class__, 3)    # Climb to its class

def selftest():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B,C): pass
    class E: pass
    class F(D,E): pass

    instancetree(B())
    instancetree(F())

    
selftest()


#%% Documentation Strings Revisited - pg 882


#%%

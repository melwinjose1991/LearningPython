#%% Methods Are Objects: Bound or Unbound - pg 948

# Two flavors of class methods, based on how it is accessed :
#   Unbound method objects: no self
#   Bound method objects: self + function pairs

class Spam():
    def doit(self, msg):
        print(msg)
    
    def selfless(arg1, arg2):
        return arg1 + arg2
    
X = Spam()
bound_obj = X.doit          # Bound Method Objects
bound_obj("Hello World")

unbound_obj = Spam.doit    # Unbound Method Objects
unbound_obj(X, "Hello World")

# X.selfless(1,2)            # Error : selfless() doesn't require self
# Spam.doit('Hello World')   # Error : doit() requires self


#%% Multiple Inheritance : pg 959

class ListTree:
    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                # result += spaces + '{0}\n'.format(attr)
                pass
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<Class {1}:, address {2}: (see above)>\n'.format(
                           dots, 
                           aClass.__name__, 
                           id(aClass))
        else:
            self.__visited[aClass] = True
            
            here  = self.__attrnames(aClass, indent)
            
            above = ''
            for super in aClass.__bases__:
                above += self.__listclass(super, indent+4)
                
            return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(
                           dots, 
                           aClass.__name__, 
                           id(aClass), 
                           here, above, 
                           dots)

    def __str__(self):
        self.__visited = {}
        here  = self.__attrnames(self, 0)
        above = self.__listclass(self.__class__, 4)
        return '<Instance of {0}, address {1}:\nObj.__dict__:\n{2}\n obj.__class__.__dict__:{3}>'.format(
                           self.__class__.__name__,
                           id(self),
                           here, 
                           above)

class A:
    def __init__(self, a):
        self.a = a
        A.a_class_attr = 123
        
    def Afunc():
        pass

        
class B(A, ListTree):
    def __init__(self, b, a=0):
        A.__init__(self, a)
        self.b = b
        B.b_class_attr = 456

    def Bfunc():
        pass

obj_b = B(1, 2)
print(obj_b)
#%% Stream Processor Revisited - pg 938

class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
    
    def process(self):
        while True:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)
            self.writer.write(data)
    
    def converter(self, data):
        assert False, 'converter must be defined'

class Uppercase(Processor):
    def converter(self, data):
        return data.upper()
    
class HTMLize:
    def write(self, line):
        print('<PRE>%s</PRE>' % line.rstrip())

if __name__ == '__main__':
    import sys
    Uppercase(open('trispam.txt'), sys.stdout).process()
    Uppercase(open('trispam.txt'), HTMLize()).process()



#%% OOP and Delegation: "Wrapper" Proxy Objects - pg 942
    
class Wrapper:
    def __init__(self, object):
        self.wrapped = object                   # Save object
    
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)             # Trace fetch
        return getattr(self.wrapped, attrname)  # Delegate fetch
   
x = Wrapper([1, 2, 3])
x.append(4)                                     # Delegate to list method
print(x.wrapped)



#%% Pseudoprivate Class Attributes : pg 944

# Python today does support the notion of name “mangling” (i.e., expansion) to 
# localize some names in classes. Mangled names are sometimes misleadingly called
# “private attributes,” but really this is just a way to localize a name to the 
# class that created it—name mangling does not prevent access by code outside 
# the class.

class C1:
    def meth1(self): self.__X = 88 
    def meth2(self): print(self.__X)     # Becomes _C1__X in I
    
class C2:
    def metha(self): self.__X = 99  
    def methb(self): print(self.__X)    # Becomes _C2__X in I

class C3(C1, C2): pass

I = C3()                                # Two X names in I
I.meth1(); I.metha()
print(I.__dict__)
I.meth2(); I.methb()


#%%
#%% __getitem__ & __setitem__

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __getitem__(self, index):
        print("Person :: __getitem__")
        if isinstance(index, int):
            if index==0:
                return self.name
            elif index==1:
                return self.age
            else:
                raise IndexError
        else:   
            # when slice object is passed
            print('Slicing :: start_index:', index.start, 'end_index:',index.stop)
            to_return = []
            for i in range(index.start, index.stop+1, 1):
                to_return.append(self[i])
            return to_return
        
    def __setitem__(self, index, value):
        if isinstance(index, int):
            if index==0:
                self.name = value
            if index==1:
                self.age = value
        # can also receive slice object
            
me = Person('melwin', 26)
print(me[0], "\n")
print(me[1], "\n")
print(me[0:1], "\n")

me[0] = 'Melwin Jose'
print(me[0])

# 'for' statement works by repeatedly indexing a sequence from zero to higher
# indexes, until an out-of-bounds IndexError exception is detected.
for i in me:
    print(i)
print('\n')

# the in membership test, list comprehensions, the map built-in, list and 
# tuple assignments, and type constructors will also call __getitem__ 
# automatically, if it’s defined
print(26 in me)


#%% Iterable objects : __iter__ & __next__
# pg 895

# all iteration contexts in Python will try the __iter__ method first, before 
# trying __getitem__

# iteration contexts work by passing an iterable object to the iter built-in
# function to invoke an __iter__ method, which is expected to return an 
# iterator object. If it’s provided, Python then repeatedly calls this 
# iterator object’s __next__ method to produce items until a StopIteration 
# exception is raised.

class Squares:
    def __init__(self, start, stop): # Save state when created
        self.value = start - 1
        self.stop = stop
    
    def __iter__(self):             # Get iterator object on iter
    # single traversal only. For mutliple pass, create new instance OR
    # convert to a list
        return self
    
    def __next__(self):             # Return a square on each iteration
        if self.value == self.stop: # Also called by next built-in
            raise StopIteration
        self.value += 1
        return self.value ** 2
    
for i in Squares(1,5):
    print(i, end=' ')
   

#%% User Defined Iterator Object
    
class SkipObject:
    def __init__(self, wrapped):            # Save item to be used
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)   # New iterator each time

class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped              # Iterator state information
        self.offset = 0
        
    def __next__(self):
        if self.offset >= len(self.wrapped): # Terminate iterations
            raise StopIteration
        else:
            item = self.wrapped[self.offset] # else return and skip
            self.offset += 2
            return item

alpha = 'abcdef'
skipper = SkipObject(alpha)                 # Make container object
I = iter(skipper)                           # Make an iterator on it
print(next(I), next(I), next(I))            # Visit offsets 0, 2, 4

for x in skipper:                   # for calls __iter__ automatically
    for y in skipper:               # Nested fors call __iter__ again each time
        print(x + y, end=' ')       # Each iterator has its own state, offset


#%% The same above functionality, but using yield.
# Advantages: Supports multiple scans. Less code. No need iterator class.
        
class SkipObject:                   # Another __iter__ + yield generator
    def __init__(self, wrapped):    # Instance scope retained normally
        self.wrapped = wrapped      # Local scope state saved auto
    
    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item
        
I = iter(SkipObject('abcdef'))
print(next(I),next(I))

J = iter(SkipObject('abcdef'))
print(next(J))

print(next(J),next(J))
print(next(I))


#%%


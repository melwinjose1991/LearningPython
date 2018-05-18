#%% Generators - produces results only when needed
# Two Types : Generator Functions and Expressions


#%% Generator Functions

# uses 'yield' inside def 
# they return a result generator that can appear in any iteration context
# pg 592: State Suspension
# pg 592: Iteration protocol integration

print("=== next() ===")
L = [1, 2, 3]
def genSquares(L):
    for i in L:
        yield i**2

for square in genSquares(L):
    print(square, end=" ")

squares = genSquares(L)
print("\n", next(squares))
print(next(squares))
print(next(squares))

print("\n === send() ====")
def gen():
    for i in range(10):
        X = yield i
        print(X)

G = gen()
print(next(G))
print(G.send(1))
print(next(G))


#%% Generator Expressions

G = (x**2 for x in range(4))
print(next(G))
print(next(G))
print(next(G))
print(next(G))

# (x**2 for x in range(4)) 
#   the above return a generator object

for x in (x**2 for x in range(4)):
    print(x)


# generator exp vs map
#  list comprehension creates a temporary list
#  map loses simplicity


#%% Generators just support one active iteration

def timesFour(S):
    for c in S:
        yield c*4
        
G = timesFour('spam')
I1,I2 = iter(G), iter(G)
print(next(I1))
print(next(I2))
print(next(I2))
print(next(I1))
print(next(I2)) # StopIteration !!!
    
    
#%% Built-in Generations

# keys of dict
# open('file')
# os.walk() , recursive directory walker


#%% Scramble Generator

def scramble(items):
    for i in range(len(items)):
        items = items[1:] + items[:1]
        yield items

for s in scramble([1,2,3]):
    print(s)
   
    
# Explicit is better than implicit


#%% Examples : Map
l = [-1, 2, -3]

def mymap1(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)

def mymap2(func, *seqs):
    return (func(*args) for args in zip(*seqs))    

for a in mymap1(abs, l):
    print(a)
    
for a in mymap2(abs, l):
    print(a)
  
    
#%% Examples : Zip
l1 = [1, 2, 3]
l2 = [1, 2, 3, 4]

def myZipComp(*seqs):
    seqs = [list(S) for S in seqs]
    print(seqs)
    
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res

def myZipGen(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)

myZipComp(l1, l2)
myZipGen(l1, l2)


#%% 3.X map returns a one-shot iterable object !!!
l = ('abc', 'xyz123')
iters = map(iter, l1)
for iiter in iters:
    print(iiter)


#%%

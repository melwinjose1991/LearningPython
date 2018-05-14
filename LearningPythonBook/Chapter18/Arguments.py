#%% Passing Arguments
# Immutable are passed by value
# Mutable are passed by reference

def func_1(A, B, C):
    A += 1
    B[0] += 1
    C = ['a', 'b']

a = 1
b = [1, 2]
c = ['y', 'z']
func_1(a, b, c)
print(a, "\n", b, "\n", c)


#%% Multiple Reutrns

def func_1():
    return 1,2,3

a, b, c = func_1()
print(a, b, c)


#%% Argument matching order

#1: nonkeyword args by position
#2: keyword args by matching names
#3: extra nonkeyword args to *name tuple
#4: extra keyword args to **name dictionary
#5: default values to unassigned args in header

def func_1(a, b=0, *pargs, **kargs):
    print("a = ", a)
    print("b = ", b)
    print("pargs = ", pargs)
    print("kargs = ", kargs)
    
func_1(1, 2, 3, 4, y=5, z=6)

def func_2(a, b, c=1):
#def func_2(a, b=1, c): , doesn't work 
    print(a, b, c)
    
# func_2(1, c=2, 3) , doesn't work
    

#%% Arbitrary Args 

# Headers - Collection Args
def func_1(*pargs):
    print(pargs)
    
func_1(1,2,3)

def func_2(**kargs):
    print(kargs)
    
func_2(a=1, b=2, c=3)

# Calls - Unpacking Args
def func_3(a, b):
    print(a)
    print(b)
    
func_3(*(1,2))
func_3(**{'a':1, 'b':2})


#%% Keyword-Only Args - used for passing config options
# Has to define after * and before **
# Can have defaults

def func_1(a, *b, c):
    print("func_1")
    print(a)
    print(b)
    print(c)
    
func_1(1, 2, c=3)
# func_1(1, 2, 3) # 3 param must be keyword=value

def func_2(a, *, b, **kargs):
    print("\nfunc_2")
    print(a)
    print(b)
    print(kargs)

func_2(1, b=2, c=3, d=4)
    

#%% Exercise - min function

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y

print(minmax(lessthan, 4, 2, 1, 5, 6, 3)) 
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))

#%% 
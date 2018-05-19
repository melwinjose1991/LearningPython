#%% Indirect Function Calls

# Functions as arguments
def func_1(a):
    print("func_1() : ", a)

def func_2(a):
    print("func_2() : ", a)
    
def caller(func, arg):
        func(arg)
        
caller(func_1, 1)
caller(func_2, 1)

x = caller
x(func_1, 1)
x(func_2, 1)


# Functions inside data structures
schedule = [(func_1, 1), (func_2, 2)]
print("\nStarting Scheduled Functions")
for (func, arg) in schedule:
    func(arg)
    
    
#%%% Function Introspection

dir(func_1)
print(func_1.__name__)


#%% Functions Attributes

def func_1():
    print(func_1.a)
    
func_1.a = 1
func_1.a += 1
print(func_1.a) 
func_1()


#%% Function Annotations

def func_1(a:'1st arg'=1, b:'2nd arg'='melwin') -> float:
    print("Nothing much")
    
print(func_1.__annotations__)

    
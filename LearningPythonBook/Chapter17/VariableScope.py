#%% Function Vairable Scope

global_var = 1

def func_1():
    global_var = 2
    print("func_1 : ", global_var)
    
def func_2():
    global global_var
    print("func_1 : ", global_var)
    
def func_3():
    global global_var
    global_var = 3
    print("func_1 : ", global_var)
    
func_1()
print("Outside : ", global_var, "\n")

func_2()
print("Outside : ", global_var, "\n")

func_3()
print("Outside : ", global_var, "\n")


#%% Nested Functions
def f1():
    X = 88
    def f2():
        print(X)
    f2()

f = f1()
f() # f2() remembers f1()'s scope


#%% Factory Functions : Closures

def maker(N):
    def action(X):
        return X ** N
    return action

f = maker(2)
print(f(3)) # Remembers the scope variable, N=2
print(f(4))

g = maker(3)
print(g(3)) # Remembers the new scope assignment, N=3
print(g(4))


#%% Nested Functions : Lambdas

def func_1():
    x = 4
    action = (lambda n: x ** n)
    return action
    
x = func_1()
print(x(2))


def func_2():
    act = []
    for i in range(5):
        act.append(lambda x: x ** i)
    return act
    
y = func_2()
print(y[0](4)) # !=1, as lambda remembers the last iteration value


def func_3():
    act = []
    for i in range(5):
        act.append(lambda x,i=i: x ** i)
    return act
    
y = func_3()
print(y[0](4)) # Need to assign default to i


def func_4():
   state = 1
   def inner_func_4():
       # state += 1 # Not allowed, read nonlocal variables
       print("Nothing Much")
   return inner_func_4

y = func_4()
y()

#%% nonLocal

def outer():
    state = 0
    def inner():
        nonlocal state
        # nonlocal state2 # Won't work, state2 need to be present in enclosing 
        # scope
        state += 1
        print("State : ", state)
    return inner

x = outer()
x()


#%% Function Attributes
def outer():
    def inner():
        inner.var += 1
        print(inner.var)
    inner.var = 0
    return inner

f = outer()
f()
f()

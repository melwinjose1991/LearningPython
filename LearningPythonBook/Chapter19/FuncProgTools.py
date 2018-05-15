#%% map
l = [1, 2, 3]

def inc(x):
    return x+1

print(list(map(inc, l)))
print(list(map(lambda x: x+1, l)))


#%% filter
l = range(-5, 5)

print(list(filter(lambda x: x>0, l)))


#%% reduce
from functools import reduce

print(reduce(lambda x,y: x+y, l))

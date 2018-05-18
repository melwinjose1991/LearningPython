#%% List Comprehensions


res = [ord(x) for x in 'spam']
print(res)


# filter and map
print([ x**2 for x in range(10) if x%2==0 ])


# [ exp for target1 in iterable1 if condition1
#       for target2 in iterable2 if condition2 ... ]
#

print([x+y for x in [0,1,2] for y in [0,1,2]])
print([x + y for x in 'spam' if x in 'sm' for y in 'SPAM' if y in ('P', 'A')])
print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])
# The map & filter equivalent would be complex


M = [[1,2,3],[4,5,6],[7,8,9]]
print([col+10 for row in M for col in row])
print([[col+10 for col in row] for row in M])


# programming is not about being clever and obscure—it’s about how clearly 
# your program communicates its purpose


# time taken : list comprehensions < map < for
# list comp. & map run at C language speed inside the interpreter

          
#%%
# map is slightly faster than list comprehensions, both are quicker than 
# for loops, and generator expressions and functions place in the middle


# We can say for certain is that on this Python, using a user-defined
# function in map calls seems to slow performance substantially, and that list 
# comprehensions run quickest in this case (though slower than map in some 
# others). List comprehensions seem consistently twice as fast as for loops, 
# but even this must be qualified—the list comprehension’s relative speed might
# be affected by its extra syntax (e.g., if filters), Python changes, and usage 
# modes we did not time here.


# Write for readability and simplicity first, then optimize later, if and only 
# if needed. It could very well be that any of the five alternatives is quick
# enough for the data sets your program needs to process; if so, program 
# clarity should be the chief goal.


#%% timeit

import timeit
stmt = "[x ** 2 for x in range(1000)]"
print(timeit.repeat(stmt=stmt, number=100, repeat=5))
 
# multiline statement
stmt = "L = [1, 2, 3, 4, 5]\ni=0\nwhile i < len(L):\n\tL[i] += 1\n\ti += 1"
print(timeit.repeat(number=10000, repeat=3, stmt=stmt))

# setup
from timeit import repeat
setup = '#from <library> import <functions>\nvals=list(range(1000))' 
repeat(number=1000, repeat=3, setup=setup, stmt='min(vals)')


#%% 651
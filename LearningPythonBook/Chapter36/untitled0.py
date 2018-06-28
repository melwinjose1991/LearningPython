#%% Nesting Exception Handlers - pg 1141

# once the exception is caught, its life is over - pg 1141
# the finally clauses do not kill the exception - pg 1142



#%% Exception Idioms - pg 1145

# "go to"
print('\n ... go to ...')
class ExitLoop(Exception): pass

try:

    while True:
        while True:
            for i in range(10):
                if i>3: raise ExitLoop
                print('loop3', i)
            print('loop2')
        print('loop1')

except ExitLoop:
    print('continuing')


# Exceptions aren't always errors - pg 1146
# In Python, all errors are exceptions, but not all exceptions are errors.
#   Example, EOFError


# Functions can signal conditions with raise - pg 1147
    
# By wrapping an entire program (or a call to it) in an outer try in your 
# top-level code, you can catch any exception that may occur while your
# program runs, thereby subverting the default program termination - pg 1149
    
# PyUnit
    
# sys.exc_info : (type, value, traceback)

# traceback
print('\n ... traceback ... ')
import traceback

try:
    1 / 0
except Exception:
    traceback.print_exc(file=open("Errors.log", "w"))

print('Bye')    




#%% Exception Design Tips and Gotchas - pg 1152

# What should be wrapped - pg 1152

# Catching Too Much: Avoid Empty except and Exception - pg 1153
# You many wind up interception an error thats expected by a try handler higher
# up in the exception nesting structure.
# Rule of thumb : Be as specific in your handlers as you can be.

# Catching Too Little: Use Class-Based Categories - pg 1155
# If you catch a general superclass, you can add and raise more specific 
# subclasses in the future without having to extend except clause lists 
# manually—the superclass becomes an extendible exceptions category.



#%% Core Language Summary - pg 1155







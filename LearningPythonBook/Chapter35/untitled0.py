#%% Coding Exceptions Classes - pg 1126

class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser0():
    X = General() 
    raise X

def raiser1():
    X = Specific1()
    raise X

def raiser2():
    X = Specific2() 
    raise X

import sys
for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General: 
        print('caught: %s' % sys.exc_info()[0])

# it’s usually better to be specific than general in exception handlers



#%% Default Printing and State - pg 1131
# Any constructor arguments you pass to these classes are automatically saved 
# in the instance’s args tuple attribute, and are automatically displayed
# when the instance is printed
  
try:
    raise General
except Exception as E:
    print(E)
    
try:
    raise General('Testing1')
except Exception as E:
    print(E)
    
try:
    G = General('Testing2')
    raise G
except Exception as E:
    raise
    
    
    
#%% Custom Print Displays - pg 1135
    
class MyBad(Exception):
    def __str__(self):
        # print(self.args)
        return '... __str__() called ...'

    def __repr__():
        return '... __repr__() called ...'
    
try:
    raise MyBad('String')
except MyBad as X:
    print(X)

raise MyBad()

    
    
#%% Custom Daat and Behavior - pg 1136


# Providing Exception Details / Methods
class FormatError(Exception):
    logfile = 'errors.log'
    def __init__(self, line, file):
        self.line = line
        self.file = file
    
    def logerror(self):
        log_file_handle = open(FormatError.logfile, 'a')
        print('Error at : ', self.file, ' at line', self.line, 
              file=log_file_handle)
    
def parser():
    raise FormatError(line=42, file='spam.txt')

try:
    parser()
except FormatError as X:
    # print('Error in', X.file, ' at line :', X.line)
    X.logerror()    

with open(FormatError.logfile) as file:
    for line in file:
        print(line)



#%%
#%% try Statement Clause forms - pg 1095 
# Table 34-1
#       except:                                       catch all exception types
#       except name:                            catch a specific exception only
#       except (name1, name2):               catch any of the listed exceptions
#       else:                  run if NO excpetions are raised in the try block
#       finally:                              ALWAYS perform this block on exit 



#%% try / except / else 

x = [1, 2, 3]

def func1(obj, index):
    try:
        print(obj[index])
    except IndexError:
        print('caught IndexError')
    else:       # without it there is no way to tell if no exception was rasied
        print('no exception raised') 

    print('this happens anyway\n')
    
func1(x, 1)
func1(x, 4)



#%% try/finally statement - pg 1101

def func2(obj, index):
    try:
        print(obj[index])
    # no except / else here
    finally:
        # if Exception is active at this point, it continues to propagate !!!
        print('...finally...')
        
    print('this happens only if exception is not raised\n')
    
func2(x, 1)
func2(x, 4)



#%% try / except / finally - pg 1102

def func3(obj, index):
    try:
        print(obj[index])
    except IndexError:
        print('caught IndexError')
    else:       
        print('no exception raised') 
    finally:
        print('finally block')
        # if Exception is active at this point, it continues to propagate !!!
        # active = an error that is not caught with except statement
        
    print('this happens anyway\n')
    
func3(x, 1)
func3(x, 4)
# examples - pg 1105



#%% raise - pg 1107

# raise instance                                      
    # Raise instance of class

# raise class             
    # Make and raise instance of class: makes an instance

# raise                                     
    # Reraise the most recent exception used if you need to catch and handle 
    # an exception but don't want the exception to die in your code



#%% 'as' 
try:
    1/0

except Exception as X:
    print(X)
    
# X                                  # 3.X localizes 'as' names to except block


X = [1, 2, 3]

try: 
    1/0
except Exception as X:
    print(X)

# print(X)                               # 3.X localizes _and_ removes on exit!



#%% raise ... from ... - pg 1110

try:    
    
    try:    
    
        try:
            raise IndexError('Oh NO !!! IndexError()')
        except Exception as E:
            raise TypeError('Oh NO !!! TypeError()') from E
            
    except Exception as E:
        raise SyntaxError('Oh NO !!! SyntaxError()') from E
        
except Exception as E:
    print(E)
    print(E.__cause__)
    print(E.__context__)
    raise Exception() from E
    
# ??? Not getting the chainned exception messages
    
    

#%%
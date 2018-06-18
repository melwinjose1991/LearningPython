#%%

x = "spam"

def fetcher(obj, index):
    return obj[index]

def catcher():
    try:
        fetcher(x, 4)
    except IndexError:
        print('caught exception ... inside IndexError ...')
        
    print('back to catcher()')

catcher()

#%% - Raising Exceptions

def catcher2():
    try:
        raise IndexError
    except IndexError:
        print('caught exception ... inside IndexError ...')
        
    print('back to catcher2()')

catcher2()


#%% User-Defined Exceptions

class UserException(Exception): pass

def catcher3():
    try:
        raise UserException
    except UserException:
        print('caught UserException')
    finally:
        print('finally')  
        # the finally is run on the way out regardless of whether an exception 
        # was raised, and regardless of whether the exception was caught by 
        # an except clause.
        
    print('back to catcher3()')

catcher3()


#%% Termination Actions

def catcher4():
    try:
        fetcher(x, 1)
    except IndexError:
        print('caught IndexError')
    finally:
        print('finally')
        
    print('back to catcher4()')
    
catcher4()


#%%
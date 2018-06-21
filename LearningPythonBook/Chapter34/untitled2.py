#%% with / as Context Managers - pg 1114

with open('untitled2.py') as myfile:
    for line in myfile:
        print(line)



#%% The Context Management Protocol - pg 1116
        
class CMP:
    def message(self, arg):
        print('message() :: arg = ' + arg)
    
    def __enter__(self):
        print('__enter__() :: start')
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('__exit__() :: exiting normally\n')
        else:
            print('__exit__() :: got an exception ', str(exc_type))
            return False                              # Propagate the exception


with CMP() as cmp_obj:
    cmp_obj.message('something')
    
with CMP() as cmp_obj:
    cmp_obj.message('something')
    raise TypeError



#%% Multiple Context Managers - pg 1118
    
with open('untitled2.py') as fin, open('out.txt', 'w') as fout:
    for line_in in fin:
        line_out = line_in.upper()
        fout.write(line_out)

print(open('out.txt').read())
     


#%%
#%% 

# The __getattr__ method intercepts attribute references. It’s called with the 
# attribute name as a string whenever you try to qualify an instance with an 
# undefined (nonexistent) attribute name. It is not called if Python can find 
# the attribute using its inheritance tree search procedure.

# The __setattr__ intercepts ALL attribute assignments. If this method is 
# defined or inherited, self.attr = value becomes self.__setattr__('attr',value)
# Use self.__dict__['name'] = x, not self.name = x; because you’re not 
# assigning to __dict__ itself, this avoids the loop
class Person:
    def __setattr__(self, attr, value):
        if attr == 'age':
                self.__dict__[attr] = value + 10
        else:
            raise AttributeError(attr + 'not allowed')
    
me = Person()
me.age = 16
print(me.age)

# me.name = "Melwin Jose"


#%%
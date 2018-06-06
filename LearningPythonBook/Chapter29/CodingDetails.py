#%%
class MixedNames:
    data = 'spam'
    
    def __init__(self, value):
        self.data = value
    
    def display(self):
        print(self.data, MixedNames.data)

x = MixedNames(1)
y = MixedNames(2)

x.display()
y.display()

MixedNames.data = "class_spam"
x.data = "x_spam"
# inheritance searches occur only on attribute references, not on assignment: 
# assigning to an object’s attribute always changes that object, and no other

x.display()
y.display()


#%% Inheritor | Replacer | Extender | Provider

class Super:
    def method(self):
        print('in Super.method')    # Default behavior
    def delegate(self):
        self.action()               # Expected to be defined
    def action(self):
        assert False, "Action() must be defined!"
        
class Inheritor(Super):             # Inherit method verbatim
    pass

class Replacer(Super):              # Replace method completely
    def method(self):
        print('in Replacer.method')

class Extender(Super):              # Extend method behavior
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super):              # Fill in a required method
    def action(self):
        print('in Provider.action')


for klass in (Inheritor, Replacer, Extender):
    print('\n' + klass.__name__ + '...')
    klass().method()
    
print('\nProvider...')
x = Provider()
x.delegate()
# When we call the delegate() method through a Provider instance, two independent 
# inheritance searches occur. One for finding delegate() and other for finding
# action()

print('\nInheritor...')
x = Inheritor()
x.delegate()                    # action() call reached Super-class !!!


#%%
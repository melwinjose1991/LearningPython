#%%

from person import Person, Manager

melwin = Person('Melwin Jose', 'SE in Analytics', 97000)
melna = Manager('Melna Jose', 110000)

import shelve
db = shelve.open('peopledb')

for obj in (melwin, melna):
    db[obj.name] = obj
    
db.close()


#%%

db = shelve.open('peopledb')

print(list(db.keys()))

for key in db:
    print(key, "=>", db[key])

db.close()   
    

#%%
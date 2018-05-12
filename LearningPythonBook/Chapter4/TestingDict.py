person = { 'name' : {'first':'melwin', 'last':'jose'},
          'age' : 26}
print(person)


#%% Access and Modify

if 'name' in person:
    print(person['name'])

person['job'] = 'Software Engineer'


#%% Sorting Keys

Keys = list(person.keys())
Keys.sort()

for key in Keys:
    print(key," -> ",person[key])
    

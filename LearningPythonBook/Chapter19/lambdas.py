#%% Basics
x = lambda a=1,b=2,c=3: a+b+c
print(x(1,2))

ending = "III"
def Knight():
    title = "Sir"
    action = (lambda x: title+' '+x+' '+ending)
    return action

act = Knight()
print(act('James'))


#%% if...else

lower = lambda x,y: x if x<y else y
print(lower(1,2))
print(lower(2,1))


#%% for & if...else ???



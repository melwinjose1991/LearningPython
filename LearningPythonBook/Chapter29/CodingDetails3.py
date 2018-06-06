#%% 

import CodingDetails2

X = 66
print(X)                    # 66: the global here
print(CodingDetails2.X)     # 11: globals become attributes after imports

CodingDetails2.f()          # 11: CodingDetails2's X, not the one here!
CodingDetails2.g()          # 22: local in other file's function

print(CodingDetails2.C.X)   # 33: attribute of class in other module
I = CodingDetails2.C()
print(I.X)                  # 33: still from class here
I.m()
print(I.X)                  # 55: now from instance!    <<< 


#%%
#%% === List Creation ===

L = [123, "melwin", 123.123]
N = [3, 2, 4, 1, 5]

print(L)
print(len(L))


#%% === List modification ===

L.append('jose')
print(L)

L.pop(2)
print(L)


#%% === List Specific Operations ===

N.sort()
print(N)

N.reverse()
print(N)


#%% === Nesting ===

Matrix = [[1,2,3],[4,5,6]]

print(Matrix[0])
print(Matrix[1][2])


#%% === Comprehension ===

print([row[0] for row in Matrix])

print([row[0]+1 for row in Matrix])

print([row[0] for row in Matrix if row[0] % 2 ==0])

# Geneators
G = (sum(row) for row in Matrix)    
print(next(G))
print(next(G))

# Map
print(list(map(sum, Matrix)))

# Set
print({sum(row) for row in Matrix})

# Dictionary
print({i:sum(Matrix[i]) for i in range(2)})


#%%


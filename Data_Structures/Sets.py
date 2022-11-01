# like the list but with out duplicate 

# using {} to declaire set 

x = 'hello'
x1 = list(x)
print(x1)

#### the same thing for list 
# we can convert string to list & list to set & set to list 

x2 = set(x1)
print(x2)  # list to set

x3 = ''.join(x1) #list to string
print(x3)

x2.add('hello')
print (x2)

### note : list is inordered so we cant indexing it 
##print(x2[0])  ------ errror

x2.pop()# remove a random element
x1.pop() # remove the last element beacuse its ordered 

# we can using (in) & (not in ) with it 
print('hello' in x2)

# its mutable beacue add and pop

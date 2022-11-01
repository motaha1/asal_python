elements = {"hydrogen": 1, "helium": 2, "carbon": 6}


# insert new value ------ 
elements['hello'] = 5 

# we can use (in / not in) in decionary (for key )

print('carbon' in elements)

#print(elements['jjj']) # its print error 

print(elements.get(1)) # its return none

#### is / not is 
x=elements.get(1) is not None
print (x) # to return false /trur instead of none 

#قاعدة : the key must be immutable like tubles and string an int and flaot 

print(len(elements))




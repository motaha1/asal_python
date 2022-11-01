from lib2to3.pytree import type_repr


x = 2<3 # true
x = 2>3 # false
 
print (x) 
#1- # < / > / == / != /  <= / >= 
print(type(x))

#2- logic # and / or /not 

y = x < 30 or 30!=30
print(y)


#when we return bool we only but it direct 
# return x<y # without if statment !


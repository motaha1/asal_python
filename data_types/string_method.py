# this is method beacuse its using with specific object (string )  / type is function / print is function / len function (its not in side string class)

#title is method not function

#title method
p='mohammad taha'
print(p.title())

#is_lower 
print(p.islower())
print(p.title().islower())

#count
p='motaha taha taha'
print('count---------'+str(p.count('taha')))


## find 
print('find---------'+str(p.find('taha')))

## format 
print('hello {} {} i love you!'.format('mo','taha'))

#split
new_str = "The cow jumped over the moon."
list1 = new_str.split()
list=new_str.split(' ',3)
print(list1)



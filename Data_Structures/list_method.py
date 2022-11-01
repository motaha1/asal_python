### very important :
 # string is immutable (and its object and refrence ) a= 'motaha'(a point to 'motaha') / b = a(make new location) / a = 'taha' / a-------- taha / b ------ motaha

 # list is muttable  (and its object and refrence ) but diffrent from string 

a =[1 , 2 ,3]

b= a  #  the refrence of a and b point to the same location  (in list )
a[0] = 5
b[-1] = 5
print(a)
print(b)
# the refrence of a and b point to the same location  (in list )
# the refrence of a not point to the same location (in string )


####### the function (not method) -------- for list 
#1- len 
#2- max ----- if list of num return the max number 
    #---- if list of string return the max alphabit 
    # if list of string  and num ---- error

print(max('motaha','ahmad' , 'ioio')) #---- motaha 


print(max(a)) #---- 5 

#3-min 

#4- sorted()------ sort list (can sort revirece)

c = [5 , 4 , 9]
c = sorted(c , reverse=True)
print(c)



################## method 
# 5- join ----- convert list of string to string(بستخدمها مع سترنج بدي افصل بيناتهم )  #method for stirng 
#بستدعيها باستخدام سترينج 

uu = ['mo' , 'taha']
print('-'.join(uu))

#6- append ------ add element to the last of list    #method for list
uu.append('uu')

print (uu)



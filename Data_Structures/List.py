s = [1 , 4 , 'i' , True]
print (type(s))
print(s[3])
# print(s[4])
print(s)

# print the last element ------ (-1)
# print the second last element  ---- (-2)
print(str (s[-1])+' ' +s[-2])
#print(s[len(s)])  ------- error 

s1 = s[1:3]  # 1 is inclusive and 2 is exclutve 
# number of elemt in s1 ---- 2-1 = 1
print(len(s1))


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

s1 = months[0:3+1]
first_half = months[:6] # defult from 0  /// 6 exlusive 
second_half = months[6:]   # 6 inclusive 


print(s1 +first_half )

############################ slicing in list and string 
#### we can use len function with string and list 

x = 'moahammad taha'
y = ['a' , 'b' , 'c' , 'd']


x1 = x[3:5] #3  inclusive and 5 exclusive 

y1 =y[3:5]  #3  inclusive and 5 exclusive 
print(x1,y1)

############# in and not in (we can use it in string and list )

print ('hello' in months , 'January' in months) 

print('taha' in x , 'taha4' not in x)
#remember in string using find method 
print(x.find('tah'))
print('hello' not in 'hello world')

months[3] = 'sunday'
print(months)

print(x[-1]) #print the last letter in string 


# x[0]='M'
# print(x)
#فرق جوهري بين اللست و الستريج ان الليست يمكن تغيير احد عناصرها مباشرة اما الليست لا يمكن تعديل على حرف لوحده مباشرة 

#حفظ 
#string is immutable /// list is mutuble ------- الشرح فوق   
#string and list is ordered //// يمكن الدخول على اي عنصر منهم باستخدام ال indexing 

#-----------------------------------------------------
# note : we can use negative index for slicing 
# x =x[-3:] 

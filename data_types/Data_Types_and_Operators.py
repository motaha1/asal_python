x = 3. # x is float 
y = 3 
z = x+y
print (z) # --- -- 6.5 // add float to int give float 
print (type(z)) 

# we can use type casting 
# convert z to int 
z = int(z)
print (z)
print(0.1+0.1+0.1)
print(.1 + .1 + .1 == .3)
print (float(3))


## اذا كان لدي اكثر من عملية نضع مسافة على طرفي العملية الاقل اولوية 
# لتسهيل قراءة الكود
print(x*3 - 1)
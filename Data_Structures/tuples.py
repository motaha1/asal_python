### immutable --------- لا يمكن التغيير على احد عناصرها 
## beacuse its immutable ------- a = tuple \ b =a   / refrence a != refrence b (b is new object )
# tuples is ordred ----- not true prob.
# 
#  نستخدمها لما بدي اخزن شغلتين او اكثر الهم علقة ببعض (خطوط الطول و العرض / الابعاد :طول عرض ارتفاع / ..... الخ )

from lib2to3.pgen2.token import EQUAL
from re import A


location = (13.4125, 103.866667)
print(location[0])

x  = location

#x[0] = 88 ------ error 

# tuple unpacking -------- give the tuple values to multi variable 
y ,z = location #tuple unpacking   # same as x , y = 2 , 3 
print (x)
print(z)


# note : ممكن اكتب التوبل بدون )()
ii = 5 , 4 #same as (5,4)
print(ii)



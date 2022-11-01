## create anoynumus function 

def multiply(x, y):
    return x * y


x = lambda x , y=7: print(x*y)
x(2,2)
#############################3
###map 

def k (x):
    return (x+" "+"hello")

i = ['hello' , 'world']
i = list (map(k,i))
print(i)
x = lambda x : f" {x.title()} "
i = list (map ((lambda x : f" {x.title()} "),i))
print(i)

 ########### filter 
#لازم يرجعلها ترواو فولس فقط 
# الماب بتلف على كل العناصر و بتطبق عليهم شرط
# هذه تلف على العناصر و العنصر الذي يرجع ترو يكون من اجوبه الليست الجديدة

def ir (i):
    return i>10

p =[1 , 5 , 10 , 100 , 1000]
ooo = list(filter(ir,p))
print(ooo)


#or using lambda
lambda x:x>10



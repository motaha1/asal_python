def x(x,y):
    return x+y

print(x(1,2))

#### optional parameter # you must give it value

def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2

print(cylinder_volume(2))

# This will result in an error
# def some_function():
#     word = "hello"

# print(word) ########error

x = 5 
def z(x):
    x+=1
    return x

x=z(x)

print(x)

### قواعد مهمه :
# لا يمكن التعديل داخل الفنكشن على قيمه متغير جلوبال ,ولكن يمكن رؤيته و طباعته
# للتعديل عليها بشكل غير مباشر نقوم بوضع باراميتر للفنكشن ثم نسند القيمه للمتغير القلوبال 

# المتغيرات داخل الفنكشن منفصله كليا عن التي بالخارج حتى لو بنفس الاسم ولا نصل اليها الا داخل الفنكشن نفسه 


def x():
    yield 1 
    yield ' hello'

y = x()


for i in y:
    print(i)

###### 


def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

z = my_range(7)


for i in z:
    print(i)

#print(next(z))  ## stop itteration
###########################################################################

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):

    x=enumerate (lessons,start)
    for i in x: 
        yield i




for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

def chunker(iterable, size):
    
    for i in range(0, len(iterable), size):
        yield iterable[i :  i+size]


for chunk in chunker(range(25), 4):
    print(list(chunk))
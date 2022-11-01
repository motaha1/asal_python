from symbol import return_stmt


a = [1,3,5,4]
print(a.__len__()) 
print(len(a))    
#print(a.__dir__())
#print(dir(a))

##################################################

class hello :
    def __init__(self , name , hello = ['hello' , 'hi']) :
        self.name = name
        self.hello = hello

    def __call__(self):
        print (self.name)
    
    def __str__(self) -> str:
        return f"welcome mr. {self.name}"

    def __repr__(self) -> str:
        return f"hello world"

    def __bool__(self):
        return self.name=='motaha'
    
    def __add__(self , other): #o=o+1

        newhello = self.hello.copy()
        newhello.append(other)
        return hello(self.name, newhello)

    def __iadd__(self,other): #o+=other
        self.hello.append(other)
        return self

    def __getitem__(self , key):  #o[0]
        return self.hello[key]


    def __setitem__(self , key , value):  #o[0] = mohammad
        self.hello[key] = value
        return self



o = hello('motaha')
o()
print(o)
print (repr(o))
print (bool(o))

if o : # depand on bool var
    print('iam from function')

o= o +1
print(o.hello)

o+=5
print(o.hello)

print(o[0])

o[0] = 'mohammad'

print(o.hello)




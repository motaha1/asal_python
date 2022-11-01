# -----------------------------------------------------
# -- Object Oriented Programming => Class Attributes --
# -----------------------------------------------------
# Class Attributes: Attributes Defined Outside The Constructor
# -----------------------------------------------------------


# -------------------------------------------------------------------
# -- Object Oriented Programming => Class Methods & Static Methods --
# -------------------------------------------------------------------
# Class Methods:
# - Marked With @classmethod Decorator To Flag It As Class Method
# - It Take Cls Parameter Not Self To Point To The Class not The Instance
# - It Doesn't Require Creation of a Class Instance
# - Used When You Want To Do Something With The Class Itself
# Static Methods:
# - It Takes No Parameters
# - Its Bound To The Class Not Instance
# - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class
# -----------------------------------------------------------



# static method -------- no  para
# class method ------ cls
#insta method ----- self 

class Member :

        #this is class attribute (مرتبطة بالكلاس نفسه وليس الانستانس )

    name_not_allow = 'hh'
    user_count = 0    # static 

       

    


    def __init__(self,name = 'taha' , age = 6 ):
        # instance attribute 
        self.name =name
        self.age = age
        Member.user_count+=1

    #instance method take self parameter 

        # this is instance method(with self parameter)
    def full_info (self , gender):
        if (gender == 'male') :
            return f"mr.{self.name} {self.age}"
        elif (gender == 'female'):
             return f"miss.{self.name} {self.age}"

    def new_test(self , gender):
        self.gender = gender
        return f"{self.full_info(self.gender)}"

    def test2(self):
        return f"hello {self.gender}"
        

    #this is class method 
    @classmethod
    def test3(cls):
        return "we have "+str(Member.user_count)+" user in our system"
        #return "we have "+str(cls.user_count)+" user in our system"

    @staticmethod
    def say_hello():
        return f"hello from static"

    


    # self pointer to the object i make 

     # self pointer to the object i make 


  
    



one =Member("motaha")

two = Member()
print(dir(Member))
#print(one.__class__)

print(one.name)
print(two.full_info('male'))
print(two.new_test('female'))
print(two.test2())
print(two.test2())

print(Member.test3())
print(Member.user_count)
print(Member.say_hello())


print(Member.full_info(one , 'male'))



### there is defrence between class method and instance method ///// instance var and class var
### there is defrence between class method and instance method  ///// instance var and class var
### there is defrence between class method and instance method  ///// instance var and class var

# static att----------- for all member ------ out of init 
# static method ------- for all member ------- with out self 




        
        
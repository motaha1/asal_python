# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# ----------------------------------------------------------------------
# 1- make function take function parameter
# 2- make nested function with paratmeter = number of parameter in the function under decorator
# 3- in nested function make any thing you want 
# 4- return parameter function 


def hello (func):
    
    def nested ():
        print ('taha')

        func()
        print('mohammad')
    
    return nested


def myDecorator(func):  # Decorator

  def nestedFunc():  # Any Name Its Just For Decoration

    print("Before")  # Message From Decorator

    func()  # Execute Function

    print("After")  # Message From Decorator

  return nestedFunc  # Return All Data


@hello # hello(sayhello)

def sayHello():  # hello(sayhello)

  print("Hello From Say Hello Function")

@myDecorator

def sayHowAreYou():

  print("Hello From Say How Are You Function")

afterDecoration = myDecorator(sayHello)

afterDecoration()

sayHello()

print("#" * 50)

sayHowAreYou()
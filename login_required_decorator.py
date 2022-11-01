import logging
from time import * 

# print(dir(logging))

logging.basicConfig(filename="my_app.log",
                    filemode="a",
                    format="(%(asctime)s) | %(name)s | %(levelname)s => '%(message)s'",
                    datefmt="%d - %B - %Y, %H:%M:%S")


session = {
    'logged_in' :'' ,
    'name' :''

}


def timeit(func):

    def wrapper(*args, **kwargs):

        start = time()

        result =func( * args , **kwargs)

        end = time()
        total_time = end - start
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.8f} seconds')
        #return result
    return wrapper

def login_required(func):

    def wrap (*args , ** kwargs):
        if  session ['logged_in'] :
            return func(*args , **kwargs)

        else :
            my_logger = logging.getLogger(session['name'])

            logging.warning("you need to login first")
        
    return wrap


def login(name):
     
         session['logged_in'] = True
         session['name'] =name

        

def logout():
    session['logged_in'] = False
    session['name']  =''



@timeit
@ login_required 
def open_html():
    i=0
    for number in range(1, 2000000):
        i+=number

    my_logger = logging.getLogger(session['name'])

    my_logger.critical(f"its open")


login('taha')
open_html()
logout()




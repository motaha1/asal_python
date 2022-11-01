from random import random
import Raw_Input as mo
import math



try: 
    x = int (input ('helo  : ----- '))
    print(math.factorial(x))
   
    
except Exception as e : 
    print('error is {}  '.format(e))

finally : 
    print('finally')


print  (__name__)
print(mo.__name__)


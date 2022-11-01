from time import * 

def timeit(func):

  def wrapper(*args, **kwargs):

    start = time()

    func()

    end = time()
    total_time = end - start
    print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.8f} seconds')

    

  return wrapper

@timeit

def bigLoop():
  i=0
  for number in range(1, 200000):
    i+=number

    #print(number)

bigLoop()
from contextlib import contextmanager


@contextmanager
def manage_file(name):
    
    try :
        print('open')
        f = open(name , 'w')
        yield  f

    finally :
        print('close')
        f.close()


with  manage_file('a.txt') as g:
    g.write('motaha')



with manage_file('n.txt') as f : 
    f.write('hello')
    f.write('motaha')
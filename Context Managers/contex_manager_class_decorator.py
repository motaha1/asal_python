from contextlib import contextmanager

class Test:
    
    @contextmanager
    def filee(self , name):

        try :
            print('its open')
            self.f = open(name , 'w')
            yield self.f

        finally:
            print('its close')
            self.f.close()


t = Test ()
with t.filee('u.txt') as f :
    f.write('helloo')



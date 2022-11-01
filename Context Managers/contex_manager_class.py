class Contex :
    def __init__(self , name) :
        self.name = name
    
    def __enter__(self):  #try 
        print('open')
        self.file = open (self.name , 'w')
        return self.file

    
    def __exit__(self , exc_type , exc_val , exc_tb):   #finaly 
        
            print('close')
            self.file.close()

    


c = Contex('o.txt')

with Contex('o.txt') as f :  #f =c or f= contex(o.txt)
    f.write('hellocc p ')





        
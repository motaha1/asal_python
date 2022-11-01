class Undecorated :
    @staticmethod
    
    def get():
        return 'its undecoretor'


x = Undecorated()
print(x.get())


class decorator ():
    def __init__(self, undecoreted):
        self.undecoreted= undecoreted
    
    def get(self):
       return self.undecoreted.get().replace("undecoretor" , "decorated")


y = decorator(x)
print(y.get())

        

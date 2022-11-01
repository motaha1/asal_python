book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

yy = {}

for i in book_title:
    if(i not in yy):
        yy[i]=1
    
    else:
        yy[i]=yy[i]+1
        

print(yy)

##############################3
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

for i in cast :
    print(i)

for key , val in cast.items() :
    print (key + "          "+ val)

o = cast.items()

print(o)




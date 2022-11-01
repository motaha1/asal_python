#### بستخدمها لما بدي اعمل ليست جديدة من ليست موجودة (بدل الفور لوب )

squares = [x**2 for x in range(9) if x % 2 == 0]


squares1=[]
for x in range (0,9):
    if not(x%2 ) :
        squares1.append(x**2)
    else:
        squares1.append( x+2)


squares1=[x**2 if not(x%2 )  else ( x+2)  for x in range (0,9)  ]
print(squares)
print(squares1)



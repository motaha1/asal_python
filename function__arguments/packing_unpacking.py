
print(1, 2, 3, 4)

myList = [1, 2, 3, 5]

print(myList)
print(*myList)  #astric = unpack

def say_hello(*peoples):  # n1, n2, n3, n4
  print(peoples)   #its tuple 
  for name in peoples:

    print(f"Hello {name}")

say_hello("Osama", "Ahmed", "Sayed", "Mahmoud")

def show_details(name, *skills):
  print(skills[1])

  print(f"Hello {name} Your Skills Is: ")

  for skill in skills:

    print(skill)

show_details("Osama", "Html", "CSS", "JS")
show_details("Ahmed", "Html", "CSS", "JS", "Python", "PHP", "MySQL")
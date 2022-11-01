x = input('hello : ')
print(str(x.capitalize()))

y =float (input('y : ')) 
y += 5
print(y)



#############
def main():
    names = input("Enter names separated by commas: ").title().split(",")
    assignments = input("Enter assignment counts separated by commas: ").split(",")
    grades = input("Enter grades separated by commas: ").split(",")

    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
    submit before you can graduate. You're current grade is {} and can increase \
    to {} if you submit all assignments before the due date.\n\n"

    x= zip(names, assignments, grades)
    for name, assignment, grade in x:
        print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))

if __name__=='__main__':
    main()
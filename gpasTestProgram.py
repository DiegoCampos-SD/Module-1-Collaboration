'''
Author: Diego Campos
File name: GPAs Test Program
Description:    This app will be displaying if the student
                made the Dean's List or Honor Roll because
                of the GPA acquired.
'''
#Variables
lastName = input("Student Last Name: ")
while lastName != 'ZZZ':
    firstName = input("Student First Name: ")
    gpa = float(input(f"{lastName}'s GPA: "))
    if gpa >= 3.5:
        print(f"{lastName}, {firstName} made the Dean's List")
    elif gpa >= 3.25:
        print(f"{lastName}, {firstName} made the Honor's Roll")
        
    else:
        print (f"{lastName}, {firstName} did not made Dean's List or Honor's Roll")
    print ("Enter another student's last name bellow: ")
    lastName = input("Student Last Name: ")
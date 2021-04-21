from DBHandler import DBHandler


def validateChoice(choice, range):
    while choice > range:
        choice = int(input(
            "invalid input choice must not be greater than " + str(range) + "\nEnter Choice(1-" + str(range) + ')?'))

db = DBHandler('localhost', 'root', 'versatile', 'mydb')

choice = 0
while(choice!=9):
    print('1. Add Student\t2. Update Student\t3. Delete Student\n4. Get Students By Name\t5. Get Student Data\t6. Student Exists?\n7. Get Student with Highest CGPA\t8. Display All')
    choice = int(input("Enter Choice(1-8): "))
    validateChoice(choice, 8)
    if (choice == 1):
        roll = input("Enter Roll Number : ")
        name = input("Enter Name : ")
        phone = input("Enter Phone # : ")
        email = input("Enter Email : ")
        cgpa = float(input("Enter CGPA : "))
        status = db.addStudent(roll, name, phone, email, cgpa)
        if (status):
            print("operation successfull...")
        else:
            print("operation failed...")
        input("press any key to continue.....")
    if (choice == 2):
        roll = input("Enter Roll Number : ")
        name = input("Enter New Name : ")
        phone = input("Enter New Phone # : ")
        email = input("Enter New Email : ")
        cgpa = float(input("Enter New CGPA : "))
        status = db.updateStudent(roll, name, phone, email, cgpa)
        if (status):
            print("operation successfull...")
        else:
            print("operation failed...")
        input("press any key to continue.....")
    if (choice == 3):
        roll = input("Enter Roll Number : ")
        status = db.deleteStudent(roll)
        if (status):
            print("operation successfull...")
        else:
            print("operation failed...")
        input("press any key to continue.....")
    if (choice == 4):
        records = db.getStudentsByName()
        for r in records:
            print(r)
        input("press any key to continue.....")
    if (choice == 5):
        roll = input("Enter Roll Number : ")
        record = db.getStudentData(roll)
        print(f"CGPA = {record['cgpa']}\nRoll NO = {record['roll']}\nEmail = {record['email']}")
        input("press any key to continue.....")
    if (choice == 6):
        roll = input("Enter Roll Number : ")
        status = db.isStudent(roll)
        if (status):
            print("Student Exists...")
        else:
            print("Students not found...")
        input("press any key to continue.....")
    if (choice == 7):
        record = db.getHighestCGPA()
        print(f"Student with Highest CGPA....\nCGPA = {record['cgpa']}\nRoll NO = {record['roll']}\nEmail = {record['email']}")
        input("press any key to continue.....")
    if (choice == 8):
        db.displayAll()
        input("press any key to continue.....")



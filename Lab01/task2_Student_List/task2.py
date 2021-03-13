stuList=[]
def registerStudent(name,rollno,cgpa,sem):
    stuInfo = {'Name':name,'Rollno':rollno,'CGPA':cgpa,'Semester':sem}
    stuList.append(stuInfo)
    print("Student Added...")
choice = 'Y'
while(choice == 'y' or choice == 'Y'):
    print("Enter Student Info...")
    name = input("Enter Name: ")
    rollno = input("Enter rollno: ")
    cgpa = float(input("Enter CGPA: "))
    sem = int(input("Enter Semester: "))
    registerStudent(name,rollno,cgpa,sem)
    print("List of Students: ",stuList)
    choice = input("Do you want to add more Student(Y/N): ")

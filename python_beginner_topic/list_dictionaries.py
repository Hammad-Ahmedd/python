students=[
    {"name": "Hammad", "age": 19, "grade": "A"},
    {"name": "Ali", "age": 20, "grade": "B"}
    
]

def addStudent():
    name=str(input("Enter Student Name: "))
    age=int(input("Enter Student Age: "))
    grade=str(input("Enter Student grade: "))
    students.append({"name":name,"age":age,"grade":grade})


def viewallstudents():
    studentnumber=0
    for student in students:
        studentnumber=studentnumber+1
        print(f"Student {studentnumber}")
        print(f"Name:{student["name"]} Age:{student["age"]} Grade:{student["grade"]}")

def searchStudentByName():
    searchStudentName=str(input("Enter Student Name: "))
    found=False
    for student in students:
        if searchStudentName==student["name"]:
            print(f"Name:{student["name"]} Age:{student["age"]} Grade:{student["grade"]}")
            found=True
            break
    if not found:
        print("Studend Not Found")    

def deleteStudent():
    deleteStudentName=str(input("Enter Student Name: "))
    found=False
    for student in students:
        if deleteStudentName==student["name"]:
           students.remove(student)
           found=True
           break
    if not found:
        print("Studend Not Found")    


while True:
    print("1)Add new students\n2)View all students\n3)Search for a student by name\n4)Delete a student\n5)Exit the program")
    choice=int(input("Please Select an Option: "))
    if choice==1:
        addStudent()
        print("Student Added Successfully")
    elif choice==2:
        print("ALL the Student")
        print("--------------")
        viewallstudents()
    elif choice==3:
        searchStudentByName()
    elif choice==4:
         deleteStudent()
         print("Student Deleted Successfully")
    elif choice==5:
        print("Good Bye")
        break
    else:
        print(f"The option you {choice} is invalid")
'''
class Person:
    def __init__(self,name):
        self.name=name
        print("Person initialized")


class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        print("Student initialized")
        self.grade=grade


S1=Student("Hammad","A+")
print(S1.name)
print(S1.grade)
'''

'''
class Grandfather:
    def show_grandfather(self):
        print("This is Grandfather")

class Father(Grandfather):
    def show_father(self):
        print("This is Father")

class Son(Father):
    def show_son(self):
        print("This is Son")        

s1=Son()
s1.show_grandfather()
s1.show_father()
s1.show_son()        
'''

'''
class Teacher:
    def show_teacher(self):
        print("This is Teacher")

class Student(Teacher):
    def show_student(self):
        print("This is Student")    

class Person(Teacher,Student):
      def show_person(self):
          print("This is Person")

p1=Person()
p1.show_teacher()
p1.show_student()
p1.show_person()
'''

'''
class ClassA:
      def show(self):
        print("This is ClassA")

class ClassB:
    def show(self):
        print("This is ClassB")

class ClassC(ClassA,ClassB):
      def show(self):
          print("This is ClassC")

c=ClassC()
c.show()       
'''


# Final Challenge Question

class Person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"Person: {self.name}")

class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject            

    def show(self):
        print(f"Teacher of {self.subject}")
        super().show()

class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade          

    def show(self):
        print(f"Student in grade {self.grade}")
        super().show()

class TeachingAssistant(Teacher, Student):
    def __init__(self,name,subject,grade):
        super().__init__(name,subject)
        self.grade=grade

    def show(self):
        print(f"Teaching Assistant Details: {self.name} {self.subject} {self.grade}")
        super().show()

ta = TeachingAssistant("Hammad", "Python", "A+")
ta.show()
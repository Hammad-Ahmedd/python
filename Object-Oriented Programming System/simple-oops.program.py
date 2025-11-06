class student:
    def __init__(self,name,age): # __init__ is the constructure
        self.name=name
        self.age=age
    def printInput(self):
        print(f"Name:{self.name} Age:{self.age}")

student1=student("Hammad",19)
student1.printInput()

'''
class roll:
    a=10

roll1= roll
print(roll.a)    
'''
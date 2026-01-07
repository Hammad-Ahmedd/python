class car:
    wheels=6

    #constructur
    def __init__(self,brand,year):
         self.brand=brand
         self.year=year

    # instance method
    def printwheels(self):
        print(f"{self.brand} is {self.year}")

    @classmethod
    def clsmethod(cls,count):
        cls.wheels = count 

    @staticmethod
    def info():  # static method
        print("Cars are a means of transport.")


c1=car("Toyota",2002)
c1.printwheels()
c1.info()
car.clsmethod(10)
print(c1.wheels)
c1.wheels=20
print(c1.wheels)
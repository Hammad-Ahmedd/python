#🟩 *1. args – Variable Number of Arguments

def argsFun(*number):
    total=0
    for num in number:
        total+=num
    return total
print(argsFun(1,2,3))
    
    
# 🟩 **2. kwargs – Variable Keyword Arguments   

def kwargsFun(**kwargs_dis):
          for key,value in kwargs_dis.items():
                print(f"{key}:{value}")
kwargsFun(name="Hammad",age=18,grade="A+")


# 🟩 3. Lambda Functions (Anonymous Functions)

add=lambda a,b:a*b
print(add(2,4))
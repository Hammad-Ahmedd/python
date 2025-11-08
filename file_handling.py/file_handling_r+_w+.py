with open("demo.txt","r+") as f:
    print("Before Read",f.read())
    f.seek(0)
    f.write("hammad ahmed new")
    f.seek(0)
    print("After Read",f.read())


with open("demo.txt","w+") as f:
    f.write("added")
    f.seek(0)
    print(f.read())

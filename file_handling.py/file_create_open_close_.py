f=open("demo.txt","w")
f.write("I am hammad ahmed")
f.close()

f=open("demo.txt","a")
f.write("\nI like coding")
f.close()

f=open("demo.txt","r")
content=f.readline()
print(content)
f.close()

# 🧩 Example 4 – Using with (best practice)

with open("demo.txt","r") as f:
    content=f.read()
    print(content)

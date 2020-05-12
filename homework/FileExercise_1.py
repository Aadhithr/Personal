a = input("What is the name of your file?")
b = input("What would you like to store on your notepad?")

with open(a, "w") as f:
    f.write(b)
qn = input("Do you want to read the content on your note pad?")
if qn == "yes":
    with open(a, "r") as f:
        print(f.read())
else:
    x = input("Do you want to add any other things to your notepad?")
if x == "no":
    print("Ok bye")
else:
    y = input("What would you like to store on your notepad?")
    with open(a, "w") as f:
        f.write(y)
    with open(a, "r") as f:
        print(f.read())
        
        





    

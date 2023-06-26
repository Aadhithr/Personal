a =int(input("Enter a number"))
b = int(input("How many rows?"))

c = 0
for x in range(b):
    print()
    for i in range(c, (5*a+c), a):
        print(i, end = "\t")
    c = i + a
print("\n", "="*80)

j = 0
for i in range(0, a*5*b, a):
    print(i, end = "\t")
    j = j+1
    if ((j % 5) == 0):
        print()
   
 

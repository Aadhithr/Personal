#StationaryStore.py

#importing turtle
import turtle

#inventory
items = ["Notebooks", "Pencils", "Erasers", "Markers", "Pens"]
inventory = [50, 200, 30, 75, 100]
Unitprice =[5, 1, 1, 2, 3]

Tax = 0.09
for i in range(5):
        print(i+1,". ",items[i])
        
print("Press '0' to finish shopping")

things=[]
count=[]

numItem = 0
item = int(turtle.numinput("Stock",
                        "Select number of the item", 2, 0, 5))
a = item
while (item != 0):
   

    print("We have", inventory[a-1], items[a-1])

    b = "How many "+  items[a-1] + " do you want?"

    c = int(turtle.numinput("Stock",
                        b, inventory[a-1]//4, 1, inventory[a-1]))
    count.append(c)
    inventory[a-1] = inventory[a-1] - c
    

    things.append(item)
    
    numItem+=1
    
    for i in range(5):
        print(i+1,". ",items[i])
        
    print("Press '0' to finish shopping")
    
    item = int(turtle.numinput("Stock",
                        "Select number of item", 2, 0, 5))
    a = item
print("Total number of times bought : ", numItem)

print("="*80)

subtotal = 0
print("Items\t\tUnit Price\tQty\tPrice")
for i in range(numItem):
    print(items[ things[i] - 1 ], "     \t$",Unitprice[things[i] - 1], "\t", count[i], "\t", count[i] * Unitprice[things[i] - 1])
    subtotal = subtotal + count[i] * Unitprice[things[i] - 1]


print("-"*80)
print("\t\t\tSubtotal :$ ", subtotal)
print("Tax (9%) = $",round( (Tax * subtotal) ,2), "\n")
print("-"*80)
print("Total = $", (Tax * subtotal) + subtotal)


print("Thank you for shopping")









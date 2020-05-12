#StationaryStore.py

#importing turtle
import turtle

#inventory
items = ["Notebooks", "Pencils", "Erasers", "Markers", "Pens"]
inventory = [50, 200, 30, 75, 100]
Unitprice =[5, 1, 1, 2, 3]
tax= 9
Tax = 0.09
for i in range(5):
        print(i+1,". ",items[i])
        
print("Press '0' to finish shopping")

a = item = int(turtle.numinput("Stock",
                        "Select number of item", 2, 0, 5))

while (item != 0):
   

    print("We have", inventory[a-1], items[a-1])

    b = "How many "+  items[a-1] + " do you want?"

    count = int(turtle.numinput("Stock",
                        b, inventory[a-1]//4, 1, inventory[a-1]))
    print("Unit price:$",Unitprice[a-1])

    print("Subtotal - ",count, items[a-1],  "= $ ", Unitprice[a-1] * count)

    print("Tax =",tax,"%")

    subtotal = Unitprice[a-1] * count

    TAX = subtotal*Tax

    print("Tax - ", subtotal*Tax)

    print("Total = $",TAX + subtotal,"\n\n")

    for i in range(5):
        print(i+1,". ",items[i])
        
    print("Press '0' to finish shopping")
    
    a = item = int(turtle.numinput("Stock",
                        "Select number of item", 2, 0, 5))    

print("Thank you for shopping")









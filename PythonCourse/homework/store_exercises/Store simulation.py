#Storesimulation.py

#importing turtle
import turtle

#inventory
inventory = 50
notebookprice = 2

#loop
while (inventory > 0):
    
#customer to manager chat
    print("We have" , inventory, "notebooks in stock")

   
#notebook price
  
    print("Each notebook costs $", notebookprice)

#customer to manager chat
    bought = int(turtle.numinput("Store",
                                 "How many notebooks do you want?", 3, 1, inventory ))

#subtotal
    subtotal = int(bought) * notebookprice

#Recipt
    print("Item                   Quantity        Unit Price    Price")
    print("====================================")
    print("Notebook         ", bought,"\t\t", notebookprice,"\t", subtotal)
    print("--------------------------------------------------------------------------")

#subtotal
    print("Subtotal = $",subtotal)

#tax
    tax = 0.09
    print("Tax = $", round((subtotal * tax),2))
    Tax = subtotal * tax

#Total
    print("Total = $", Tax + subtotal)

#inventory
    inventory = inventory - int(bought)
    print("---------------------------------------------")
    print("Inventory")
    print("---------------------------------------------")
    print(inventory,"Notebooks")

print("Sorry out of stock")






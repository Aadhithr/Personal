#inventory
inventory = 50

#customer to manager chat
print("We have" , inventory, "notebooks in stock")

#notebook price
notebookprice = 2
print("Each notebook costs $", notebookprice)

#customer to manager chat
bought = input("How many notebooks do you want : ")

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
newinventory = inventory - int(bought)
print("---------------------------------------------")
print("Inventory")
print("---------------------------------------------")
print(newinventory,"Notebooks")




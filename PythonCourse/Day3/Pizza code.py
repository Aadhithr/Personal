#menu
print("You won the Pizza Hut pizza coupon!")

print("You can decide on how much one pizza is!")

menu = input("What is the cost of one pizza")

#question to customer
pizza = input("How many pizzas do you want?")

#the cost of x pizzas
subtotal  = int(pizza)*float(menu)

#tax
tax = subtotal*0.08

print("Tax  -  " , "$" , tax)

#total cost
totalcost = tax+subtotal

print( "Total cost = " , "$" ,totalcost)




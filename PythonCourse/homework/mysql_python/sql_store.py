import mysql.connector


mydb = mysql.connector.connect(
    user = "root",
    password = "C0de4ever",
    host = "192.168.29.153",
    database = 'sql_store',
    auth_plugin='mysql_native_password'
)

cursor = mydb.cursor()

new_old_cstmer = input("Welcome to the Stationary store\nAre you a old or new customer[Old/New]: ").upper()
if new_old_cstmer == "NEW":
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    state = input("Enter the state you live in[Please abreviate]:")
    password = input("Please make a password: ")

    cursor.execute("INSERT INTO customers(first_name, last_name, email, state)  VALUES('{}', '{}','{}', '{}')"
                .format(first_name, last_name, email, state ))
   
    cust_id = cursor.execute("SELECT customer_id FROM customers WHERE first_name = '{}' AND last_name = '{}' AND email = '{}'"
                             .format(first_name, last_name, email))
    result_id = cursor.fetchall()
    cursor.execute("INSERT INTO cust_passwd VALUES('{}', '{}')".format(result_id[0][0], password))
   
    mydb.commit()
    order = input("Hello {} would you like to place and order[Y/N]:".format(first_name))
else:
    password = input("Enter your password: ")
    cust_id = cursor.execute("SELECT customer_id FROM cust_passwd WHERE password = '{}'".format(password))
    result_id = cursor.fetchall()
    cust_name = cursor.execute("SELECT first_name FROM customers WHERE customer_id = '{}'".format(result_id[0][0]))
    result_name = cursor.fetchall()
    order = input("Hello {} would you like to place and order[Y/N]:".format(result_name[0][0]))
    
if order == "Y":
   products = cursor.execute("SELECT name, unit_price FROM products")
   result_product = cursor.fetchall()
   print("-"*35)
   print("Product\t\t\tUnit_Price")
   print("-"*35)
   for product in result_product:
       print(product[0].ljust(20),  str(product[1]).rjust(10) )
   print("-"*35)
   
   cursor.execute("SELECT order_id FROM orders")
   result_order_id = cursor.fetchall()
   if result_order_id:
       new_order_id = result_order_id[0][-1] + 1
   else:
       new_order_id = 1

  
   while True:
      order = input("Enter the product you want to buy [Please enter exit if you are done shopping]: ").capitalize()
      if order == 'Exit':
          break;
      product_id_check = cursor.execute("SELECT product_id FROM products WHERE name = '{}' ".format(order))
      result_product_id = cursor.fetchall()
      
      if len(result_product_id) == 0:
          print("Please enter a valid item")
          continue;
      
      item_quantity = int(input("Enter the amount of {}s you want to buy".format(order)))
      
      
      cursor.execute("INSERT INTO orders(order_id, customer_id, product_id, quantity) VALUES('{}', '{}', '{}', '{}')"
                     .format(new_order_id, result_id[0][0], result_product_id[0][0], item_quantity ))
      
      mydb.commit()

else:
    print("Thanks for coming!")
  



        
    
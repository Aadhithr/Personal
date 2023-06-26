print("Welcome to my library!")
print("----------------------")

books = ["Harry Potter", "The Hunger Games", "Moby Dick"]
borrowedbooks = {}

def borrowbook(name):
    bookadd = input("What book do you want to borrow: ")
    if bookadd in books:
        print("Book has been borrowed")
        borrowedbooks[name] = bookadd
    books.remove(bookadd)

def returnbook(name):
    bookadd = input("What book do you want to return: ")
    if name in borrowedbooks.keys():
        if borrowedbooks[name] == bookadd:
            print("Book has been returned")
            books.append(bookadd)
            borrowedbooks.pop(name)
        else:
            print("Sorry could not find the book")
    else:
        print("Sorry could not find your name!")




def addbook():
    bookadd = input("What book would you like to add: ")
    books.append(bookadd)


def run():

    while True:

        print('----------------------------------')
        print('1. Display Library Books')
        print('2. Borrow a Book')
        print("3. Return a Book")
        print("4. Donate a Book")
        print("5. Quit")
        username = input("Please enter your name: ")
        action = int(input("Enter Choice: "))

        if action == 1:
            for item in books:
                print(item)
        elif action == 2:
            borrowbook(username)
        elif action == 3:
            returnbook(username)
        elif action == 4:
            addbook()
        elif action == 5:
            quit()
        

run()
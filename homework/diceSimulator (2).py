from random import randint
b = randint(1, 6)
a = input("Do you want to roll the die: ")
while (a=="yes"):
    print("Dice rolling...")
    print(b,"\n")
    a = input("Do you want to roll the die: ")

print("Thanks for playing")







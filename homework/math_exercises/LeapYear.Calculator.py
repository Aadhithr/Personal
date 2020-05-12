year = input("Please enter a year:")

while len(year) != 4:
    print("Error.enter a year please!")
    year = input("Please enter a year:")
if int(year)%4 == 0:
    print("Leap Year")
else: print("Not a Leap Year")


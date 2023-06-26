import turtle
import random
names = []
a = turtle.textinput("Name of Student", "Enter a student's name, click enter to exit")
while a != " ":
    names.append(a)
    a = turtle.textinput("Name of Student", "Enter a student's name, click space and enter to exit")

for x in range(len(names)):
    print(x + 1, ".", names[x])

print("The person who got chose is:",random.choice(names))



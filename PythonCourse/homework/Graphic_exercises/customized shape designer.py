# circle spiral
import turtle
turtle.bgcolor("black")
wn = turtle.Pen()
wn.speed(0)
sides = eval(input("Enter a number between 1 and 6:"))
wn.width(3)
colors = ["red", "yellow", "blue", "green", "white", "orange"]
for x in range(360):
     wn.color(colors[x%sides])

     wn.forward(x)
     
     wn.left(90)



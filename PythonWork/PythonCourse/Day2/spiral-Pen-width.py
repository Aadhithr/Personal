# circle spiral
import turtle
turtle.bgcolor("black")
wn = turtle.Pen()
wn.speed(0)
sides = 6
s = 0.2

colors = ["red", "yellow", "blue", "green", "white", "orange"]
for x in range(360):
     wn.color(colors[x%sides])
    # if ((x % 30) == 0) :
     wn.width(s)
     

     wn.forward(2*x)
     
     wn.left(91)



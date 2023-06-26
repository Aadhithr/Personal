# circle spiral
import turtle

wn = turtle.Pen()
wn.speed(0)
colors = ["red", "yellow", "blue", "green"]
for x in range(200):
     wn.color(colors[x%4])
     #wn.bg("black")
     wn.forward(2*x)
     
     wn.left(91)



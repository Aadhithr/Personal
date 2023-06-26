# circle spiral
import turtle

wn = turtle.Pen()
wn.speed(0)

for x in range(200):
     wn.color(240)
     #wn.bg("black")
     wn.circle(x-200)
     wn.left(360)

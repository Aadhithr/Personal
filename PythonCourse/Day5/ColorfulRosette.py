import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
t.width(3)
numcircles = int(turtle.numinput("Number of Circles", "How many circles in your rosette?", 6))
for x in range(numcircles):
    t.pencolor("yellow")
    t.circle(50)
    t.pencolor("red")
    t.circle(100)
    t.left(360/numcircles)

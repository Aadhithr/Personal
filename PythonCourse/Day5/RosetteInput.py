import turtle
t = turtle.Pen()
t.speed(0)
numcircles = int(turtle.numinput("Number of Circles", "How many circles in your rosette?", 6))
for x in range(numcircles):
    t.circle(100)
    t.left(360/numcircles)

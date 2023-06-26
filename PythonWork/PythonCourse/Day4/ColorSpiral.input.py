#colorSpiral.input
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")

colors = ["blue" , "red", "green", "aqua", "white", "orange",
                 "purple", "gray", "brown", "yellow"]

sides = int( turtle.numinput("Number of sides",
                                               " How many sides do you want (1-10)?", 4 , 1, 10))

for x in range(400):
    t.pencolor(colors[x%sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 5)
    t.width(x * sides / 200)
               

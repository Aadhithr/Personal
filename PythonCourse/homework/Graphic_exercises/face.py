#turtle screen
import turtle

wn = turtle.Screen()
wn.title("My Face")

#head
x = turtle.Turtle()
x.shape("circle")
x.color("brown")
x.shapesize(stretch_wid=10, stretch_len=10)

#eye
y = turtle.Turtle()
y.shape("circle")
y.color("blue")
y.penup()
y.goto(-40, 30)

#eye
z = turtle.Turtle()
z.shape("circle")
z.color("blue")
z.penup()
z.goto(40, 30)

#nose
x = turtle.Turtle()
x.setheading(90)
x.color("black")
x.penup()
x.forward(0)

#mouth
t = turtle.Turtle()
t.penup()
t.goto(-45, -50)
t.backward(0)
t.color("red")
t.setheading(-45)
t.begin_fill()
t.circle(66, 90)
t.end_fill()
t.hideturtle()










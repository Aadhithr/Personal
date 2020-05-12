import turtle

wn = turtle.Screen()
wn.title("My Face")

x = turtle.Turtle()
x.shape("circle")
x.color("brown")
x.shapesize(stretch_wid=10, stretch_len=10)

x = turtle.Turtle()
x.shape("circle")
x.color("blue")
x.penup()
x.goto(-40, 30)

x = turtle.Turtle()
x.shape("circle")
x.color("blue")
x.penup()
x.goto(40, 30)

x = turtle.Turtle()
x.setheading(90)
x.color("black")
x.penup()
x.forward(0)


x = turtle.Turtle()
x.penup()
x.goto(-45, -50)
x.backward(0)
x.color("red")
x.setheading(-45)
x.begin_fill()
x.circle(66, 90)
x.end_fill()
x.hideturtle()

def dragging(x, y):
    x.ondrag(None)
    x.setheading(x.towards(x, y))
    x.goto(x, y)
    x.ondrag(dragging)

def main():
    x.ondrag(dragging)

main()












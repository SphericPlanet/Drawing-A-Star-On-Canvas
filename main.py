import turtle

turtle.title("A Star On Canvas")

screen = turtle.Screen()
screen.bgcolor("Cyan")

##Turtle
t = turtle.Turtle()
t.pencolor("Green")
t.shape("turtle")
t.pensize(5)
t.speed(1)

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

t.right(150)
t.penup()
t.forward(50)
t.right(90)

t.pendown()
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)

turtle.done()

import turtle

k = turtle.Turtle()
k.getscreen().bgcolor("white")
k.speed(5)
k.penup()
k.back(100)
k.pendown()

k.color("yellow", "green")
k.begin_fill()
k.pensize(5)
k.forward(80)
k.left(45)
k.forward(100)
k.right(90)
k.forward(100)
k.left(45)
k.forward(100)
k.right(132)
k.forward(100)
k.left(65)
k.forward(100)
k.right(135)
k.forward(150)
k.left(49)
k.forward(125)
k.right(135)
k.forward(100)
k.left(65)
k.forward(110)
k.end_fill()

k.penup()
k.back(450)
k.pendown()

k.speed(10)
k.color("Red", "blue")
k.begin_fill()
for i in range(45):
    k.forward(450)
    k.left(168)
k.end_fill()

turtle.color('deep pink')
style = ('Courier', 30, 'italic')
turtle.write('Cavendish', font=style, align='center')
turtle.hideturtle()
turtle.done()

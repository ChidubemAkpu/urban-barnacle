import turtle

screen = turtle.Screen()
diagram = turtle.Turtle()

diagram.pensize(3)

screen.bgcolor("lightgreen")
diagram.color("blue")

for i in range (5):

    for i in range(5):
        diagram.forward(100)
        diagram.right(144)
    
    diagram.penup()
    diagram.forward(350)
    diagram.right(144)
    diagram.pendown()

screen.mainloop()
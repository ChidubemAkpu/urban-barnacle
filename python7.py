import turtle

screen = turtle.Screen()
diagram = turtle.Turtle()
number = 20
diagram.pensize(3)

screen.bgcolor("lightgreen")
diagram.color("red")

    

def draw_squares():

    for i in range(4):
        diagram.forward(80)
        diagram.left(90)

for i in range(number):
    draw_squares()
    diagram.right(18)
    

screen.mainloop()
import turtle
import math as mt
moved = mt.sqrt(10**2 + 10**2)


screen = turtle.Screen()
diagram = turtle.Turtle()
diagram.pensize(2)
screen.bgcolor("lightgreen")
diagram.color("red")

number = int(screen.numinput("NUMBER OF SQUARES",'HOW MANY SQUARES?',default=2,minval=0,maxval=None))


def draw_squares():
    for i in range(4):
        diagram.forward(size)
        diagram.left(90)

size = 20
for i in range(number):
    draw_squares()

    diagram.right(135)
    diagram.penup()
    diagram.forward(moved)
    diagram.left(135)
    diagram.pendown()
    size = size + 20

    
screen.mainloop()


    



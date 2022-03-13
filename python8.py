import turtle

screen = turtle.Screen()
diagram = turtle.Turtle()

screen.bgcolor("lightgreen")
diagram.color("red")

size = 5
for i in range(50):
    diagram.forward(size)
    diagram.right(90)
    size = size + 2
    

screen.mainloop()


    

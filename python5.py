#QUESTION 1 OF CHAPTER 4

import turtle

screen = turtle.Screen()
diagram = turtle.Turtle()


#Pen screen properties

number_of_squares = int(screen.numinput("NUMBER OF SQUARES","INPUT NUMBER OF SQUARES",default=None,
minval = 0 , maxval = None))

pen_size = int(screen.numinput("PEN SIZE","Choose a pen size",default=None,
minval = 0 , maxval = None))

size = int(screen.numinput("SQUARE'S SIZE","CHOOSE A LENGTH FOR EACH SIDE",default=None,
minval = 0 , maxval = None))

bg_color = screen.textinput("BACKGROUND COLOUR","CHOOSE A BACKGROUND COLOUR")

pen_color = screen.textinput("PEN COLOUR","CHOOSE A PEN COLOUR")

diagram.pensize(pen_size)
screen.bgcolor(bg_color)
diagram.color(pen_color)

diagram.shape("blank")



def draw_square(size):
    for i in range(4):
        diagram.forward(size)
        diagram.left(90)

for i in range(number_of_squares):
    
    draw_square(size)
    
    diagram.penup()
    diagram.forward(1.2* size)
    diagram.pendown()
    

screen.mainloop()




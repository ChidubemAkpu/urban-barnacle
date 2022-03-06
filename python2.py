#Day 2
#Creating turtle diagrams

#Turtle projects

# Creating a diagram
import turtle
import math as mt


screen = turtle.Screen()
diagram = turtle.Turtle()

#Colour specifications
bg_color = screen.textinput(title="Backgound color",prompt="What is your preferred backgound color? ")
line_color = screen.textinput(title="Line color",prompt="What shape's line color do you prefer")
screen.bgcolor(bg_color)

n1 = screen.numinput(title='First triangle side',prompt="Choose a length",default=None,
minval=0,maxval=None)

n2 =  screen.numinput(title='second triangle side',prompt="Choose a length",default=None,
minval=0,maxval=None)

#Angle of rotation
hypothenus = mt.sqrt(n1**2 + n2**2)
rad_angle = mt.atan(n1/n2)
deg_angle = (180 * rad_angle)/ mt.pi
required_angle = 180 - deg_angle
diagram.color(line_color)

#Chose pensize
pen_size =  screen.numinput(title='Pen size',prompt="Choose a pen size",default=None,
minval=None,maxval=None)

#Code implementation
diagram.pensize(pen_size)
diagram.forward(n1)
diagram.left(90)
diagram.forward(n2)
diagram.left(required_angle)
diagram.forward(hypothenus)


screen.mainloop()







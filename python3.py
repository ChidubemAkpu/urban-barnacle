#For loop
#Drawing regular polygons of any sides

import turtle

screen = turtle.Screen()
diagram = turtle.Turtle()

diagram.shape("blank")
diagram.speed(1)

poly_num_side =int(screen.numinput(title="Polygon's side number",
prompt="What is the polygon's number of sides?",default=None,minval=3,maxval=None))


poly_side_length = int(screen.numinput(title="Polygon's sides lenths",
prompt="What is the polygon's sides length?",default=None,minval=0,maxval=None))

poly_int_angle = int(180 * (poly_num_side - 2) / poly_num_side)


for i in range(poly_num_side):
    diagram.forward(poly_side_length)
    diagram.left(180 - poly_int_angle)

screen.mainloop()
    


x = float(input("Input the length of one side"))
y = float(input("Input the length of the other side"))
z = float(input("What is the value of Z?"))

def is_rightangled():
    if z == (x**2 + y**2) ** 0.5:
        print("It is a right angled triangle")
    elif x == (z**2 + y**2) ** 0.5 :
        print("It is a right-angled triangle")
    elif y == (z**2 + x**2) ** 0.5:
        print("It is a right-angled triangle")
    else:
        print("It is not a right-angled triangle")

is_rightangled()

import math
a = math.sqrt(2.0)
print(a,a*a)
print(a*a == 2.0)







    
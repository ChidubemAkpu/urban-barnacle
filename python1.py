#...Journey through coding-Day 1

#'type' verifies the data type

print(type("Hello world")) 
print(type(20))
print(type(20.0))
print(type('Hello world'))
print(type(3.2))
print(type(True))
print(type(False))
print(type(3 > 2))
print(type(3 + 2))
print(type(3.0 + 2.0))
print(type('3 + 6'))

#printing strings and comparing types of quotes

#They can only print a line
print('It is cool i get this printed on the terminal')
print("It is cool i get this printed on the terminal")

#They can print many lines without having to introduce more print classes
print('''It is cool
i get this printed
on the terminal''')

print("""It is cool
i get this printed 
on the terminal""")

print('I\'m not your normal guy')

#Creating variables and using them in our python programs
#strings
first_variable = 'The first variable'
second_variable = 'the second variable'
conjuction = ' is bether than '
sentence = first_variable + conjuction + second_variable
#Numerics
first_math_value = 45
second_math_value = 35
addition = first_math_value + second_math_value
subtraction = first_math_value - second_math_value
product = first_math_value * second_math_value
division = first_math_value / second_math_value
floor_division = first_math_value // second_math_value
modulus = first_math_value % second_math_value

print(first_variable)
print(second_variable)
print(conjuction)
print(sentence)

print(first_math_value)
print(second_math_value)
print(addition)
print(subtraction)
print(product)
print(division)
print(floor_division)
print(modulus)

print('The value',modulus,'is the remainder gotten by dividing 45 by 35')
print(floor_division, 'Was gotten by dividing 45 by 35 and removing the fractional part')
print('hence, 45 can be gotten by doing',floor_division * 35 + modulus, "Cool stuff!")

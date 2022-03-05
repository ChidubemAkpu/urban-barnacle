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
print(round(division,3))
print(floor_division)
print(modulus)

print('The value',modulus,'is the remainder gotten by dividing 45 by 35')
print(floor_division, 'Was gotten by dividing 45 by 35 and removing the fractional part')
print('hence, 45 can be gotten by doing',floor_division * 35 + modulus, "Cool stuff!")

#Exercise 2.4
#1
word1 = "All"
word2 = " work"
word3 = " and"
word4 = " no"
word5 = " play"
word6 = " makes"
word7 = " Jack"
word8 = " a"
word9 = " dull"
word10 = " boy"
word_general = word1 + word2 + word3 + word4 + word5 + word6 + word7 + word8 + word9 + word10
print(word1,word2,word3,word4,word5,word6,word7,word8,word9,word10)
print(word_general)

#2
print(6 * (1-2))

#3

print(word_general) #works
#print(word_general) #doesn't work

#4

bruce = 6
print(bruce + 4)

#5
p = 1000
n = 12
r = 8
t = int(input("What is the number of years? "))

p_new = p * (1 + r / n)**(n*t)
print(p_new)

#6
print(5 % 2)
print(9 % 5)
print(15 % 12)
print(12 % 15)
print(6 % 6)
print(0 % 7)
#print(7 % 0)

#7
print((2 + 51) % 12)

#8
time_now = int(input("What time is it now? "))
number_of_hours = int(input("How many hours are you going to rest? "))
new_time = (time_now + number_of_hours) % 12
print("The alarm will ring at exactly when the hour hand is at", new_time)


#Puzzle solution popular on twitter
#If the squareroot of a 4-digit number abcd is cd, find a + b + c + d

for num in range(1000, 10000):
    if (num ** 0.5) == (num % 100) :
        break

print("abcd is %d and cd is %d"%(num,num % 100),end = " ")  

sum_of_digits = 0
count = 0
while count < 4:
    number = num % 10
    num = (num - number) // 10
    sum_of_digits += number
    count += 1

print("while a+b+c+d is %d"%sum_of_digits)





        

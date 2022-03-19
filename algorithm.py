number_of_values = int(input("How many values? "))
values_container = []

#Collect all inputs into a container named values_container
for values in range(number_of_values):
    number = int(input("Value? "))
    values_container.append(number)

#sort list in descending order
values_container.sort(reverse = True)
print("In descending order:",values_container)

#Sort list in ascending order
values_container.sort()
print("In ascednsing order:",values_container)




#Calculating standard deviation

#Tells about the number of values in the data set
number_of_values = int(input("How many values? "))
data_sets = []

#Appending each value into data sets
for num in range(number_of_values):
    print("value%d"%(num + 1), end = " ")
    value = float(input())
    data_sets.append(value)

#sum of sample data and their mean
sum_of_values = 0
for num in data_sets:
    sum_of_values += num
mean_of_data = sum_of_values / number_of_values

#Where the deviations were squared
sum_of_squared_deviations = 0
for num in data_sets:
    deviation = num - mean_of_data
    squared_deviations = deviation ** 2
    sum_of_squared_deviations += squared_deviations

#degree of freedom, variance and standard deviation
degree_of_freedom = number_of_values - 1
variance = round(sum_of_squared_deviations / degree_of_freedom, 3)
standard_deviation = round(variance ** 0.5, 3)

#Where the actual printing of results take place
print("The standard deviation of",data_sets,"is",standard_deviation,end = " ")
print("with variance",variance)





        
        
    




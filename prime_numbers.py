#Print the month and the number of days it has.

days_with_30 = ["April","June","September","November"]
days_with_31 = ["January","March","May","July","August","October","December"]
feb_list = ["February","february","FEBRUARY"]
months_space = []
months_list = []
number_of_months = int(input("How many months do you wanna verify their number of days?"))

if number_of_months <= 0:
    print("It must be a number greater than 0")
elif number_of_months > 12:
    print("We have only 12 months in a year")
else:
    for i in range(number_of_months):
        month = str(input("Which month do you want to find its number of days? "))
        months_space.append(month)

for month in months_space:
    if month in feb_list:
        check_year_type = int(input("Input year "))
        if check_year_type % 4 == 0:
            months_list.append("February has 29 days")

        else:
            months_list.append("February has 28 days")

    else:
        for num in days_with_30:
            if month == num or month == num.upper() or month == num.lower():
                months_list.append("%s has 30 days"%num) 

        for num in days_with_31:
            if month == num or month == num.upper() or month == num.lower():
                months_list.append("%s has 31 days"%num)

print(months_list)


                    

                    
                



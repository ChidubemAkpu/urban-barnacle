#Function with day name and number of days spent as argument bringing up corresponding end day
day1, day2, day3, day4 = "Sunday","Monday","Tuesday","Wednesday"
day5, day6, day7 = "Thursday", "Friday" , "Saturday" 

def condition():
    """Returns end day"""
    if day_calc == 0:
        return day1
    elif day_calc == 1:
        return day2
    elif day_calc == 2:
        return day3
    elif day_calc == 3:
        return day4
    elif day_calc == 4:
        return day5
    elif day_calc == 5:
        return day6
    elif day_calc == 6:
        return day7

def day_add(day,num):

    global day_calc
    if day == "Sunday":
        day_calc = (0 + num) % 7
        return condition()


    elif day == "Monday":
        day_calc = (1 + num) % 7
        return condition()

    elif day == "Tuesday":
        day_calc = (2 + num) % 7
        return condition()

    elif day == "Wednesday":
        day_calc = (3 + num) % 7
        return condition()

    elif day == "Thursday":
        day_calc = (4 + num) % 7
        return condition()

    elif day == "Friday":
        day_calc = (5 + num) % 7
        return condition()

    elif day == "Saturday":
        day_calc = (6 + num) % 7
        return condition()
   
print(day_add("Friday",4))


        






            
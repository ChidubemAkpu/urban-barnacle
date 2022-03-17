from sys import _getframe

def test(did_pass):
    """print the result of a test"""
    linenum = _getframe(1).f_lineno  #get the caller's line number
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} failed.".format(linenum)
    print(msg)

def test_suite():
    """Run the suite of tests for code in this module (this file)"""
    test(abs(17) == 17)
    test(abs(-17)== -17)
    test(abs(18) == -18)

test_suite()

def turn_clockwise(give_out):
    if give_out == "N":
        return "E"
    elif give_out == "E":
        return "S"
    elif give_out == "S":
        return "W"
    elif give_out == "W":
        return "N"

test(turn_clockwise("N"))
test(turn_clockwise(40) == None)

def day_num(number):
    if number == 0:
        return "Sunday"
    elif number == 1:
        return "Monday"
    elif number == 2:
        return "Tuesday"
    elif number == 3:
        return "Wednesday"
    elif number == 4:
        return "Thursday"
    elif number == 5:
        return "Friday"
    elif number == 6:
        return "Saturday"

test(day_num(0))
test(day_num(1))
test(day_num(2))
test(day_num(3))
test(day_num("Tuesday") == 2)
test(day_num("Sunday") == 0)

#Function with day name and number of days spent as argument bringing up corresponding end day
day1, day2, day3, day4 = "Sunday","Monday","Tuesday","Wednesday"
day5, day6, day7 = "Thursday", "Friday" , "Saturday" 

def day_add(day,num):
    if day == "Sunday":
        day_calc = (0 + num) % 7
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

    elif day == "Monday":
        day_calc = (1 + num) % 7
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


    elif day == "Tuesday":
        day_calc = (2 + num) % 7
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


    elif day == "Wednesday":
        day_calc = (3 + num) % 7
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

    
    elif day == "Thursday":
        day_calc = (4 + num) % 7
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

    
    elif day == "Friday":
        day_calc = (5 + num) % 7
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

    
    elif day == "Saturday":
        day_calc = (6 + num) % 7
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


    
    
print(day_add("Sunday",4))


        






            


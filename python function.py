#Function with day name and number of days spent as argument bringing up corresponding end day

day_dict = {
    "Sunday":0,
    "Monday":1,
    "Tuesday":2,
    "Wednesday":3,
    "Thursday":4,
    "Friday":5,
    "Saturday":6
            }
start_day = str(input("What is the start day? "))
accurate_case = start_day.capitalize()
day_list = list(day_dict)

try:
    def day_add(accurate_case,num):
        day_calc = (day_dict[accurate_case] + num) % 7
        return day_list[day_calc]
    
    print(day_add(accurate_case,4))

except:
    print('Enter correct')



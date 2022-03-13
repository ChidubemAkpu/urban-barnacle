#PRINTS RETURN DAY WHEN DAY NUMBER IS GIVEN



day_number = int(input("When are you going??"))

#decisions

if day_number >6 or day_number < 0:
    print("This is out of range. Range is 0-6 inclusive.")

else:
    number_of_nights = int(input("How many nights will you spend?"))

    return_day = (day_number + number_of_nights) % 7

    def days_of_the_week():

        if return_day == 0 :
            print("you will be back on Sunday")
        elif return_day == 1:
            print("you will be back on Monday")
        elif return_day == 2:
            print("you will be back on Tuesday")
        elif return_day == 3:
            print("you will be back on Wednesday")
        elif return_day == 4:
            print("you will be back on Thursday")
        elif return_day == 5:
            print("you will be back on Friday")
        elif return_day == 6:
            print("you will be back on Saturday")

    days_of_the_week()



    


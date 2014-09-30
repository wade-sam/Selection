#Sam Wade
# Development exercise 3: rate of pay
# 30/9/14

hours = int(input("please enter the amount of hours ouve worked this week"))
money_hour = int(input("please enter the amount of money ou earn per hour"))
if hours <= 39:
        total_money = money_hour * hours
        print("you will get £{0} this week.".format(total_money))

elif 40 < hours <= 60:
              extra_hours = 1.5 * total_money
              print("you will get £{1} this week.".format(extra_hours))
else:
    print("your entry is invalid")
    
            


#Sam Wade
#Extension exercises
day = int(input("Please enter the day"))
month = int(input("Please enter the month"))
year = int(input("Please enter the year"))

if day ==1 or day == 21 or day == 31:
    day_sufix = "st"
elif day ==2 or day == 22:
    day_suffix = "nd"
elif day == 3 or day == 23:
    day_suffix = "rd"
elif 4 <= day <=  20 or 24 <= day <= 30:
    day_suffix = "th"

if month == 1:
    name_month = "January"
elif month == 2:
    name_month = "February"
elif month == 3:
    name_month = "March"
elif month == 4:
    name_month = "April"
elif month == 5:
    name_month = "May"
elif month == 6:
    name_month = "June"
elif month == 7:
    name_month = "July"
elif month == 8:
    name_month = "August"
elif month ==9:
    name_month = "September"
elif month == 10:
    name_month = "October"
elif month == 11:
    name_month = "November"
elif month == 12:
    name_month = "December"
else:
    print("Sorry that is incorect")

if year == 1:
    name_year = "2001"
elif year ==2:
    name_year = "2002"
elif year ==3:
    name_year = "2003"
elif year ==4:
    name_year = "2004"
elif year ==5:
    name_year = "2005"
elif year ==6:
    name_year = "2006"
elif year ==7:
    name_year = "2007"
elif year ==8:
    name_year = "2008"
elif year ==9:
    name_year = "2009"
elif year ==10:
    name_year = "2010"
elif year ==11:
    name_year = "2011"
elif year ==12:
    name_year = "2012"
elif year ==13:
    name_year = "2013"
elif year ==14:
    name_year = "2014"
else:
    print("Sorry thats incorect")

print ("the day is the {0}{1} of {2} {3} .".format(day, day_suffix, name_month, name_year))
       
       
    
    

    
    
    
    

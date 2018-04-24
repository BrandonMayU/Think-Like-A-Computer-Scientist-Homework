# 3 criteria must be taken into account to identify leap years:The year is evenly divisible by 4;If the year can be
# evenly divided by 100, it is NOT a leap year, unless;The year is also evenly divisible by 400. Then it is a leap
# year.Write a function that takes a year as a parameter and returns True if the year is a leap year, False otherwise.

import calendar #Using calendar import allows you to write more effcient code and remove the need to logical statements

print("We will tell you if a year is a leap year or not")
year = int(input("Please provide a year: "))

if(calendar.isleap(year) == True): #We see what the func returns and then wrap it with logic for an output
    print("Correct, that is a leap year")
else:
    print("False, ", year, " is not a leap year")
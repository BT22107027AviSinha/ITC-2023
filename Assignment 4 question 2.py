y = int(input("Enter the year here:"))#The user enters the year as an integer input

if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0: #This is the required equation which specifies two conditions for an year to be a leap year, either the year is divisible by 4 and not divisible by 100 or it is divisible by 400 if the year is divisible by 100.

    print(y, "The year is a leap year")

else:
    print(y, "The year is not a leap year")


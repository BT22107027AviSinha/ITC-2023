m = float(input( "Enter your Grade here:"))  #We take the input of marks in type 'float' from the user

#These are the required constraints on the Grade assigned to diferent ranges of marks
if m>=0 and m<25:
    print("Your Grade is F")

elif m>=25 and m<45:
    print("Your Grade is E")

elif m>=45 and m<50:
    print("Your Grade is D")

elif m>=50 and m<60:
    print("Your Grade is C")

elif m>=60 and m<80:
    print("Your Grade is B")

elif m>=80 and m<=100:
    print("Your Grade is A")

else:
    print("Invalid")#The value must lie between 0 to 100 in terms of marks hence, if any other value is entered the program prints it as invalid


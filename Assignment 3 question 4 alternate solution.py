a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a > b and a > c:
    greatest = num1
elif b > a and b > c:
    greatest = b
else:
    greatest = c

print("The greatest of the three numbers is:", greatest)

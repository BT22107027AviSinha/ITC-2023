# Take input of three sides of a triangle
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

# Check if the given lengths can form a triangle
if a + b > c and a + c > b and b + c > a:
    print("Yes, these lengths can form a triangle.")
else:
    print("No, these lengths cannot form a triangle.")

A = float(input("Enter the first number: "))  #takes the input of the three numbers in float type
B = float(input("Enter the second number: "))
C = float(input("Enter the third number: "))

print("First number:", A)
print("Second number:", B)#prints the three numbers for user reference
print("Third number:", C)
#if statements to establish the conditions as per requisite where the three numbers can be equal greater than or lesser than with respect to each other
if A > B and A > C:
    greatest = A
elif B > A and B > C:
    greatest = B
elif C > A and C > B:
    greatest = C
elif A == B == C:
    greatest = A
elif A == B and A > C:
    greatest = A
elif A == C and A > B:
    greatest = A
elif B == C and B > A:
    greatest = B
else:
    print("Code Blast!!")#prints code blast if there is some error which is unlikely but is a fail safe

print("The greatest of the three numbers is:", greatest)#prints the greatest number of the three

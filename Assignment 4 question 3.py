import random #We import the 'random' library to randomize the question choosing process

for i in range(1,11): #We assign 10 questions to the user in the range 1 to 11
    #We compute 10 different random questions for the user and since it is a multiplication game for kids the range in which the values of the two numbers lie is in between 1 and 10
    a = random.randint(1,10)
    b = random.randint(1,10)
    answer = a*b
    user_answer = int(input(f"{i}. What is {a} x {b}?"))#This provides user with an interface to enter their answer
    #These 'if' statements check whether the answer entered by the user is the same as the answer computed by the program
    if user_answer == answer:
        print("The answer is correct")

    else:
        print("The answer is incorrect")


print("Game Over")


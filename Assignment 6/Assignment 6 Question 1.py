def is_perfect_number(number):
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
    if divisor_sum == number:
        return True
    else:
        return False


num = int(input("Enter your number here ",))
number = num #checking if the number is a perfect number or not
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

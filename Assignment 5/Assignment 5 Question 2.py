def print_divisible_numbers(start, end, divisor):
    divisible_numbers = []
    for num in range(start, end + 1):
        if num % divisor == 0:
            divisible_numbers.append(num)
    return divisible_numbers

# Example usage
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
divisor = int(input("Enter the number to check divisibility: "))

result = print_divisible_numbers(start, end, divisor)
print("Numbers divisible by", divisor, "within the range", start, "to", end, "are:", result)

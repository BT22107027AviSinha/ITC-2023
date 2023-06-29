numbers = []

# Input 10 integer values from the user
for i in range(10):
    num = int(input("Enter an integer value: "))
    numbers.append(num)

# Initialize counters for each category
positive_count = 0
negative_count = 0
odd_count = 0
even_count = 0
number_counts = {}

# Iterate through the numbers list
for num in numbers:
    # Check if the number is positive
    if num > 0:
        positive_count += 1
    # Check if the number is negative
    elif num < 0:
        negative_count += 1

    # Check if the number is odd
    if num % 2 != 0:
        odd_count += 1
    # Check if the number is even
    else:
        even_count += 1

    # Count the occurrences of each number
    if num in number_counts:
        number_counts[num] += 1
    else:
        number_counts[num] = 1

# Print the results
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Odd numbers:", odd_count)
print("Even numbers:", even_count)
print("Number of times each number occurs in the list:")
for num, count in number_counts.items():
    print(num, "occurs", count, "time(s)")

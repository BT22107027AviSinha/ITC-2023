start = 1
end = 500

print("Numbers between", start, "and", end, "that are multiples of 7 and divisible by 11:")

for num in range(start, end + 1):
    if num % 7 == 0 and num % 11 == 0:
        print(num)

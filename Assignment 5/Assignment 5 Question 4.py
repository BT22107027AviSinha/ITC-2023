n = 5  # Number of rows in the pattern

# Construct the upper half of the pattern
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

# Construct the lower half of the pattern
for i in range(n - 1):
    for j in range(n - i - 1):
        print("*", end=" ")
    print()

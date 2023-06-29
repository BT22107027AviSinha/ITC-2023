def print_alphabet_triangle(rows):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0
    for i in range(1, rows + 1):
        for j in range(i):
            print(alphabet[count % len(alphabet)], end="")
            count += 1
        print()

# Example usage
num_rows = int(input("Enter the number of rows: "))
print_alphabet_triangle(num_rows)

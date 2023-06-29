def print_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1]  # First element of each row is always 1

        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(len(prev_row) - 1):
                # Each element in the current row (except first and last)
                # is the sum of the two elements above it in the previous row
                row.append(prev_row[j] + prev_row[j + 1])

            row.append(1)  # Last element of each row is always 1

        triangle.append(row)

    # Print Pascal's triangle
    for row in triangle:
        print(" ".join(map(str, row)))

# Example usage
n = 6
print(f"First {n} rows of Pascal's triangle:")
print_pascals_triangle(n)

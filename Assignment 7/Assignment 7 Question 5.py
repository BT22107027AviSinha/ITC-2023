def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    count = 0

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            count += 1

            # Check for other occurrences on the left side
            i = mid - 1
            while i >= 0 and arr[i] == target:
                count += 1
                i -= 1

            # Check for other occurrences on the right side
            i = mid + 1
            while i < len(arr) and arr[i] == target:
                count += 1
                i += 1

            return count

        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return count

# Prompt the user to enter the array
array = list(map(int, input("Enter the integer array (comma-separated): ").split(',')))

# Sort the array
sorted_array = sorted(array)

# Print the sorted array
print("Sorted array:", sorted_array)

# Prompt the user to enter the element to search
target = int(input("Enter the element to search: "))

# Perform binary search and count the number of occurrences
occurrences = binary_search(sorted_array, target)

# Print the number of occurrences
if occurrences > 0:
    print(f"Number of occurrences of element {target} is: {occurrences}")
else:
    print(f"Element {target} not found in the array.")

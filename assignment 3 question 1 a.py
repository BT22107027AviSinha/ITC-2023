# Define the input string
input_string = "Python is a case sensitive language"

# Find the length of the input string
length = len(input_string)
print("Length of the input string:", length)

# Reverse the order of the string in one line code
reverse_string = input_string[::-1]
print("Reverse of the input string:", reverse_string)

# Using Slice function store “a case sensitive” in new string
new_string = input_string[11:27]
print("New string:", new_string)

# Replace “a case sensitive” with “object oriented”
new_input_string = input_string.replace("a case sensitive", "object oriented")
print("New input string:", new_input_string)

# Find index of substring “a” in the given input string
index_a = input_string.index("a")
print("Index of 'a':", index_a)

# Remove the white spaces from the given input string
stripped_string = input_string.replace(" ", "")
print("Stripped string:", stripped_string)



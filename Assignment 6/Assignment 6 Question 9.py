class ParenthesesValidator:
    def __init__(self, string):
        self.string = string

    def is_valid(self):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in self.string:
            if char in mapping:
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0

# Example usage
valid_string = "()[]{}"
invalid_string = "({[)]"

validator = ParenthesesValidator(valid_string)
print(f"Is '{valid_string}' valid? {validator.is_valid()}")

validator = ParenthesesValidator(invalid_string)
print(f"Is '{invalid_string}' valid? {validator.is_valid()}")

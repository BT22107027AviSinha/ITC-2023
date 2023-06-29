class ZeroSumFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_zero_sum_elements(self):
        result = []
        n = len(self.numbers)

        # Sort the numbers in ascending order
        self.numbers.sort()

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = self.numbers[i] + self.numbers[left] + self.numbers[right]
                if current_sum == 0:
                    result.append((self.numbers[i], self.numbers[left], self.numbers[right]))
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result


numbers = [1, -2, 3, -4, 5, -6, 2, -1, 0]

zero_sum_finder = ZeroSumFinder(numbers)

result = zero_sum_finder.find_zero_sum_elements()

print(result)

import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        # Check if the combination of sides is possible
        if self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 and self.side2 + self.side3 > self.side1:
            # Calculate semi-perimeter
            s = (self.side1 + self.side2 + self.side3) / 2

            # Calculate area using Heron's formula
            area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
            return area
        else:
            return "Invalid triangle"

# Get sides from user input
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Create Triangle object
triangle = Triangle(side1, side2, side3)

# Calculate and display the area
area = triangle.calculate_area()
print("Area of the triangle:", area)

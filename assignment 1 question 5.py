import math

# print table header
print("Angle\tSine\tCosine")

# calculate and print sine and cosine for each angle
for angle in range(0, 346, 15):
    rad = math.radians(angle)
    sin_val = round(math.sin(rad), 4)
    cos_val = round(math.cos(rad), 4)
    print(angle, "\t", sin_val, "\t", cos_val)

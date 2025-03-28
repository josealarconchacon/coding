import math

x = 3.14
print(x)  # Output: 3.14

# convert to float
print(float(5))         # From int: 5.0
print(float("10.5"))    # From string: 10.5

#  arithmetic with floats
a = 2.5
b = 1.2
print(a + b)   # 3.7
print(a - b)   # 1.3
print(a * b)   # 3.0
print(a / b)   # 2.083333...
print(a ** b)  # 2.5^1.2

# float division vs integer division
print(7 / 2)   # Float division: 3.5
print(7 // 2)  # Integer division: 3

# rounding a float
pi = 3.14159
print(round(pi))       # 3
print(round(pi, 2))    # 3.14 (2 decimal places)

# getting absolute value
temp = -12.5
print(abs(temp))   # 12.5

#  math functions with float
print(math.floor(4.7))  # Round down: 4
print(math.ceil(4.2))   # Round up: 5
print(math.sqrt(9.0))   # Square root: 3.0

# check if a value is float
print(isinstance(3.14, float))  # True
print(isinstance(5, float))     # False

#  special float values
print(float('inf'))    # Infinity
print(float('-inf'))   # Negative infinity
print(float('nan'))    # Not a number

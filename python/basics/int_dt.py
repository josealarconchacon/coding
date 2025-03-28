import math

a = 10
print(a)  # Output: 10

# arithmetic with integers
x = 5
y = 3
print(x + y)   # Addition: 8
print(x - y)   # Subtraction: 2
print(x * y)   # Multiplication: 15
print(x // y)  # Integer Division: 1
print(x % y)   # Modulus: 2
print(x ** y)  # Exponent: 125

# type conversion to int
# From float (truncates decimals)
print(int(3.99))  # Output: 3
# From string (must be a valid number string)
print(int("42"))  # Output: 42
# From binary, octal, hex strings
print(int("1010", 2))   # Binary to int: 10
print(int("12", 8))     # Octal to int: 10
print(int("A", 16))     # Hex to int: 10

# using int() with two arguments
# Syntax: int(string, base)
print(int("111", 2))  # Binary to decimal: 7
print(int("1A", 16))  # Hex to decimal: 26

# convert into to other base
n = 25
print(bin(n))   # Convert to binary: '0b11001'
print(oct(n))   # Convert to octal: '0o31'
print(hex(n))   # Convert to hex: '0x19'

#  checking if a value is an int
print(isinstance(100, int))      # True
print(isinstance("100", int))    # False

# math functions with integers
print(math.factorial(5))     # 5! = 120
print(math.gcd(20, 8))       # Greatest common divisor: 4
print(pow(2, 5))             # 2^5 = 32
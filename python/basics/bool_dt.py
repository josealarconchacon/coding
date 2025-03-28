a = True
b = False
print(a)  # True
print(b)  # False

age = 18
is_adult = age >= 18
print("Is adult?", is_adult)  # True


# comparison operators
print(5 > 3)     # True
print(2 == 4)    # False
print(7 != 7)    # False
print(10 <= 10)  # True

# using bool() to convert values
print(bool(1))         # True
print(bool(0))         # False
print(bool("Hello"))   # True (non-empty string)
print(bool(""))        # False (empty string)
print(bool([]))        # False (empty list)
print(bool([1, 2]))    # True (non-empty list)

# using in conditions (if statements)
logged_in = True
if logged_in:
    print("Welcome back!")
else:
    print("Please log in.")

# boolean Logic operators
a = True
b = False
print(a and b)  # False (both must be True)
print(a or b)   # True (either can be True)
print(not a)    # False (inverts the value)

# check boolean type
x = False
print(isinstance(x, bool))  # True

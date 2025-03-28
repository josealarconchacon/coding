# creating a list
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]
empty = []

# accessing list items
print(fruits[0])     # apple (1st item)
print(fruits[-1])    # cherry (last item)
print(fruits[1:3])   # ['banana', 'cherry'] (slicing)

# modifying a list
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# adding items
fruits.append("orange")        # Add to end
fruits.insert(1, "grape")      # Insert at index
print(fruits)

# removing items
fruits.remove("apple")         # Remove by value
last = fruits.pop()            # Remove last item
del fruits[0]                  # Delete by index
fruits.clear()                 # Empty the whole list

# loop through a list
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# list methods
numbers = [4, 2, 9, 1]
numbers.sort()       # Sort in place
print(numbers)       # [1, 2, 4, 9]
numbers.reverse()    # Reverse order
print(numbers)       # [9, 4, 2, 1]
print(numbers.index(4))   # Find index of 4
print(numbers.count(2))   # Count occurrences of 2

# check if item exists
print("yellow" in colors)    # False
print("yellow" not in colors)  # True

# list concatenation and repetition
a = [1, 2]
b = [3, 4]
print(a + b)         # [1, 2, 3, 4]
print(a * 2)         # [1, 2, 1, 2]

# check type
print(isinstance(colors, list))  # True

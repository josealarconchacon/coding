# creating set
my_set = {1, 2, 3, 4}
print(my_set)  # {1, 2, 3, 4}

# creating set form list 
nums = [1, 2, 2, 3, 3, 3]
unique_nums = set(nums)
print(unique_nums)  # {1, 2, 3}

# check is an item in the set exist 
colors = {"red", "blue", "green"}
print("red" in colors)    # True
print("yellow" in colors) # False

# add and remove item from set 
colors.add("yellow")         # Add new item
colors.remove("blue")        # Remove item (error if not found)
colors.discard("purple")     # Safe remove (no error)
print(colors)

# looping through a set
for color in colors:
    print(color)
    
# set operation 
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # Union: {1, 2, 3, 4, 5}
print(a & b)   # Intersection: {3}
print(a - b)   # Difference: {1, 2}
print(a ^ b)   # Symmetric difference: {1, 2, 4, 5}

# set method
print(len(a))          # Size of the set
a.clear()              # Remove all elements
print(a)               # Output: set()

# set is unordered and no duplicates
s = {1, 2, 2, 3, 3, 3}
print(s)  # {1, 2, 3}

# check type
print(isinstance(s, set))  # True

# empty set must use Set()
empty_set = set()
print(type(empty_set))     # <class 'set'>
not_a_set = {}             # This is a dictionary
print(type(not_a_set))     # <class 'dict'>

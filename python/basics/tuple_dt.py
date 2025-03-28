# creating tuple
person = ("Jose", 21, "Computer Science")
print(person)  # ('Jose', 21, 'Computer Science')

# tuple with one item 
single = ("hello",)
print(type(single))  # <class 'tuple'>

not_a_tuple = ("hello")  # This is just a string
print(type(not_a_tuple))  # <class 'str'>

# accessing elements
print(person[0])   # 'Jose'
print(person[-1])  # 'Computer Science'

# slicing tuple 
numbers = (1, 2, 3, 4, 5)
print(numbers[1:4])  # (2, 3, 4)

# tuples are immutable
# numbers[0] = 10  # TypeError: 'tuple' object does not support item assignment

# loop through tuple
for item in person:
    print(item)

# tuple methods
colors = ("red", "blue", "red", "green")
print(colors.count("red"))   # 2
print(colors.index("green")) # 3

# tuple packing & unpacking
# Packing
data = ("Jose", 21, "CS")
# Unpacking
name, age, major = data
print(name)   # Jose
print(age)    # 21
print(major)  # CS

# concatenating and repeating tuples
a = (1, 2)
b = (3, 4)
print(a + b)  # (1, 2, 3, 4)
print(a * 2)  # (1, 2, 1, 2)

# check type
print(isinstance(person, tuple))  # True


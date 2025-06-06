name = "Tom"
greeting = 'Hello'
print(name)      # Tom
print(greeting)  # Hello

# converting to string 
print(str(100))        # From int: '100'
print(str(3.14))       # From float: '3.14'
print(str(True))       # From bool: 'True'

# string concatenation 
first = "Hello"
last = "World"
print(first + " " + last)  # Hello World

# string 
s = "  Python is Awesome!  "
print(s.lower())      # '  python is awesome!  '
print(s.upper())      # '  PYTHON IS AWESOME!  '
print(s.strip())      # 'Python is Awesome!' (removes extra spaces)
print(s.replace("Awesome", "Great"))  # '  Python is Great!  '
print(s.split())      # ['Python', 'is', 'Awesome!']

# checking substring 
text = "Learning Python"
print("Python" in text)   # True
print("Java" not in text) # True

# indexing and slicing 
word = "Python"
print(word[0])     # P (first letter)
print(word[-1])    # n (last letter)
print(word[1:4])   # yth (characters from index 1 to 3)

# loop through a string
for char in "Hi":
    print(char)
    
# check if a value is a string 
print(isinstance("hello", str))  # True
print(isinstance(123, str))      # False

# string formatting (3 Ways)
name = "Tom"
age = 21
# f-string (recommended)
print(f"My name is {name} and I am {age} years old.")
# format() method
print("My name is {} and I am {} years old.".format(name, age))
# % formatting (old style)
print("My name is %s and I am %d years old." % (name, age))

# indexes
greeting = "Hello Tom"
print(greeting[:4].lower()) # hell
print(greeting[3:5]) # lo
print(greeting[4:7]) # o T

# immutability
# string in python are Immutable, once a string is created, its value cannot be changed. 
# any operation that appears to modify a string actually creates a new string.
# trying to change part of a string will raise an error
name = "Tom"
# name[0] = "M"  # This will raise: TypeError: 'str' object does not support item assignment

# built-Iin functions + methods
text = "Python"
# len() - returns the number of characters
print(len(text))  # 6
# type() - tells you the data type
print(type(text))  # <class 'str'>
# str() - converts something to a string
num = 123
print(str(num))  # '123'
# sorted() - returns a sorted list of characters
print(sorted(text))  # ['P', 'h', 'n', 'o', 't', 'y']
# enumerate() - gives index and character
for index, char in enumerate(text):
    print(index, char)

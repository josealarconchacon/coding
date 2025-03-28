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

# string and numbers 
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

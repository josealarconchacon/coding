age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

# comparing two numbers 
a = 10
b = 20
larger = a if a > b else b
print("Larger number:", larger)  # Output: 20

# even or odd checker 
num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(result)  # Output: Odd

# check if a list is empty 
my_list = []
message = "List has items" if my_list else "List is empty"
print(message)  # Output: List is empty

# temperature category
temp = 32
status = "Hot" if temp >= 30 else "Cold"
print(status)  # Output: Hot

# nested ternary
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)  # Output: B

# creating a dictionary
student = {
    "name": "Jose",
    "age": 21,
    "major": "Computer Science"
}
print(student)  # {'name': 'Jose', 'age': 21, 'major': 'Computer Science'}

# accessing values
print(student["name"])     # Jose
print(student.get("age"))  # 21

# modifying values
student["age"] = 102
student["GPA"] = 3.8  # Add new key-value pair
print(student)

# removing items
student.pop("GPA")       # Remove by key
del student["major"]     # Also removes by key
print(student)

# looping through a dictionary
for key in student:
    print(key, '--> ', student[key])

for key, val in student.items():
    print(f'{key}: {val}')

# dictionary methods
print(student.keys())     # dict_keys(['name', 'age'])
print(student.values())   # dict_values(['Jose', 102])
print(student.items())    # dict_items([('name', 'Jose'), ('age', 102)])
print("name" in student)  # True
print("GPA" not in student)  # True

# nested dictionary
users = {
    "user1": {"name": "Jose", "age": 21},
    "user2": {"name": "Anna", "age": 25}
}
print(users["user1"]["name"])  # Jose

# check if it's a dictionary
print(isinstance(student, dict)) # True

# dictionary from a list of tuples
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)
print(d)  # {'a': 1, 'b': 2}

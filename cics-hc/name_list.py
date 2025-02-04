# ass user to enter a list of names
names = input("Enter a list of names separated by semicolons (;):\n"
                    "- Example: Doe, John; Smith, Alice\n"
                    "- Format: LastName, FirstName\n"
                    "Enter names: ")
# print the name one per line
for name in names.split(';'):
    # get the fist character for the fist name
    first_name = name.split(',')[1].split()[0][0] + '.'
    # print the name
    print(f"{first_name} {name.split(',')[0]}")  # print the name
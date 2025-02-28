# ask the user to enter last names separated by commas
names = input("Enter names, separated by commas: ")
# split the input string into a list of names
names_list = names.split(",")
# create an empty list to store names that contain spaces
names_with_spaces = []

# loop through each name in the list
for name in names_list:
    # check if the name contains a space
    if " " in name:
        # add the name to the list of names with spaces
        names_with_spaces.append(name)

# print the list of names that contain spaces
print("A list of names with spaces: ", names_with_spaces)

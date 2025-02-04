# Ask user to enter a list of names
enter_names = input("Enter a list of names separated by semicolons (;):\n"
              "- Example: Lastname, Firstname; Lastname, Firstname\n"
              "Enter names: ")

# loop over each name , splitting by (;) one per line
for name in enter_names.split("; "):
    # split each name by ', ' to separate last and first names
    split_name = name.split(", ")

    last_name = split_name[0] # set a new last_name variable to store last_name
    first_name = split_name[1] # set a new first_name variable to store first_name

    # Print the first initial of the first name, followed by ".", and followed by the last name.
    print(f"{first_name[0]}. {last_name}")

print("\nThank you for using my name organizer!")

    
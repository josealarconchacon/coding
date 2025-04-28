

# get user input
def get_user_input():
    user_input = input("Enter a non-empty string: ")
    return user_input

# validate user input
def validate_input():
    while True:
        user_input = get_user_input()
        if user_input == "":
            print("That was empty. Try again")
        else:
            return user_input

def main():
    user_input = validate_input()
    print(f"You entered: {user_input}")
    
if __name__ == "__main__":
    main()
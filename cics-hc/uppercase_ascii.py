# ask the user to enter a phrase:   
phrase = input("Enter a phrase: ")
# convert the phrase to uppercase
phrase_upper = phrase.upper()
# prints each uppercase character and its corresponding ASCII code
for char in phrase_upper:
    print(f"Character: {char}, ASCII Code: {ord(char)}")  # ord
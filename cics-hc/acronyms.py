# prompts the user to enter a phrase
phrase = input("Enter a phrase: ")
# make the phrase uppercase
phrase = phrase.upper()
# print the phrase
print('Your phrase in capital letters: ', phrase)

# initialize an empty acronym string
acronym = ''
# Loop through the phrase and get the first letter of each word
for i in phrase.split():
    acronym += i[0]# store the first letter of each word to the acronym
# print the acronym
print('Acronym: ', acronym)
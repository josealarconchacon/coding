# ask user for a binary number
binary_string = input("Enter a binary number: ")

# start with decimal number 0
dec_num = 0

# loop through each character, bit in the binary string
for c in binary_string:
    dec_num = dec_num * 2 # multiply the current decimal number by 2
    # If the current bit is '1', add 1 to the decimal number
    if c == '1':
        dec_num = dec_num + 1

# print the decimal
print("Your number in decimal is:", dec_num)


# Ask the user for a DNA string
dna_string = input("Enter a DNA string: ")

count = 0 # initialize an empty count variable

# through each character in the dna_string
for dna in dna_string:
    # get the length of the dna_string
    length = len(dna_string)
    # Check if the character is 'C' or 'G' and count it
    if dna == 'C' or dna == 'G':
        count = count + 1
    # Calculate the GC-content as a decimal
    gc_content = count / length

# Print the results
print(f"Length is {length}\nGC-content is {gc_content}")

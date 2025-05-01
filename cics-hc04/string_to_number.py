

# map string numbers to their integer values
def string_and_num():
    # set a dict of string numbers to their integer values
    map_dict = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19, "twenty": 20,
        "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }
    return map_dict

def string2num(s):
    # split the input string into words
    words = s.split()
    # set a total variable to zero
    total = 0
    # call function to get the dict
    map_dict = string_and_num()
    
    # loop over each word in the input string
    for w in words:
        # If the word is in the dictionary
        if w in map_dict:
            # add it to the total
            total += map_dict[w]
        
    # verify if total is between 1 and 99
    if total < 1 or total > 99:
        return -1
    return total

# Example usage 
if __name__ == "__main__":
    print("Converting fourteen to", string2num("fourteen"))
    num_str = "sixty six"
    print("Converting", num_str, "to", string2num(num_str))
    print("Converting hundred to", string2num("hundred"))  


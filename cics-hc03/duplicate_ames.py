
def duplicates(names):
    name_count = {} # empty dictionary counts to count how many times each name appears
    is_duplicated = [] # store names that are duplicated in the list
    
    # loop through the names
    for name in names:
        if name in name_count:
            name_count[name] += 1 # increment the count of the name, if name already seen
            # only add to the list is the count is 2
            if name_count[name] == 2:
                is_duplicated.append(name)
        else:
            name_count[name] = 1
    return is_duplicated # return duplicated names

def main():
    names = ['Daniel','Dorothy','Bethany','Beth','Daniel','Georgi']
    print(duplicates(names))

if __name__ == "__main__":
    main()
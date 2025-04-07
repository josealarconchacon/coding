
def unique_visitors(emp_id):
    unique_id = {} # create an empty dictionary
    # loop through the list of emp_id
    for id in emp_id:
        if id in unique_id:
            unique_id[id] += 0 # id already exists
        else:
            unique_id[id] = 1 # add id to the dictionary
    # return the length of the dictionary
    return len(unique_id)

def main():
    ids = ['12345678','11223344','12312323','12345678']
    print("The number of unique visitors is ", unique_visitors(ids))

if __name__ == "__main__":
    main()

# import the pandas library for data handling
import pandas as pd  

def ticket_offenders():
    # ask the user to enter the CSV file name
    csv_file_name = input("Enter file name: ")
    # ask the user for the attribute (column name) they want to search by
    attribute = input("Enter attribute: ")

    # Read the CSV file
    ticket_data_file = pd.read_csv(csv_file_name)

    # Count how many times each unique value appears in the selected column
    offenders_count = ticket_data_file[attribute].value_counts()

    # access and add the column name to the result
    offenders_count.name = attribute

    # Print the 10 most frequent values and their counts
    print("\nThe 10 worst offenders are:")
    print(offenders_count[:10])

# call the function to run the program
ticket_offenders()

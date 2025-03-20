# import pandas library
import pandas as pd

# Ask the user for the name of a CSV file name
filename = input("Enter the name of the CSV file: ")

# Read the CSV file into
data_file = pd.read_csv(filename)

# Find the lowest temperature recorded across all locations and dates
lowest_temp = data_file['MinTemp'].min() # use min() to find the minimum value

# Find the lowest temperature for each location across all dates
# use the groupby method to split the records from the CSV file by location
# then find the minimum temperature for each location
lowest_temp_by_location = data_file.groupby('Location')['MinTemp'].min() # use min() to find the minimum value

# Print the overall results and minimum temperature by location
print(f"\nOverall min temp: {lowest_temp}")

print("Minimum temperature by location:")
print(lowest_temp_by_location)

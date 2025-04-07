
"""
Name: Jose Alarcon Chacon
Email: jose.alarconchacon76@login.cuny.edu
Date: March 27, 2025
# Ask user for input and output, 
# display the fraction of Grade K to 6 enrollment that has lived in that borough, over time,
# and print out the minimum, maximum, median, mean, and stand deviation of total enrollment in that borough (round to 3 decimal numbers).
"""
# import panda and matplotlib library 
import pandas as pd
import matplotlib.pyplot as plt

def get_user_input():
    # ask the user fro input and output
    borough_name = input('Enter borough name: ')
    output_file = input('Enter output file name: ')
    return borough_name, output_file

def read_csv_file():
    # read demo_boro csv file
    return  pd.read_csv('demo_boro.csv')

def calculate_fraction(data):
    # create a column that calculate the fraction of Grade K to 6 vs
    data['Grade K to 6'] = (
        data['Grade K'] + 
        data['Grade 1'] + 
        data['Grade 2'] + 
        data['Grade 3'] + 
        data['Grade 4'] + 
        data['Grade 5'] + 
        data['Grade 6']
    )
    # calculates the fraction column
    data['Grade K-6 Enrollment Fraction'] = data['Grade K to 6'] / data['Total Enrollment']
    return data

def result(input_borough_name, borough_data):
    # print stats
    print("minimum of total enrollment for", input_borough_name, "is", round(borough_data['Total Enrollment'].min(), 3))
    print("maximum of total enrollment for", input_borough_name, "is", round(borough_data['Total Enrollment'].max(), 3))
    print("median of total enrollment for", input_borough_name, "is", round(borough_data['Total Enrollment'].median(), 3))
    print("mean of total enrollment for", input_borough_name, "is", round(borough_data['Total Enrollment'].mean(), 3))
    print("stand deviation of total enrollment for", input_borough_name, "is", round(borough_data['Total Enrollment'].std(), 3))
    
def my_school_enrollment():
    # call read_csv_file function
    data_file = read_csv_file()
    # call get_user_input function
    input_borough_name, output_file = get_user_input()
    
    # get borough data using query method
    borough_data = data_file.query("Borough == '" + input_borough_name + "'")
    # call calculate_fraction function
    calculate_fraction(borough_data)
    
    # plot fraction using this data
    # plt.plot(borough_data['Year'], borough_data['Grade K to 6'])
    borough_data.plot(x = 'Year', y = 'Grade K-6 Enrollment Fraction')
    plt.savefig(output_file)
    # plt.show()
        
    # call result function
    result(input_borough_name, borough_data)

# call function
if __name__ == "__main__":
     my_school_enrollment()
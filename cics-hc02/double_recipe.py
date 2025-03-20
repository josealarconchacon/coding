
# import pandas library
import pandas as pd

# ask the user for the recipe CSV file name
filename = input("Enter recipe name: ")

# read the CSV file
read_recipe = pd.read_csv(filename)

# multiply the "Amount" column by 2 to double the recipe
read_recipe['Amount'] = read_recipe['Amount'] * 2

# print the doubled recipe
print("Double your recipe is:")
print(read_recipe)
# import matplotlib library
import matplotlib.pyplot as plt

# asks the user for a choice: (L or R)
user_choice = input("Would you like the left or right half (L/R): ").lower()

# validate the user choice
if user_choice not in ['l', 'r']:
    print("Error: Invalid input. Please enter 'L' or 'R'. Run program again.")
    exit()

# Ask user for input and output file names
input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")

# # Load the image from the input file
img = plt.imread(input_file)

# Get the dimensions of the image, height and width
height = len(img) # get the number of rows in height
width = len(img[0]) # get the number of columns in width

# set conditional statement, then slice the image based on user choice
if user_choice == 'l':
    half_img = img[:, :width // 2]
elif user_choice == 'r':
    half_img = img[:, width // 2:]
else:
    print("Error")

# Save the result
plt.imsave(output_file, half_img)

print("Saved to", output_file)

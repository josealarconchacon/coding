#Import the packages for images and arrays
import matplotlib.pyplot as plt
import numpy as np

# Ask the user for input and output image file names
img_input_file = input("Enter name of the input file: ")
img_output_file = input("Enter name of the output file: ")

# Read the image
img = plt.imread(img_input_file)

# Make a copy of the image and keep only the blue channel
blue_img = img.copy()
blue_img[:, :, 0] = 0  # Set the red channel to 0
blue_img[:, :, 1] = 0  # Set the green channel to 0

# plt.imshow(blue_img) 
# plt.show() 

# Save the modified image
plt.imsave(img_output_file, blue_img)


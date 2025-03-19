import matplotlib.pyplot as plt
import numpy as np

# Ask the user for the size of the image
size = int(input("Enter the size: "))

# Ask the user for the name of the output file
output_file = input("Enter output file: ")

# Create an empty image (height, width, color channels)
# Initialize all pixels as white
image = np.ones((size, size, 3))  # White = (1, 1, 1)

# Set every other column to blue (0, 0, 1)
image[:,::2] = [0, 0, 1]  # Blue columns

# Save the image to the specified file
plt.imsave(output_file, image)

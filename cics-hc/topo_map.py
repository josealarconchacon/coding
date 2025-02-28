
# Import necessary libraries for arrays and image display
import numpy as np
import matplotlib.pyplot as plt

# Read in the elevation data into an array
elevations = np.loadtxt('elevationsNYC.txt')

# Enter amount of intensity (a floating point number between 0.0 and 1.0)
intensity = float(input("What intensity for the topo lines: "))
# Then enter a name for the output image
output_filename = input("What is the output file: ")

# Take the shape (dimensions) of the elevations and add another dimension to hold the 3 color channels
map_shape = elevations.shape + (3,)

# Create a blank image, all zeros
topo_map = np.zeros(map_shape)  

# Process each pixel based on elevation data
for row in range(map_shape[0]):
    for col in range(map_shape[1]):
        if elevations[row, col] <= 0:
            # Below or at sea level
            topo_map[row, col] = [0, 0, 1]  # Blue
        elif elevations[row, col] % 10 == 0:
            # Topo lines (elevations divisible by 10)
            topo_map[row, col] = [intensity, intensity, intensity]  # Gray based on user input
        else:
            # Land (default white)
            topo_map[row, col] = [1, 1, 1]  # White

# Display the image using imshow
# plt.imshow(topo_map)
# Show the image
# plt.show()
# Save the image as well
plt.imsave(output_filename, topo_map)

# Print confirmation message
print(f"Thank you for using my program!\nYour map is stored as {output_filename}.")



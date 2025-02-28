import matplotlib.pyplot as plt  # Import libraries for plotting
import numpy as np  # Import numpy for array operations

# create a 30 by 30 array
logoImg = np.ones((30, 30, 3))

# for blue color, set red and green to 0 and keep blue at 100%
# top 10 rows to be blue
# Turn the red and green to 0 for the first 10 rows
logoImg[:10, :, 0] = 0  
logoImg[:10, :, 1] = 0  

# bottom 10 rows to be blue
# Turn the red and green to 0 for the last 10 rows
logoImg[-10:, :, 0] = 0  
logoImg[-10:, :, 1] = 0  

# left 10 columns to be blue
# Turn the red and green to 0 for the first 10 columns
logoImg[:, :10, 0] = 0  
logoImg[:, :10, 1] = 0 

# remove the middle right part to form 'C' shape, set it to white
logoImg[10:-10, 10:] = 1  # Keep it white: 100%,100%,100%

# save file as logo.png
plt.imsave("logo.png", logoImg)  

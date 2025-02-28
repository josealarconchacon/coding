import matplotlib.pyplot as plt #import libraries for plotting
import numpy as np #and for arrays (to hold images)
logoImg = np.ones((10,10,3)) #10x10 array with 3 sheets of 1’s

#To make purple, we’ll keep red and blue at 100% and turn green to 0%
logoImg[:,:3,1] = 0 #Turn the green to 0 for first 3 columns


import turtle

# Create a turtle object
t_color_stamps = turtle.Turtle()
t_color_stamps.backward(-15)

# Loop for 5 colors
for i in range(5):
    color = input("Enter color (as hex): ")  # Get color input
    t_color_stamps.forward(20)  # Move forward for spacing
    t_color_stamps.color(color) # stamps out that color using the turtle library
    t_color_stamps.stamp()  # Stamp at current position

# Keep the window open
turtle.done()

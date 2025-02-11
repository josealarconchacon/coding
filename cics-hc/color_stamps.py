import turtle

# Create a turtle object
t_color_stamps = turtle.Turtle()

# Loop for 5 colors
for i in range(5):
     # Get color input
    color = input("Enter color (as hex): ") 
    # stamps out that color using the turtle library
    t_color_stamps.color(color)
    t_color_stamps.fillcolor(color)

    t_color_stamps.stamp()  # Stamp at current position
    t_color_stamps.forward(20)  # Move forward for spacing

# Keep the window open
turtle.done()

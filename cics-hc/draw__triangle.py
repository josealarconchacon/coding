import turtle

# create a turtle object
t_triangle = turtle.Turtle()

# loop and repeat 3 times, one for each side of the triangle
for i in range(3):
    t_triangle.forward(100)  # draw a line
    t_triangle.left(120)     # turn left by 120 degrees

# turtle.done()  # Keeps the window open

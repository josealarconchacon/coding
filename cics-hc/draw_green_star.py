import turtle

# create a turtle object
t_green_start = turtle.Turtle()

# repeat 5 times, one for each side of the star
for i in range(5):
    t_green_start.color("green") # set the color of the star to green
    t_green_start.forward(100) # walk forward 100 steps
    t_green_start.left(144) #turn left 144 degrees
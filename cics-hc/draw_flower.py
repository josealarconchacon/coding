import turtle

# create a turtle object
t_flower = turtle.Turtle()

# loop and repeat 50 times to draw a flower
for i in range(50):
    t_flower.color('blue') # change color to blue
    t_flower.forward(100) # walk forward 100 steps
    t_flower.left(155) # turn left 155 degrees
    t_flower.color('red') # change color to red
    t_flower.forward(100) # walk forward 100 steps
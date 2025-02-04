import turtle

# create turtle object named t_twisting_square
t_twisting_square = turtle.Turtle()

# loop will range from 20 to 100, incrementing by 2
for i in range(20, 100, 2):
    t_twisting_square.forward(i) # walk forward i steps,
    t_twisting_square.right(93) # turn right 93 degrees
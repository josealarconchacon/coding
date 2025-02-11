#Import the turtle drawing package
import turtle

# Create a new turtle object 
turning_turtle = turtle.Turtle()

# loop and ask the user for 5 numbers
for i in range(5):
    # get user input
    enter_number = int(input("\nEnter 5 whole numbers:\nFor each number, the turtle will turn left\nby that many degrees and then move forward 100 units:\n\nEnter a number: "))
    # turn left the degrees entered 
    turning_turtle.left(enter_number)
    # move forward 100
    turning_turtle.forward(100)
# keep window open
turtle.done()
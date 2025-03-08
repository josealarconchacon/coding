# import the turtle commands to use in the program
import turtle

# crate a turtle object
t_obj = turtle.Turtle()
window_screen = turtle.Screen()
step_forward = 50 
step_left = 90
step_right = 90
thick_pensize = 10
thin_pensize = 1
r_pencolor = 'red'
b_pencolor = 'black'

# Get input from the user
command_string = input("Enter command string: ")

# Process each character in the command string
for ch in command_string:
    #perform action indicated by the character
    if ch == 'F':  # Move forward
        t_obj.forward(step_forward)
    elif ch == 'B':  # Move backward
        t_obj.backward(step_forward)
    elif ch == 'L':  # Turn left
        t_obj.left(step_left)
    elif ch == 'R':  # Turn right
        t_obj.right(step_right)
    elif ch == 'S':  # Stamp the turtle's shape
        t_obj.stamp()
    elif ch == 'r':  # Change color to red
        t_obj.pencolor(r_pencolor)
    elif ch == 'b':  # Change color to black
        t_obj.pencolor(b_pencolor)
    elif ch == 'T':  # Set thick pen size
        t_obj.pensize(thick_pensize)
    elif ch == 't':  # Set thin pen size
        t_obj.pensize(thin_pensize)

window_screen.exitonclick() #Close the window when clicked




            
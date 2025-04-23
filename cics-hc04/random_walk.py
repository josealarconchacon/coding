"""
Name: Jose Alarcon Chacon
Email: jose.alarconchacon76@login.cuny.edu
Date: April 23, 2025
Program creates a random walk using the turtle module.
"""

import turtle
import random

# Setup turtle
trey = turtle.Turtle()
trey.speed(10)
trey.color('blue')
trey.pensize(2)

# Perform 250 steps
for i in range(250):
    a = random.randrange(0, 360, 10)  # 0,10,20,30,...,340,350
    trey.right(a)
    trey.forward(5)

turtle.done()

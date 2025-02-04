#Import the turtle drawing package
import turtle

turtle.colormode(255)		#Allows colors to be given as 0...255
shades_of_purple = turtle.Turtle()		#Create a turtle
shades_of_purple.shape("turtle")		#Make it turtle shaped
shades_of_purple.backward(100)          #Move her backwards, to give more space to draw

#For 0,10,20,...,250
for i in range(0,255,10):
    shades_of_purple.forward(10)		#Move forward
    shades_of_purple.pensize(i)		    #Set the drawing size to be i (larger each time)
    shades_of_purple.color(i,0,i)		#Set the purple channel to be i (brighter each time)
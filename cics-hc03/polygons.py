
# import turtle
import turtle

# polygon function 
def polygon(t_object, edges, length, color):
    polygon_angle = 360 / edges # calculate the angle of the polygon to turn at each corner
    t_object.color(color) #  turtle drawing color
    # loop and draw the polygon
    for i in range(edges):
        t_object.forward(length) # move forward by length
        t_object.left(polygon_angle) # turn left by the angle of the polygon

def main():
	tess = turtle.Turtle()
	polygon(tess, 5, 100, "green")
	polygon(tess, 6, 60, "#ff00ff")
	polygon(tess, 7, 70, "#ff0000")
	turtle.done()

if __name__ == '__main__':
	main()
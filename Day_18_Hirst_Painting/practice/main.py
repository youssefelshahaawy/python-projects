from turtle import Turtle,Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("purple")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(num_sides):
    rotation = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(rotation)
        

for shape in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape)






screen = Screen()
screen.exitonclick()
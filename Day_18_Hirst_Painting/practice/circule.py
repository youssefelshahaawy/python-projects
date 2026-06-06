import turtle as t
import random


tim = t.Turtle()
t.colormode(255)
tim.speed(0)



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

def draw_spirograph(size):
    for _ in range(int (360 / size)):
        tim.color(random_color())
        tim.circle(70)
        tim.setheading(tim.heading() + size)

draw_spirograph(6)





screen = t.Screen()
screen.exitonclick()
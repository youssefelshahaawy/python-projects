import turtle as t
import random


tim = t.Turtle()
t.colormode(255)
# colors = ["lime green", "dark orange", "green yellow", "gold", "dark violet", "red"]
directions = [0, 90, 180, 270]
tim.speed(10)
tim.pensize(7)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

for _ in range(200):
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(directions))







screen = t.Screen()
screen.exitonclick()
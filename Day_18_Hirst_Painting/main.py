import turtle as t
import colorgram as c
import random


colors = c.extract('hirst_painting.jpg', 30)
rgbs=[]

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgbs.append(new_color)
    
    
tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.hideturtle()
tim.setheading(255)
tim.forward(300)
tim.setheading(0)    
tim.speed(0)
number_of_dots = 100
 
for dot_count in range(1,number_of_dots + 1):
    tim.dot(30,random.choice(rgbs))
    tim.forward(50)
    
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)





screen = t.Screen()
screen.exitonclick()
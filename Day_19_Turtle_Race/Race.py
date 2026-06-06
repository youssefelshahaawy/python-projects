from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput("Make your bet",prompt="which turtle will win the race? Enter a color: ")
colors =["red","orange","yellow","green","blue","purple"]
all_turtles = []

    
t = -100
for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230,y= t) 
    t += 40
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winner is: {winning_color}")
            else:
                print(f"You've lost! The winner is:{winning_color}")

            
        distance = random.randint(0, 10)
        turtle.forward(distance)
            






screen.exitonclick()
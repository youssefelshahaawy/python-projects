# listen and draw freely

from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

 
def move_forward():
    tim.forward(20)
def step_forward():
    tim.forward(5)
def step_backward():
    tim.backward(5)
def turn_left():
    tim.left(10)
def turn_right():
    tim.right(10)
def reset():
    tim.reset()
    
    
screen.listen()
screen.onkey(key="space", fun = move_forward)
screen.onkey(key="w", fun = step_forward)
screen.onkey(key="s", fun = step_backward)
screen.onkey(key="a", fun = turn_left)
screen.onkey(key="d", fun = turn_right)
screen.onkey(key="c", fun = reset)
screen.exitonclick()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def reach():
    turn_left()
    move()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear():
        move()
    turn_left() 
    
while not at_goal():
    if wall_in_front():
        reach()
    else:
        move()
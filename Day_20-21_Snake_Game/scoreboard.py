from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 15, "normal")
with open("data.txt") as file:
    data = int(file.read())
    
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.high_score = data
        self.penup()
        self.goto(0,270)
        self.update_scoreboeard()
        self.hideturtle()
       
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.high_score))
                
        self.score = 0
        self.update_scoreboeard()
    
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align= ALIGMENT, font= FONT)
        

    def update_scoreboeard(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score: {self.high_score}", align= ALIGMENT, font= FONT)
        
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboeard()
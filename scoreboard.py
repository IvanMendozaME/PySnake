from food import Food
from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier",24,"normal")
class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,260)
        self.color("white")
        
        self.hideturtle()
        with open("data.txt") as file:
            self.high_score = file.read()
        self.update_scoreboard()
    def update_scoreboard(self):
        
        if self.score > int(self.high_score):
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))

        self.clear()
        self.write(f"Score:{self.score} High score:{self.high_score}", align=ALIGMENT, font=FONT)

    def increase(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
    
        """ def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGMENT, font=FONT) """

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.hideturtle()
        self.goto(-280,280)
        self.write(f"level:{self.level}",align="left",font=("Arial",8,"normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=("Arial",8,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("game over:{self.level}", align="left", font=("Arial",8,"normal"))

    def inc_level(self):
        self.level+=1
        self.update_scoreboard()
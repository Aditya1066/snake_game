from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.ht()
        self.goto(0,270)
        self.write(f"Score:- {self.score} ", align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f"Score:- {self.score} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

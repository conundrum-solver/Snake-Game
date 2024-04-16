from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.score}", align="center", font=("Geometric", 24, "normal"))

    def food_eaten(self):
        self.write(f"Score: {self.score}", align="center", font=("Geometric", 24, "normal"))

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.food_eaten()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=("Geometric", 24, "normal"))

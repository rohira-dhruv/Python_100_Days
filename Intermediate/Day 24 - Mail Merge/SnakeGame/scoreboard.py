from turtle import Turtle

SCOREBOARD_POSITION = (0, 270)
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.score = 0
        self.color("white")
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score: {self.high_score}", font=FONT, align=ALIGNMENT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", font=FONT, align=ALIGNMENT)

from turtle import Turtle

MOVE_DISTANCE = 15


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__(shape="square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        y_cor = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y_cor)

    def down(self):
        y_cor = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), y_cor)

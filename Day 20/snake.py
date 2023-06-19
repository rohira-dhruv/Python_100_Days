from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(3):
            snake_part = Turtle(shape="square")
            snake_part.color("white")
            snake_part.penup()
            snake_part.goto(float(_ * -20), 0)
            self.segments.append(snake_part)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for index in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[index-1].xcor()
            new_y = self.segments[index-1].ycor()
            self.segments[index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


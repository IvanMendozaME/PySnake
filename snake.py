from turtle import Turtle
STARTING_POS = [(0,0), (-20,0), (-40,0)]
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
        for position in STARTING_POS:
            self.add_segments(position)
    def move(self):
        for i in range(len(self.segments) -1,0,-1 ):
            newx = self.segments[i-1].xcor()
            newy = self.segments[i-1].ycor()
            self.segments[i].goto(newx,newy)
        self.segments[0].forward(MOVE_DISTANCE)

    def add_segments(self, position):
        snake = Turtle()
        snake.penup()
        snake.color("white")
        snake.shape("square")
        snake.goto(position)
        self.segments.append(snake)
    def reset(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def extend(self):
        self.add_segments(self.segments[-1].position())
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
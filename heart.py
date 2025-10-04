from turtle import Turtle

class Heart(Turtle):
    def __init__(self,gif,x,y):
        super().__init__()
        self.penup()
        self.shape(gif)
        self.shapesize(stretch_len=0.1, stretch_wid=0.1)
        self.goto(x,y)
        
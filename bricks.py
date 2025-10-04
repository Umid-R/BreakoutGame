from turtle import Turtle

class Brick(Turtle):
    
    def __init__(self, color,len):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.penup()
        self.shapesize(stretch_len=len,stretch_wid=3)
        
    
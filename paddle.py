from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=12,stretch_wid=0.5)
        self.penup()
        self.color('white')
        self.x=0
        self.goto(self.x,-350)
    
    
    def to_right(self):
        if self.xcor()<480:
            self.x+=60
        self.goto(self.x,-350)
            
    def to_left(self):
        if self.xcor()>-480:
            self.x-=60
        self.goto(self.x,-350)
                
        
        
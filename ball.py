from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        
        self.x_cor=0
        self.y_cor=-350
        self.step_y=2
        self.step_x=2
        self.shapesize(stretch_len=0.7,stretch_wid=0.7)
    
    
    def move(self):
        self.y_cor+=self.step_y
        self.x_cor+=self.step_x
        self.goto(self.x_cor,self.y_cor)
    
    def bounce_y(self):
        self.step_y*=-1
        
        
        
    def bounce_x(self):
        
        self.step_x*=-1
    
    
    def bounce_paddle(self, paddle):
        # Just flip vertical direction
        self.step_y = abs(self.step_y)  
        
        

    def restart(self):
        self.x_cor=0
        self.y_cor=-300
        self.step_y=2
        self.step_x=2
        

        
    
        
        
        
        
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(500,330)
        self.color('white')
        self.hideturtle()
    
    def score(self,score):
        self.write(score, align="center", font=("Arial", 30, "bold"))
    
    def win(self):
        self.home()
        self.color('green')
        self.write("You win",align="center", font=("Arial", 50, "bold"))
        
    def lose(self):
        self.goto(0,250)
        self.color('red')
        self.write("You lose",align="center", font=("Arial", 50, "bold"))
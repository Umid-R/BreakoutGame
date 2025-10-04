import turtle
from paddle import Paddle
from ball import Ball
from bricks import Brick
from heart import Heart
from scoreboard import ScoreBoard

screen=turtle.Screen()
screen.setup(width=1200, height=800)
screen.title('Breakout Game')
screen.bgcolor('black')
screen.tracer(0)

#Scoreboard
scoreboard=ScoreBoard()

#Bricks
bricks=[]
x=-550
for n in range(13):
    brick=Brick('red',len=4)
    
    brick.goto(x,0)
    x+=91
    bricks.append(brick)
    
    
x=-550
y=70
for n in range(13):
    brick=Brick('green',len=4)
    
    brick.goto(x,y)
    x+=91
    bricks.append(brick)
    
x=-550
y=140
for n in range(13):
    brick=Brick('yellow',len=4)
    
    brick.goto(x,y)
    x+=91
    bricks.append(brick)
  
  
#Paddle
paddle=Paddle()

#Ball
ball=Ball()

#Hearts
hearts=[]
x=-550
screen.addshape('heart.gif')
for _ in range(3):
  heart=Heart('heart.gif',x,360)
  hearts.append(heart)
  x+=50

#Screen listens for any key presses
screen.listen()
screen.onkey(fun=paddle.to_right, key='Right')
screen.onkey(fun=paddle.to_left,key='Left')

score=0
is_game_on=True
while is_game_on:
    screen.update()
    scoreboard.score(score)
    ball.move()
    #Collision with paddle
    if abs(ball.xcor()-paddle.xcor()) < 125 and abs(ball.ycor()-paddle.ycor()) < 10:
        ball.bounce_paddle(paddle)

    
    #Collision with wall
    if ball.ycor()>395:
        ball.bounce_y()
    if ball.xcor()>595:
        ball.bounce_x()
    if ball.xcor()<-595:
        ball.bounce_x()
    
    # Check if there is any brick left
    if bricks:
        #Collision with Bricks
        for b in bricks:
            if abs(b.xcor() - ball.xcor()) < 50.5 and abs(b.ycor() - ball.ycor()) < 40:
                # Calculate how close the ball is to brick edges
                overlap_x = abs(b.xcor() - ball.xcor())
                overlap_y = abs(b.ycor() - ball.ycor())

                if overlap_x > overlap_y:
                    ball.bounce_x()
                else:
                    ball.bounce_y()

                b.hideturtle()
                score+=1
                scoreboard.clear()
                bricks.remove(b)
    else:
        scoreboard.win()
        break
    
    # Check if  Ball is out
    if ball.ycor()<-450:
        ball.restart()
        h=hearts.pop()
        h.hideturtle()
        
        # Check if there is any heart left
        if not hearts:
            scoreboard.lose()
            break
    
        
                





screen.exitonclick()
import turtle
#create the screen
wind = turtle.Screen() #creat the gama screen
wind.title('Ping Pong Game') #the title of the game
wind.bgcolor('black') #bgcolor
wind.setup(width=800,height=600) #the cardinal of the screen
wind.tracer(0) #stop the screen of updting
# paddl1
paddl1= turtle.Turtle() #declare the veriable
paddl1.speed(0) #set ther speed of the drawe
paddl1.shape('square') #set the shape
paddl1.color('yellow') #set the color
paddl1.shapesize(stretch_len=1,stretch_wid=5) #stretch by *5 in wingth and by *1 in the lenght
paddl1.penup() #to dont drawe ling while hi move
paddl1.goto(-350,0) #set the posision
# paddl2
paddl2= turtle.Turtle()
paddl2.speed(0)
paddl2.shape('square')
paddl2.color('pink')
paddl2.shapesize(stretch_len=1,stretch_wid=5)
paddl2.penup()
paddl2.goto(350,0)
# ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.15 #la pas of the ball in X
ball.dy = 0.15 #la pas of the ball in Y
#score
score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0,260)
score.write('Player 1: 0  |  player 2: 0',align='center',font=('Coureier',20,'normal')) #paramater of the strange showed in the screen
#function
# move paddl1
def paddl1_up():
    y = paddl1.ycor() #find the palce of the paddle
    y += 20 #incremant the place of the paddle by 20pi every time
    paddl1.sety(y) #set the new paddle place
def paddl1_down():
    y = paddl1.ycor()
    y -= 20
    paddl1.sety(y)
# move paddl2
def paddl2_up():
    y = paddl2.ycor()
    y += 20
    paddl2.sety(y)
def paddl2_down():
    y = paddl2.ycor()
    y -= 20
    paddl2.sety(y)
# keybord connect
wind.listen() #make the wind(screen) ready for exepte comande from the keybord
wind.onkeypress(paddl1_up,'z') #when press z execute the function paddl1_up
wind.onkeypress(paddl1_down,'s')
wind.onkeypress(paddl2_up,'Up')
wind.onkeypress(paddl2_down,'Down')
# main game loop
while True:
    wind.update() #make the screen update evrey time the loop run
    #ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #ball border
    if ball.ycor()>=290: #when the ball tech the up
        ball.sety(290)
        ball.dy*=-1 #reverse the direction
    if ball.ycor()<=-290: #when the ball tech the batom
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>=390: #when the ball pass the left
        ball.goto(0,0) #return the ball to 0,0
        ball.dx *=-1
        score1+=1
        score.clear()
        score.write('Player 1: {}  |  player 2: {}'.format(score1,score2),align='center',font=('Coureier',20,'normal'))
    if ball.xcor()<=-390:
        ball.goto(0,0)
        ball.dx*=-1
        score2+=1 #increment the score of player2 when the ball go left
        score.clear() #clear the old score
        score.write('Player 1: {}  |  player 2: {}'.format(score1, score2), align='center',font=('Coureier', 20, 'normal'))
# backup when the ball hit the paddles
    if (ball.xcor()>340 and ball.xcor()<350) and ( ball.ycor()< paddl2.ycor()+40 and ball.ycor()>paddl2.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddl1.ycor() + 40 and ball.ycor() > paddl1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1


        #the first project in python is secsessfuly compleated
               #Time recwarer : 3h



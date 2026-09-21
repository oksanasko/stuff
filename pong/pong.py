import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer()

score_a=0
score_b=0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)#max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)#max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
#Ball
ball = turtle.Turtle()
ball.speed(0)#max
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 4
ball.dy = 4
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 22, "normal"))

def paddle_move(paddle, up):
    y = paddle.ycor()
    y += 20 if up else -20
    paddle.sety(y)

wn.listen()
wn.onkeypress(lambda: paddle_move(paddle_a, True), "w") #because passing arguments
wn.onkeypress(lambda: paddle_move(paddle_a, False), "s")
wn.onkeypress(lambda: paddle_move(paddle_b, True), "Up")
wn.onkeypress(lambda: paddle_move(paddle_b, False), "Down")

while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 22, "normal"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 22, "normal"))

    #paddle n ball collisions
    if (ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1 
        ball.setx(-340)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        ball.setx(340)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
       

    

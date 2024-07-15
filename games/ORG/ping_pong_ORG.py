import turtle
import math


wn = turtle.Screen()
wn.bgcolor("white")

timer_pen = turtle.Turtle()
timer_pen.hideturtle()
timer_pen.penup()
timer_pen.speed(10)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(10)
pen.goto(275, 350)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()

ball_dx = 15
ball_dy = 15

points = 0

def move_left():
    if (platform.xcor()) < (wn.window_width() / 2 + 25):
        platform.setx(platform.xcor() - 10)
def move_right():
    if (platform.xcor()) < (wn.window_width() / 2 - 25):
        platform.setx(platform.xcor() + 10)

wn.listen()
wn.onkeypress(key='Right', fun= move_right)
wn.onkeypress(key='Left', fun= move_left)

platform = turtle.Turtle()
platform.shape("square")
platform.shapesize(stretch_wid=1, stretch_len=3)
platform.color("green")
platform.penup()
platform.goto(0, -350) 

while True:
    pen.write(f"score: {points}", font=("Comic Sans MS", 30, "normal"))
    ball_new_x = (ball.xcor() - ball_dx )
    ball_new_y = (ball.ycor() - ball_dy )
    ball.goto(ball_new_x, ball_new_y)

    plat_x = platform.xcor()
    plat_y = platform.ycor()
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    
    # cal dist between plat and ball - (x1-x2)^2 + (y1-y2)^2
    plat_ball_dist = math.sqrt((plat_x-ball_x)*(plat_x-ball_x) + (plat_y-ball_y)*(plat_y-ball_y))

    if plat_ball_dist < 30:
        ball_dy *= -1
        pen.clear()
        points += 1
    elif abs(ball_x) > wn.window_width() / 2:
        ball_dx *= -1
    elif abs(ball_y) > wn.window_height() / 2:
        ball_dy *= -1

wn.mainloop()
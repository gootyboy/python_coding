import turtle
import math
import time
import random

wn = turtle.Screen()
wn.bgcolor("white")

start_timer = turtle.Turtle()
start_timer.hideturtle()
start_timer.penup
start_timer.speed(10)
start_timer.penup()
start_timer.write("loading...", font= ("Comic Sans MS", 30, "bold"))

platform = turtle.Turtle()
platform.hideturtle()
platform.shape("square")
platform_stretch_len = 3
platform.shapesize(stretch_wid=1, stretch_len=platform_stretch_len)
platform_len = platform_stretch_len * 20
platform.color("green")
platform.penup()
platform.goto(0, -350)

start_timer.goto(-380, 0)

ball = turtle.Turtle()
ball.hideturtle()
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(platform.xcor(), platform.ycor() +30)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(10)
pen.goto(-350, 350)
pen.color("black")

ball_dx = 100
ball_dy = 100
points = 2 ** 150
mf_x = 1
mf_y = 1

def move_left():
    if (platform.xcor()) < (wn.window_width() / 2 + 25):
        platform.setx(platform.xcor() - 10)
     
def move_right():
    if (platform.xcor()) < (wn.window_width() / 2 - 25):
        platform.setx(platform.xcor() + 10)

ball.showturtle()
platform.showturtle()
start_timer.color("black")
start_timer.clear()
start_timer.write("Make sure you wait for the ball to bounce off the platform", font= ("Comic Sans MS", 20, "normal"))
start_timer.goto(start_timer.xcor() - 35, start_timer.ycor() - 50)
start_timer.write("before moving the plaform, or else the screen will say game over", font= ("Comic Sans MS", 20, "normal"))

time.sleep(5)
start_timer.clear()
start_timer.home()

for i in reversed(range(1, 4)):
    start_timer.write(i, font = ("Comic Sans MS", 75, "normal"))
    time.sleep(1)
    start_timer.clear()

start_timer.write("Go!", font = ("Comic Sans MS", 75, "normal"))
time.sleep(0.2)
start_timer.clear()
ball_dy *= -1
while True:
    wn.onkeypress(key='Right', fun= move_right)
    wn.onkeypress(key='Left', fun= move_left)
    wn.listen()
    ball_faster_power_up_show = random.randint(-50, 50)
    if points < 10 ** 6:
        pen.write(f"score: {points}", font=("Comic Sans MS", 30, "normal"))
    elif points < 10 ** 9:
        pen.write(f"score: {str(int(points / (10 ** 6)))} million", font=("Comic Sans MS", 30, "normal"))
    elif points < 10 ** 12:
        pen.write(f"score: {str(int(points / (10 ** 9)))} billion", font=("Comic Sans MS", 30, "normal"))
    elif points < 10 ** 15:
        pen.write(f"score: {str(int(points / (10 ** 12)))} trillion", font=("Comic Sans MS", 30, "normal"))
    
    ball_new_x = (ball.xcor() - (ball_dy + mf_x*10) )
    ball_new_y = (ball.ycor() - (ball_dy + mf_y*10) )
    ball.goto(ball_new_x, ball_new_y)

    plat_x = platform.xcor()
    plat_y = platform.ycor()
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    # cal dist between plat and ball - sqrt((x1-x2)^2 + (y1-y2)^2)
    plat_ball_dist = math.sqrt((plat_x-ball_x)*(plat_x-ball_x) + (plat_y-ball_y)*(plat_y-ball_y))
    if plat_ball_dist < platform_len / 2 and ball_y < -300:
        mf_y *= -1
        ball_dy *= -1
        pen.clear()
        points *= 2
    elif abs(ball_x) > wn.window_width() / 2:
        ball_dx *= -1
        mf_x *= -1
    elif abs(ball_y) > wn.window_height() / 2:
        ball_dy *= -1
        mf_y *= -1
    if  ball_y< -390:
        platform.hideturtle()
        ball.hideturtle()
        pen.clear()
        pen.home()
        pen.write("Game Over", font= ("Comic Sans MS", 50, "bold"))
        break
wn.mainloop()
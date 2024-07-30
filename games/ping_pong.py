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

# ball_faster_power_up = turtle.Turtle()
# ball_faster_power_up.hideturtle()
# ball_faster_power_up.shape("circle")
# ball_faster_power_up.color("purple")
# ball_faster_power_up.penup()
# ball_faster_power_up.goto(0, wn.window_height() / 2)
# ball_faster_move = False

# ball_faster_timer = turtle.Turtle()
# ball_faster_timer.penup()
# ball_faster_timer.hideturtle()
# ball_faster_timer.speed(10)
# ball_faster_timer.goto( 200, 350)

platform = turtle.Turtle()
platform.hideturtle()
platform.shape("square")
platform_stretch_len = 100
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
ball_2 = turtle.Turtle()
ball_2.hideturtle()
ball_2.shape("circle")
ball_2.color("black")
ball_2.penup()
ball_2.goto(platform.xcor(), platform.ycor() +30)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(10)
pen.goto(275, 350)
pen.color("black")

ball_dx = 100
ball_dy = 100
ball_2_dx = 100
ball_2_dy = 100
points = 100
mf_x = 1
mf_y = 1

def move_left():
    if (platform.xcor()) < (wn.window_width() / 2 + 25):
        platform.setx(platform.xcor() - 10)
        
def move_right():
    if (platform.xcor()) < (wn.window_width() / 2 - 25):
        platform.setx(platform.xcor() + 10)

ball.showturtle()
ball_2.showturtle()
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
ball_2_dy *= -1
while True:
    wn.onkeypress(key='Right', fun= move_right)
    wn.onkeypress(key='Left', fun= move_left)
    wn.listen()
    ball_faster_power_up_show = random.randint(-50, 50)
    
    pen.write(f"score: {points}", font=("Comic Sans MS", 30, "normal"))
    # ball_faster_timer.clear()
    ball_new_x = (ball_2.xcor() - (ball_2_dy+ mf_x*10) )
    ball_new_y = (ball_2.ycor() - (ball_2_dy + mf_y*10) )
    ball_2_new_x = (ball_2.xcor() - (ball_2_dx+ mf_x*10) )
    ball_2_new_y = (ball_2.ycor() - (ball_2_dx + mf_y*10) )
    ball_2.goto(ball_new_x, ball_new_y)

    plat_x = platform.xcor()
    plat_y = platform.ycor()
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    # ball_faster_x = ball_faster_power_up.xcor()
    # ball_faster_y = ball_faster_power_up.ycor()
    
    # cal dist between plat and ball - sqrt((x1-x2)^2 + (y1-y2)^2)
    plat_ball_dist = math.sqrt((plat_x-ball_x)*(plat_x-ball_x) + (plat_y-ball_y)*(plat_y-ball_y))
    # plat_ball_faster_dist = math.sqrt((plat_x-ball_faster_x)*(plat_x-ball_faster_x) + (plat_y-ball_faster_y)*(plat_y-ball_faster_y))
    # if ball_faster_power_up_show == 1:
    #     ball_faster_power_up.showturtle()
    #     ball_faster_move = True
    # if ball_faster_move == True:
    #     ball_faster_stop += 1
    #     ball_faster_power_up.goto(ball_faster_power_up.xcor(), ball_faster_power_up.ycor() - 10)
    # if plat_ball_faster_dist < 300:
    #     mf_x=3
    #     mf_y=3
    #     ball_faster_power_up.teleport(0, wn.window_height() /2)
    #     ball_faster_move = False
    # if ball_faster_stop == 30:
    #     mf_x = 1
    #     mf_y = 1
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
    # ball_dy += 0.1
    # ball_dx += 0.1
    # print(ball_y)
wn.mainloop()
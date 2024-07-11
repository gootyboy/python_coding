import turtle
import random


stamp = turtle.Turtle()

stamp.shape("circle")
stamp.penup()
turtle.colormode(255)
stamp.speed(10)

paces = 20
random_red = 50
random_green = 50
random_blue = 50

for i in range(1, 500):
    random_red = random.randint(0, 255)
    random_green = random.randint(0, 255)
    random_blue = random.randint(0, 255)

    stamp.color(random_red, random_green, random_blue)
    stamp.stamp()
                
    paces += 1
    stamp.forward(paces)
    stamp.right(25)

import turtle
import random

FLOWER_WIDTH = 20
FLOWER_PETAL_HEIGHT = 5
NUMBER_OF_PETALS = 10 # petals will overlap for a number over 7
FLOWER_END_COLOR = (255, 0, 0)
FLOWER_POS = (0, 0)

stamp = turtle.Turtle()

stamp.shape("circle")
stamp.penup()
turtle.colormode(255)
stamp.speed(0)
stamp.shapesize(FLOWER_PETAL_HEIGHT, FLOWER_WIDTH)
stamp.teleport(FLOWER_POS[0], FLOWER_POS[1])

stamp_2 = turtle.Turtle()

stamp_2.shape("circle")
stamp_2.penup()
turtle.colormode(255)
stamp_2.speed(0)
stamp_2.shapesize(FLOWER_PETAL_HEIGHT, FLOWER_WIDTH)
stamp_2.teleport(FLOWER_POS[0], FLOWER_POS[1])

paces = 0
random_red = 50
random_green = 50
random_blue = 50

for i in range(1, int(NUMBER_OF_PETALS / 2)):
    random_red = random.randint(0, 255)
    random_green = random.randint(0, 255)
    random_blue = random.randint(0, 255)
    if i < int(NUMBER_OF_PETALS / 2) - 1:
        stamp.color(random_red, random_green, random_blue)
    else:
        stamp.color(FLOWER_END_COLOR[0], FLOWER_END_COLOR[1], FLOWER_END_COLOR[2])
    stamp.stamp()
                
    paces += 10
    stamp.left(paces)

    if i < int(NUMBER_OF_PETALS / 2) - 1:
        stamp_2.color(random_red, random_green, random_blue)
    else:
        stamp_2.color(FLOWER_END_COLOR[0], FLOWER_END_COLOR[1], FLOWER_END_COLOR[2])
    stamp_2.stamp()
    stamp_2.right(paces)

turtle.mainloop()
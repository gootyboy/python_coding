import turtle
import random
import _tkinter

FLOWER_WIDTH = 20
FLOWER_PETAL_HEIGHT = 5
NUMBER_OF_PETALS = 100 # petals will overlap
FLOWER_END_COLOR = (255, 0, 0)
FLOWER_POS = (0, 0)
NUM_OF_PETAL_DRAWERS = 100
SPEED_2 = 0

time = 0

stamps = [turtle.Turtle() for i in range(0, NUM_OF_PETAL_DRAWERS + 1)]
try:
    for stamp in stamps:
        stamp.shape("circle")
        stamp.penup()
        turtle.colormode(255)
        if SPEED_2 >= 10:
            stamp.speed(0)
        elif 9 <= SPEED_2 < 10:
            stamp.speed(10)
        elif 8 <= SPEED_2 < 9:
            stamp.speed(9)
        elif 7 <= SPEED_2 < 8:
            stamp.speed(8)
        elif 6 <= SPEED_2 < 7:
            stamp.speed(7)
        elif 5 <= SPEED_2 < 6:
            stamp.speed(6)
        elif 4 <= SPEED_2 < 5:
            stamp.speed(5)
        elif 3 <= SPEED_2 < 4:
            stamp.speed(4)
        elif 2 <= SPEED_2 < 3:
            stamp.speed(3)
        elif 1 <= SPEED_2 < 2:
            stamp.speed(2)
        else:
            stamp.speed(1)
        stamp.shapesize(FLOWER_PETAL_HEIGHT, FLOWER_WIDTH)
        stamp.teleport(FLOWER_POS[0], FLOWER_POS[1])
except turtle.Terminator:
    while True:
        pass

paces = 0
random_red = 50
random_green = 50
random_blue = 50
try:
    for i in range(int(NUM_OF_PETAL_DRAWERS / 2), int(NUMBER_OF_PETALS / NUM_OF_PETAL_DRAWERS)):
        random_red = random.randint(0, 255)
        random_green = random.randint(0, 255)
        random_blue = random.randint(0, 255)
        for index, stamp in enumerate(stamps):
            if i < int(NUMBER_OF_PETALS / NUM_OF_PETAL_DRAWERS) - 1:
                stamp.color(random_red, random_green, random_blue)
            else:
                stamp.color(FLOWER_END_COLOR[0], FLOWER_END_COLOR[1], FLOWER_END_COLOR[2])
            stamp.stamp()
            if index % 2 == 1:
                stamp.left(paces)
            else:
                stamp.right(paces)
            paces += 10
except turtle.Terminator:
    while True:
        pass

turtle.textinput()

try:
    turtle.mainloop()
except _tkinter.TclError:
    while True:
        pass
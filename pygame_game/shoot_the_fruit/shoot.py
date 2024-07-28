from pgzero.actor import Actor
import pgzrun
from random import randint

actor = randint(1, 3)

amount_of_hits = 0
apple = Actor("apple")

def draw():
    actor = randint(1, 3)
    if actor == 1:
        apple = Actor("apple")
    elif actor == 2:
        apple = Actor("orange")
    else:
        apple = Actor("pineapple")
    apple.draw()

def place_actor():
    apple.x = randint(10, 100)
    apple.y = randint(10, 400)

def on_mouse_down(pos):
    global amount_of_hits

    if apple.collidepoint(pos):
        place_actor()
        amount_of_hits += 1
        print(amount_of_hits)

place_actor()
pgzrun.go()
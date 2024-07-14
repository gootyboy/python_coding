from pgzero.actor import Actor
import pgzrun
from random import randint

amount_of_hits = 0
apple = Actor("apple")


def draw():
    apple.draw()

def place_actor():
    apple.x = randint(10, 400)
    apple.y = randint(10, 400)

def on_mouse_down(pos):
    global amount_of_hits

    if apple.collidepoint(pos):
        place_actor()
        amount_of_hits += 1
        print(amount_of_hits)

place_actor()
pgzrun.go()
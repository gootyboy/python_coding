from pgzero.actor import Actor
import pgzrun
from random import randint

actor = randint(1, 3)

amount_of_hits = 0
apple = Actor("apple")
actor = randint(1, 3)
if actor == 1:
    apple = Actor("apple")
elif actor == 2:
    apple = Actor("orange")
else:
    apple = Actor("pineapple")
apple.x = randint(0, 700)
apple.y = randint(0, 700)

def draw():
    screen.clear()
    screen.draw.text(f"Score: {amount_of_hits}", color= "white", bottomleft= (10, 600))
    apple.draw()

def on_mouse_down(pos):
    global amount_of_hits, apple

    if apple.collidepoint(pos):
        amount_of_hits += 1
        actor = randint(1, 3)
        if actor == 1:
            apple = Actor("apple")
        elif actor == 2:
            apple = Actor("orange")
        else:
            apple = Actor("pineapple")
        apple.x = randint(10, 100)
        apple.y = randint(10, 400)

pgzrun.go()
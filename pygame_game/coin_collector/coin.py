import pgzrun
from pgzero.actor import Actor
from random import randint

WIDTH = 700
HEIGHT = 600
score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100
coin = Actor("coin")
coin.pos = 200, 200

speed = 10

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft =(10, 10))

    if game_over:
        screen.clear()
        screen.fill("green")
        screen.draw.text("Final Score: " + str(score), color= "black", center = ((WIDTH / 2), 50), fontsize = 60)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over

    game_over = True

def update():
    if keyboard.left:
        fox.x -= speed
    elif keyboard.right:
        fox.x += speed
    elif keyboard.up:
        fox.y -= speed
    elif keyboard.down:
        fox.y += speed

clock.schedule(time_up, 10.0)
place_coin()

pgzrun.go()
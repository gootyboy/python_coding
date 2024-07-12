import pgzrun
import time
from pgzero.actor import Actor
from random import randint

WIDTH = 700
HEIGHT = 600
fox_score = 0
hedgehog_score = 0
game_over = False
player_speed = 10

fox = Actor("fox")
fox.pos = 100, 100
hedgehog = Actor("hedgehog")
hedgehog.pos = 400, 400
coin = Actor("coin")
coin.pos = 200, 200

def draw():

    screen.fill("green")
    fox.draw()
    coin.draw()
    hedgehog.draw()
    screen.draw.text("Fox score: " + str(fox_score), color="black", topleft =(10, 10))
    screen.draw.text("Hedgehog score: " + str(hedgehog_score), color="black", topleft =(10, 30))

    if game_over:
        screen.clear()
        screen.fill("green")
        screen.draw.text("Fox Score: " + str(fox_score), color= "black", center = ((WIDTH / 2), 50), fontsize = 60)
        screen.draw.text("Hedgehog Score: " + str(hedgehog_score), color= "black", center = ((WIDTH / 2), 100), fontsize = 60)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over

    game_over = True

def update():
    global hedgehog_score, fox_score

    if fox.x > 20:
        if keyboard.left:
            fox.x -= player_speed
    if fox.x < (WIDTH -20):
        if keyboard.right:
            fox.x += player_speed
    if fox.y > 20:
        if keyboard.up:
            fox.y -= player_speed
    if fox.y < (HEIGHT -20):
        if keyboard.down:
            fox.y += player_speed

    if hedgehog.x > 20:
        if keyboard.a:
            hedgehog.x -= player_speed
    if hedgehog.x < (WIDTH -20):
        if keyboard.d:
            hedgehog.x += player_speed
    if hedgehog.y > 20:
        if keyboard.w:
            hedgehog.y -= player_speed
    if hedgehog.y < (HEIGHT -20):
        if keyboard.s:
            hedgehog.y += player_speed


    fox_coin_collected = fox.colliderect(coin)
    hedgehog_coin_collected = hedgehog.colliderect(coin)

    if fox_coin_collected:
        fox_score += 10
        place_coin()
    
    if hedgehog_coin_collected:
        hedgehog_score += 10
        place_coin()

clock.schedule(time_up, 60.0)
place_coin()

pgzrun.go()
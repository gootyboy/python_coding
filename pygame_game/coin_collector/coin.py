import pgzrun
from pgzero.actor import Actor
from random import randint

WIDTH = 700
HEIGHT = 600
fox_score = 0
hedgehog_score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100
hedgehog = Actor("hedgehog")
hedgehog.pos = 400, 400
coin = Actor("coin")
coin.pos = 200, 200

speed = 2

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
        screen.draw.text("Final Score: " + str(score), color= "black", center = ((WIDTH / 2), 50), fontsize = 60)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over

    game_over = True

def update():
    global hedgehog_score, fox_score

    if keyboard.left:
        fox.x -= speed
    elif keyboard.right:
        fox.x += speed
    elif keyboard.up:
        fox.y -= speed
    elif keyboard.down:
        fox.y += speed

    if keyboard.a:
        hedgehog.x -= speed
    elif keyboard.d:
        hedgehog.x += speed
    elif keyboard.w:
        hedgehog.y -= speed
    elif keyboard.s:
        hedgehog.y += speed

    fox_coin_collected = fox.colliderect(coin)
    hedgehog_coin_collected = hedgehog.colliderect(coin)

    if fox_coin_collected:
        fox_score += 10
        place_coin()
    
    if hedgehog_coin_collected:
        hedgehog_score += 10
        place_coin()

# clock.schedule(time_up, 10.0)
place_coin()

pgzrun.go()
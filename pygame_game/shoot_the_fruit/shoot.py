from pgzero.actor import Actor
import pgzrun
import random 

WIDTH = 800
HEIGHT = 600

amount_of_hits = 0
apple = Actor(random.choice(["apple", "orange", "pineapple"]))
apple.x = random.randint(100, WIDTH - 100)
apple.y = random.randint(100, HEIGHT - 100)

def draw():
    screen.clear()
    screen.draw.text(f"Score: {amount_of_hits}", color= "white", bottomleft= (10, 600))
    apple.draw()

def on_mouse_down(pos):
    global amount_of_hits, apple

    if apple.collidepoint(pos):
        if (amount_of_hits + 1) % 100 == 0 and amount_of_hits >= 100:
            apple = Actor("pineapple_2", (WIDTH / 2, HEIGHT / 2))
            amount_of_hits += 100
        elif (amount_of_hits + 1) % 50 == 0 and amount_of_hits >= 50:
            apple = Actor("orange_2", (WIDTH / 2, HEIGHT / 2))
            amount_of_hits += 50
        elif amount_of_hits % 10 == 0 and amount_of_hits >= 10:
            apple = Actor("apple_2", (WIDTH / 2, HEIGHT / 2))
            amount_of_hits += 9999999999999999999999999999999999999999999999999999999999999999999999
        else:
            apple = Actor(random.choice(["apple", "orange", "pineapple"]))
            apple.x = random.randint(100, WIDTH - 100)
            apple.y = random.randint(100, HEIGHT - 100)
            amount_of_hits += 1

pgzrun.go()
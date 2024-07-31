import pgzrun
import pygame
from pgzero.actor import Actor
from random import randint
import balloon

WIDTH = 800
HEIGHT = 600
speed_1 = 1
speed_2 = 1
speed_3 = 2

balloon = Actor("balloon")
balloon.pos = 400, 300

bird = Actor("bird-up")
bird.pos = randint(800, 1600), randint(10, 200)

house = Actor("house")
house.pos = randint(800, 1600), 460

tree = Actor("tree")
tree.pos = randint(800, 1600), 450

bird_up = True
up = False
game_over = False
score = 0
number_of_updates = 0

scores = []

def update_high_scores():
    pass

def display_high_scores():
    pass

def draw():
    screen.blit("background", (0, 0))
    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text("Score: " + str(score), (700, 5), color= "black")
    else:
        display_high_scores()

def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird_up = True

def update():
    global game_over, score, number_of_updates, up, speed_1, speed_2, speed_3
    if not game_over:
        if keyboard.SPACE:
            up = True
            balloon.y -= speed_1
        else:
            up = False
        if keyboard.up:
            speed_1 = 3
        else:
            speed_1 = 1
        if keyboard.right:                                                                                                        
            speed_3 = 10
        else:
            speed_3 = 2
        if keyboard.left:
            speed_3 = 1
        else:
            speed_3 = 3
        if keyboard.down:
            speed_2 = 3
        else:
            speed_2 = 1
        if not up:
            balloon.y += speed_2
        if bird.x > 0:
            bird.x -= speed_3 * 2
            if number_of_updates == 30:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        else:
            bird.x = randint(800, 1600)
            bird.y = randint(10, 200)
            score += 1
            number_of_updates = 0
        if house.right > 0:
            house.x -= speed_3
        else:
            house.x = randint(800, 1600)
            score += 1
        if tree.right > 0:
            tree.x -= speed_3
        else:
            tree.x = randint(800, 1600)
            score += 1
        if balloon.top < 0 or balloon.bottom > 560:
            game_over = True
            update_high_scores()
        if balloon.collidepoint(bird.x, bird.y) or balloon.collidepoint(house.x, house.y) or balloon.collidepoint(tree.x, tree.y):
            game_over = True
            update_high_scores()
pgzrun.go()
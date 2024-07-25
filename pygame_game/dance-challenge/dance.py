import pgzrun
import pygame
from pgzero.actor import Actor
from pgzero.clock import clock
from random import randint

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

move_list = []
display_list = []
score = 0
current_move = 0
count = 4
dance_length = 4 

say_dance = False
show_countdown = True
moves_complete = False
game_over = False

dancer = Actor("dancer-start", pos=(CENTER_X + 5, CENTER_Y - 40))
up = Actor("up", pos=(CENTER_X, CENTER_Y + 110))
right = Actor("right", pos=(CENTER_X + 60, CENTER_Y + 170))
down = Actor("down", pos=(CENTER_X, CENTER_Y + 230))
left = Actor("left", pos=(CENTER_X - 60, CENTER_Y + 170))

def draw():
    global game_over, score, say_dance, count, show_countdown
    if not game_over:
        screen.blit("stage",(0, 0))
        dancer.draw()
        up.draw()
        down.draw()
        right.draw()
        left.draw()
        screen.draw.text("Score: " + str(score), color= "black", topleft=(10, 10))

def reset_dancer():
    global game_over
    if not game_over:
        dancer.image = "dancer-start"


def update_dancer(move):
    global game_over
    if not game_over:
        if move == 0:
            up.image = "up-lit"
            dancer.image = "dancer-right"
            clock.schedule(reset_dancer, 0.5)
        elif move == 1:
            right.image = "right-lit"
            dancer.image = "dancer-right"
            clock.schedule(reset_dancer, 0.5)
        elif move == 2:
            down.image = "down-lit"
            dancer.image = "dancer-down"
            clock.schedule(reset_dancer, 0.5)
        elif move == 3:
            left.image = "left-lit"
            dancer.image = "dancer-left"
            clock.schedule(reset_dancer, 0.5)

def display_moves():
    pass

def generate_moves():
    pass

def countdown():
    pass

def next_move():
    pass

def on_key_up(key):
    pass

def update():
    pass

pgzrun.go()
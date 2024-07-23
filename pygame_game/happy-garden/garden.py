import time
import pgzrun
from pgzero.actor import Actor
from random import randint

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

game_over = False
finalized = False
garden_happy = True
fangflower_collision = False

time_elapsed = 0
start_time = time.time()

flower_list = []
wilted_list = []
fangflower_list = []
fangflower_vy_list = []
fangflower_vx_list = []

cow = Actor("cow", pos=(100, 500))

def draw():
    global game_over, time_elapsed, finalized
    if not game_over:
        screen.blit("garden", (0, 0))
        cow.draw()

pgzrun.go()
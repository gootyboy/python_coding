import pgzrun
import random
from pgzero.actor import Actor
from pgzero.keyboard import keyboard

WIDTH = 806
HEIGHT = 600

PLAYER_X_START = 25
PLAYER_Y_START = HEIGHT - 91
JUMP_HEIGHT = 20
PLAYER_SPEED_MF = 1 # 1 is normal, 2 is 2 times normal, 3 is 3 times normal, and so on.

player = Actor('hero', (PLAYER_X_START, PLAYER_Y_START))
game_over = False
win = False
jumped = False
jump_timer = 0
start_3 = 6 * 62
start_2 = 5 * 62
start_1 = 2 * 62
starts = [start_1]

def make_floor_stones():
    floor_stones = []
    for i in range(31, WIDTH, 62):
        floor_stones.append(Actor("stone", (i, 569)))
    return floor_stones

def make_other_stones():
    global starts
    stones = []
    for start_index in range(0, len(starts)):
        for i in range(starts[start_index] + 31, WIDTH, 62):
            stones.append(Actor("stone", (i, 569 - ((start_index + 1) * 62))))
    return stones

def draw():
    screen.fill("white")
    for stone in make_floor_stones() + make_other_stones():
        stone.draw()
    player.draw()
    if game_over:
        screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2), fontsize=50, color="red")
    if win:
        screen.draw.text("You Win!", center=(WIDTH/2, HEIGHT/2), fontsize=50, color="green")

def update():
    global jumped, jump_timer, win, game_over, starts

    if player.x < starts[0] and player.y == PLAYER_Y_START - 62:
        player.y = PLAYER_Y_START
    if player.x < starts[0] and player.y == PLAYER_Y_START - 62:
        player.y = PLAYER_Y_START

    if keyboard.left:
        if player.x > PLAYER_X_START:
            player.x -= PLAYER_SPEED_MF * 5
        else:
            player.x == PLAYER_X_START

    if keyboard.right:
        if player.x < WIDTH - PLAYER_X_START:
            player.x += PLAYER_SPEED_MF * 5
        else:
            player.x = WIDTH - PLAYER_X_START

    if keyboard.up and not jumped:
        jumped = True
        jump_timer = JUMP_HEIGHT / PLAYER_SPEED_MF

    if jumped:
        if jump_timer > 0:
            player.y -= PLAYER_SPEED_MF * 5
            jump_timer -= 1
        else:
            player.y += PLAYER_SPEED_MF * 5
            if player.x < starts[0]:
                if player.y >= PLAYER_Y_START:
                    player.y = PLAYER_Y_START
                    jumped = False
            else:
                if player.y >= PLAYER_Y_START - 62:
                    player.y = PLAYER_Y_START - 62
                    jumped = False

pgzrun.go()
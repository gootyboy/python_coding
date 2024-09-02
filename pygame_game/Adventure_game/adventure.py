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
STONE_HEIGHT = 62 # don't change

player = Actor('hero', (PLAYER_X_START, PLAYER_Y_START))
game_over = False
win = False
jumped = False
jump_timer = 0
starts_x = [2 * STONE_HEIGHT, WIDTH - (STONE_HEIGHT * 4)]
ends_x = [WIDTH - (STONE_HEIGHT * 2), WIDTH]

def make_stones():
    global starts_x
    stones = []
    for start_index in range(0, len(starts_x)):
        for i in range(starts_x[start_index] + 31, ends_x[start_index], STONE_HEIGHT):
            stones.append(Actor("stone", (i, 569 - ((start_index + 1) * STONE_HEIGHT))))
    for i in range(31, WIDTH, STONE_HEIGHT):
        stones.append(Actor("stone", (i, 569)))
    return stones

def draw():
    screen.fill("white")
    for stone in make_stones():
        stone.draw()
    player.draw()
    if game_over:
        screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2), fontsize=50, color="red")
    if win:
        screen.draw.text("You Win!", center=(WIDTH/2, HEIGHT/2), fontsize=50, color="green")

def update():
    global jumped, jump_timer, win, game_over, starts_x

    if player.x < starts_x[0] and player.y == PLAYER_Y_START - STONE_HEIGHT:
        player.y = PLAYER_Y_START

    if keyboard.left:
        if player.x > PLAYER_X_START:
            player.x -= PLAYER_SPEED_MF * 5
        else:
            player.x == PLAYER_X_START

    if keyboard.right:
        # print(WIDTH, PLAYER_X_START)
        if player.x < WIDTH - PLAYER_X_START:
            for i in range(0, len(starts_x)):
                # print (player.y, PLAYER_Y_START, STONE_HEIGHT*i)
                # if player.y == PLAYER_Y_START - (STONE_HEIGHT*(i+1)):

                if player.x < starts_x[i] or player.y == PLAYER_Y_START - (STONE_HEIGHT * (i + 1)):
                    player.x += PLAYER_SPEED_MF * 5

    if keyboard.up and not jumped:
        jumped = True
        jump_timer = JUMP_HEIGHT / PLAYER_SPEED_MF

    if jumped:
        if jump_timer > 0:
            player.y -= PLAYER_SPEED_MF * 5
            jump_timer -= 1
        else:
            player.y += PLAYER_SPEED_MF * 5
            if player.x < starts_x[0]:
                if player.y >= PLAYER_Y_START:
                    player.y = PLAYER_Y_START
                    jumped = False
            else:
                if player.y >= PLAYER_Y_START - STONE_HEIGHT:
                    player.y = PLAYER_Y_START - STONE_HEIGHT
                    jumped = False

pgzrun.go()
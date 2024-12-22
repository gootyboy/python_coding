import pgzrun
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
fall_timer = 0
starts_x = [2 * STONE_HEIGHT, WIDTH - (STONE_HEIGHT * 4), WIDTH - (STONE_HEIGHT * 2), 0, 0]
ends_x = [WIDTH, WIDTH, WIDTH, 0, WIDTH - (STONE_HEIGHT * 3)]
stones_dict = {}
stones_level = 0
counter=0
current_level = 0

def make_stones():
    global starts_x, stones_dict, stones_level
    stones = []
    for start_index in range(0, len(starts_x)):
        # print(start_index + 1)
        counter=0        
        for i in range(starts_x[start_index] + 31, ends_x[start_index], STONE_HEIGHT):
            stones.append(Actor("stone", (i, 569 - ((start_index + 1) * STONE_HEIGHT))))

            if (counter==0):
                stones_dict[start_index+1] = Actor("stone", (i, 569 - ((start_index + 1) * STONE_HEIGHT)))

            counter+=1

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

def handle_jumping():
    global jumped, jump_timer, win, game_over, starts_x, fall_timer
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

def update_player_level():
    global stones_dict, current_level
    for key in stones_dict:
        # print(player.y)
        # print(key, ", topleft:" ,stones_dict[key].y, ", bottomleft:" ,stones_dict[key].y - stones_dict[key].height)
        if stones_dict[key].y >= player.y-10 >= stones_dict[key].y - stones_dict[key].height:
            current_level=key-1
    print('current_level',current_level)

def update():
    global jumped, jump_timer, win, game_over, starts_x, fall_timer,current_level

    check_player_y = PLAYER_Y_START >= player.y >= PLAYER_Y_START - STONE_HEIGHT
    if player.x < starts_x[0] and check_player_y and not jumped:
        fall_timer = STONE_HEIGHT / PLAYER_SPEED_MF
        if fall_timer > 0:
            player.y += PLAYER_SPEED_MF * 5
            fall_timer -= 1
        else:
            player.y -= PLAYER_SPEED_MF * 5 
            if player.y >= PLAYER_Y_START:
                player.y = PLAYER_Y_START
                fall_timer = 0

    if keyboard.left:
        if player.x > PLAYER_X_START:
            player.x -= PLAYER_SPEED_MF * 5

    if keyboard.right:
        player_hit_the_wall = player.distance_to(stones_dict[current_level + 1])-player.width/2 <= 6
        if player_hit_the_wall:
            return

        if player.x < starts_x[0] or player.y <= PLAYER_Y_START - STONE_HEIGHT:
            if player.x < WIDTH - PLAYER_X_START:
                for i in range(0, len(starts_x)):
                    if player.x < starts_x[i] or player.y == PLAYER_Y_START - (STONE_HEIGHT * (i + 1)):
                        player.x += PLAYER_SPEED_MF * 5
        
        # if (player.distance_to(stones_dict[current_level + 1])-player.width/2 <= 6):
        #     print('player hit a wall')

        # print(player.distance_to(stones_dict[current_level])-player.width/2)
    handle_jumping()
    update_player_level()

pgzrun.go()
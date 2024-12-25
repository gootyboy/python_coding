import pgzrun
import random
from pgzero.actor import Actor
from pgzero.keyboard import keyboard

WIDTH = 806
HEIGHT = 600

PLAYER_X_START = 25
PLAYER_Y_START = HEIGHT - 91
JUMP_HEIGHT = 20
PLAYER_SPEED_MF = 1
STONE_HEIGHT = Actor("stone").height
NUMBER_OF_SPIKES = 3 # Maxium: 3 for first level only

players = [Actor('hero'), Actor("fox"), Actor("hedgehog"), Actor("weasel")]
game_over = False
win = False
jumped = False
game_started = False
jump_timer = 0
starts_x = [2 * STONE_HEIGHT, WIDTH - (STONE_HEIGHT * 4), WIDTH - (STONE_HEIGHT * 2), WIDTH - STONE_HEIGHT, 0]
ends_x = [WIDTH, WIDTH, WIDTH, WIDTH, WIDTH - (STONE_HEIGHT * 3)]
spikes = []
stones_dict = {}
stones_level = 0
counter = 0
current_level = 0
fall_timer = (STONE_HEIGHT / 5) / PLAYER_SPEED_MF

def make_stones():
    global starts_x, stones_dict, stones_level, stones
    stones = []
    for start_index in range(0, len(starts_x)):
        counter = 0        
        for i in range(starts_x[start_index] + int(STONE_HEIGHT / 2), ends_x[start_index], STONE_HEIGHT):
            stones.append(Actor("stone", (i, (HEIGHT - STONE_HEIGHT / 2) - ((start_index + 1) * STONE_HEIGHT))))

            if counter == 0:
                stones_dict[start_index + 1] = Actor("stone", (i, (HEIGHT - STONE_HEIGHT / 2) - ((start_index + 1) * STONE_HEIGHT)))

            counter += 1

    for i in range(int(STONE_HEIGHT / 2), WIDTH, STONE_HEIGHT):
        stones.append(Actor("stone", (i, (HEIGHT - STONE_HEIGHT / 2))))
    
def make_spikes():
    global spikes
    spikes = []
    random_xs = []
    for i in range(NUMBER_OF_SPIKES):
        if i == 0:
            random_x = random.randint(starts_x[0] + int(Actor("spikes").width / 2), starts_x[1] - int(Actor("spikes").width / 2))
        else:
            while True:
                spike_overlap = False
                for x in random_xs: 
                    if abs(x - random_x) <= Actor("spikes").width:
                        spike_overlap = True
                        break
                    else:
                        spike_overlap = False
                        continue
                if spike_overlap == True:
                    random_x = random.randint(starts_x[0] + int(Actor("spikes").width / 2), starts_x[1] - int(Actor("spikes").width / 2))
                else:
                    break
        random_xs.append(random_x)
        spikes.append(Actor("spikes", (random_x, PLAYER_Y_START - STONE_HEIGHT)))

make_stones()
make_spikes()

def draw():
    global spikes, game_started, player, players
    screen.blit("sky.png", (0, 0))
    screen.blit("sky.png", (800, 0))
    if game_started:
        for stone in stones:
            stone.draw()
        for spike in spikes:
            spike.draw()
        player.draw()
    else:
        screen.draw.text("Choose Your Character", center=(WIDTH / 2, 50), fontsize=50, color="black")
        for i in range(len(players)):
            players[i].pos = 170 + 150 * i, 125
            players[i].draw()
            screen.draw.text(str(players[i].image), midbottom=(170 + 150 * i, players[i].y + 50), fontsize=30, color="black")

    if game_over:
        screen.draw.text("Game Over", center=(WIDTH / 2, HEIGHT / 2), fontsize=50, color="red")
    if win:
        screen.draw.text("You Win!", center=(WIDTH / 2, HEIGHT / 2), fontsize=50, color="green")

def handle_jumping():
    global jumped, jump_timer, win, game_over, starts_x, fall_timer
    if keyboard.up and not jumped:
        jumped = True
        jump_timer = JUMP_HEIGHT / PLAYER_SPEED_MF

    if jumped:
        if jump_timer > 0:
            for stone in stones: 
                if player.colliderect(stone):
                    collision = True
                    break
                else:
                    collision = False
            if collision == False:
                player.y -= PLAYER_SPEED_MF * 5
            jump_timer -= 1
        else:
            player.y += PLAYER_SPEED_MF * 5
            if player.y >= PLAYER_Y_START:
                player.y = PLAYER_Y_START
                jumped = False
            for i in range(0, len(starts_x)):
                if starts_x[i] <= player.x <= ends_x[i]:
                    if PLAYER_Y_START - (STONE_HEIGHT * (i + 1)) <= player.y <= PLAYER_Y_START - (STONE_HEIGHT * i):
                        player.y = PLAYER_Y_START - (STONE_HEIGHT * (i + 1))
                        jumped = False

def update_player_level():
    global stones_dict, current_level
    for key in stones_dict:
        if stones_dict[key].y >= player.y - 10 >= stones_dict[key].y - stones_dict[key].height:
            current_level = key - 1

def update():
    global jumped, jump_timer, win, game_over, starts_x, fall_timer, current_level, stones_dict, game_started

    if game_started:
        for i in range(len(starts_x)):
            if player.y == PLAYER_Y_START - (STONE_HEIGHT * (i + 1)):
                fall_timer = (STONE_HEIGHT / PLAYER_SPEED_MF) / 5
            check_player_y = PLAYER_Y_START - (STONE_HEIGHT * i) > player.y >= PLAYER_Y_START - (STONE_HEIGHT * (i + 1))
            if player.x < starts_x[i] and check_player_y and not jumped:
                if fall_timer > 1:
                    player.y += PLAYER_SPEED_MF * 5
                    fall_timer -= 1
                else:
                    player.y = PLAYER_Y_START - (STONE_HEIGHT * i)
                    fall_timer = 0

        if keyboard.left:
            if player.x > PLAYER_X_START:
                player.x -= PLAYER_SPEED_MF * 5

        if keyboard.right:
            player.y -= 10
            player_hit_the_wall = player.distance_to(stones_dict[current_level + 1]) - player.width / 2 <= 10
            if player_hit_the_wall:
                player.y += 10
                player.x -= PLAYER_SPEED_MF
                return
            player.y += 10
            if player.x < WIDTH - PLAYER_X_START:
                player.x += PLAYER_SPEED_MF * 5

        handle_jumping()
        update_player_level()

def on_mouse_down(pos):
    global game_started, players, player
    if not game_started:
        for character in players:
            print(pos, character.pos, character.collidepoint(pos))
            if character.collidepoint(pos):
                player = character
                print(player)
                game_started = True
                character.pos = PLAYER_X_START, PLAYER_Y_START
                player = character
                game_started = True

pgzrun.go()
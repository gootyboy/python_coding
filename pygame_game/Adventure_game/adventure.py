import pgzrun
import pygame
import random
from pgzero.rect import Rect
from pgzero.actor import Actor
from PIL import ImageSequence, Image
from pgzero.keyboard import keyboard

WIDTH = 806
HEIGHT = 600

PLAYER_X_START = 25
PLAYER_Y_START = HEIGHT - 91
JUMP_HEIGHT = 20
PLAYER_SPEED_MF = 1
STONE_HEIGHT = Actor("stone").height
NUMBER_OF_SPIKES = 1 # Maxium: 3 for first level only
STAR_SPEED = 0.05 #less is faster

players = [Actor('hero_right'), Actor("fox_right"), Actor("hedgehog_right")] #, Actor("weasel")]
game_over = False
win = False
jumped = False
game_started = False
jump_timer = 0
starts_x = [2 * STONE_HEIGHT, WIDTH - (STONE_HEIGHT * 4), WIDTH - (STONE_HEIGHT * 2), WIDTH - STONE_HEIGHT, 0]
ends_x = [WIDTH, WIDTH, WIDTH, WIDTH, WIDTH - (STONE_HEIGHT * 3)]
spikes = []
STAR_POS = (starts_x[-1], PLAYER_Y_START - (Actor("star").height / 2) - (len(starts_x) * STONE_HEIGHT) - 15)
stones_dict = {}
stones_level = 0
counter = 0
current_level = 0
player = None
fall_timer = (STONE_HEIGHT / 5) / PLAYER_SPEED_MF
frames = [frame.copy() for frame in ImageSequence.Iterator(Image.open(r'C:\Projects\boy\pygame_game\adventure_game\images\star.gif'))]
current_frame = 0
last_update_time = 0

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
    times_ran = 0 
    for i in range(NUMBER_OF_SPIKES):
        spike_name = "spikes"
        if i == 0:
            random_x = random.randint(starts_x[0] + int(Actor(spike_name).width / 2), starts_x[1] - int(Actor(spike_name).width / 2)) 
        else: 
            while True: 
                if times_ran >= 100:
                    i = -1
                    times_ran = 0
                    random_xs = []
                    break
                spike_overlap = False
                for x in random_xs: 
                    if abs(x - random_x) <= Actor(spike_name).width: 
                        spike_overlap = True 
                        break 
                    else: 
                        spike_overlap = False 
                        continue 
                if spike_overlap: 
                    random_x = random.randint(starts_x[0] + int(Actor(spike_name).width / 2), starts_x[1] - int(Actor(spike_name).width / 2))
                else:
                    break
                times_ran += 1 
        random_xs.append(random_x) 
        spikes.append(Actor(spike_name, (random_x, PLAYER_Y_START - STONE_HEIGHT)))

make_stones()
make_spikes()

def draw_star_gif(pos):
    global current_frame
    frame_image = frames[current_frame]
    screen.blit(pygame.image.fromstring(frame_image.convert("RGBA").tobytes(), frame_image.size, "RGBA"), pos)

def draw():
    global spikes, game_started, player, players, yes_rect, no_rect, starts_x
    screen.blit("sky.png", (0, 0))
    screen.blit("sky.png", (800, 0))
    if not game_over:
        if game_started:
            draw_star_gif(STAR_POS)
            for stone in stones:
                stone.draw()
            for spike in spikes:
                spike.draw()
            player.draw()
        else:
            screen.draw.text("Choose Your Character", center=(WIDTH / 2, 50), fontsize=50, color=(0, 0, 0))
            for i in range(len(players)):
                players[i].pos = 170 + 150 * i, 125
                players[i].draw()
                screen.draw.text(str(players[i].image.removesuffix("_right")), midbottom=(170 + 150 * i, players[i].y + 50), fontsize=30, color=(0, 0, 0))

    if game_over:
        rect_color = (100, 100, 150)
        yes_rect = Rect(WIDTH / 2 - 215, HEIGHT / 2, 75, 75)
        no_rect = Rect(WIDTH / 2 + 125, HEIGHT / 2, 75, 75)
        screen.draw.text("Game Over", center=(WIDTH / 2, HEIGHT / 2 - 100), fontsize=100, color=(255, 0, 0))
        screen.draw.text("Do you want to play agian?", center=(WIDTH / 2, HEIGHT / 2 - 50), fontsize=50, color=(0, 0, 0))
        screen.draw.filled_rect(yes_rect, color=rect_color)
        screen.draw.textbox("Yes", yes_rect, color=(0, 0, 0))
        screen.draw.filled_rect(no_rect, color = rect_color)
        screen.draw.textbox("No", no_rect, color=(0, 0, 0))
    if win:
        screen.draw.text("You Win!", center=(WIDTH / 2, HEIGHT / 2), fontsize=100, color=(0, 255, 0))
        screen.draw.text("Do you want to play agian?", center=(WIDTH / 2, HEIGHT / 2 - 50), fontsize=50, color=(0, 0, 0))
        screen.draw.filled_rect(yes_rect, color=rect_color)
        screen.draw.textbox("Yes", yes_rect, color=(0, 0, 0))
        screen.draw.filled_rect(no_rect, color = rect_color)
        screen.draw.textbox("No", no_rect, color=(0, 0, 0))

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

def handle_falling():
    global jumped, starts_x, fall_timer, player, current_frame, last_update_time
    if pygame.time.get_ticks() - last_update_time > STAR_SPEED * 1000:
        current_frame = (current_frame + 1) % len(frames)
        last_update_time = pygame.time.get_ticks()
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

def update():
    global win, game_over, current_level, stones_dict, game_started, spikes, player
    
    if game_started:
        if not game_over and not win:
            handle_falling()

            if keyboard.left:
                if player.image.split("_")[1] == "right":
                    player.image = player.image.replace("right", "left")
                if player.x > PLAYER_X_START:
                    player.x -= PLAYER_SPEED_MF * 5

            if keyboard.right:
                if player.image.split("_")[1] == "left":
                    player.image = player.image.replace("left", "right")
                player.y -= 10
                player_hit_the_wall = player.distance_to(stones_dict[current_level + 1]) - player.width / 2 <= 10
                if player_hit_the_wall:
                    player.y += 10
                    player.x -= PLAYER_SPEED_MF
                    return
                player.y += 10
                if player.x < WIDTH - PLAYER_X_START:
                    player.x += PLAYER_SPEED_MF * 5
            
            for spike in spikes:
                if player.distance_to(spike) < 50:
                    game_over = True
            
            if Actor("star", STAR_POS).colliderect(player):
                win = True

            handle_jumping()
            update_player_level()

def restart_game():
    global players, game_over, win, jumped, jump_timer, game_started, starts_x, ends_x, spikes, stones_dict, stones_level, counter, current_level, fall_timer, stones, player, frames, current_frame, last_update_time
    players = [Actor('hero_right'), Actor("fox_right"), Actor("hedgehog_right")]
    game_over = False
    win = False
    jumped = False
    game_started = False
    jump_timer = 0
    starts_x = [2 * STONE_HEIGHT, WIDTH - (STONE_HEIGHT * 4), WIDTH - (STONE_HEIGHT * 2), WIDTH - STONE_HEIGHT, 0]
    ends_x = [WIDTH, WIDTH, WIDTH, WIDTH, WIDTH - (STONE_HEIGHT * 3)]
    spikes = []
    stones = []
    stones_dict = {}
    stones_level = 0
    counter = 0
    current_level = 0
    fall_timer = (STONE_HEIGHT / 5) / PLAYER_SPEED_MF
    player = None
    frames = [frame.copy() for frame in ImageSequence.Iterator(Image.open(r'C:\Projects\boy\pygame_game\adventure_game\images\star.gif'))]
    current_frame = 0
    last_update_time = 0
    make_stones()
    make_spikes()
    pgzrun.go()

def on_mouse_down(pos):
    global game_started, players, player
    if not game_started:
        for character in players:
            if character.collidepoint(pos):
                player = character
                game_started = True
                character.pos = PLAYER_X_START, PLAYER_Y_START
                player = character
                game_started = True
    else:
        if game_over or win:
            if yes_rect.collidepoint(pos):
                restart_game()
            elif no_rect.collidepoint(pos):
                pgzrun.sys.exit()

pgzrun.go()
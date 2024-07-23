import math
import pgzrun
import random
from pgzero import clock
from pgzero.animation import animate
from pgzero.actor import Actor

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
FONT_COLOR = (0, 0, 0)
EGG_TARGET = 20
HERO_START = (200, 300)
ATTACK_DISTANCE = 200
DRAGON_AWAKE_TIME = 2
EGG_HIDE_TIME = 2
MOVE_DISTANCE = 5

lives = 3
eggs_collected = 0
game_over = False
game_complete = False
reset_required = False

easy_lair = {
    "dragon": Actor("dragon-asleep", pos=(600, 60)),
    "eggs": Actor("one-egg", pos=(450, 100)),
    "egg_count": 1,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(7, 10),
    "sleep_counter": 0,
    "wake_counter": 0
}

medium_lair = {
    "dragon": Actor("dragon-asleep", pos=(600, 260)),
    "eggs": Actor("two-eggs", pos=(450, 300)),
    "egg_count": 2,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(4, 7),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair = {
    "dragon": Actor("dragon-asleep", pos=(600, 460)),
    "eggs": Actor("three-eggs", pos=(450, 500)),
    "egg_count": 3,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 4),
    "sleep_counter": 0,
    "wake_counter": 0
}

lairs = [easy_lair, medium_lair, hard_lair]
hero = Actor("hero", pos= HERO_START)

def draw():
    global lairs, eggs_collected, lives, game_complete
    screen.blit("dungeon", (0, 0))
    if game_over:
        screen.draw.text("GAME OVER", fontsize= 60, center= CENTER, color= FONT_COLOR)
    elif game_complete:
        screen.draw.text("YOU WON", fontsize= 60, center= CENTER, color= FONT_COLOR)
    else:
        hero.draw()
        draw_lairs(lairs)
        draw_counters(eggs_collected, lives)

def draw_lairs(lairs_to_draw):
    for lair in lairs_to_draw:
        lair["dragon"].draw()
        if lair["egg_hidden"] is False:
            lair["eggs"].draw()

def draw_counters(eggs_collected, lives):
    screen.blit("egg-count", (0, HEIGHT - 50))
    screen.draw.text(str(eggs_collected), fontsize = 40, pos=(30, HEIGHT - 50), color= FONT_COLOR)
    screen.blit("life-count", (60, HEIGHT -50))
    screen.draw.text(str(lives), fontsize = 40, pos=(90, HEIGHT - 50), color= FONT_COLOR)

def update():
    if keyboard.right:
        hero.x += MOVE_DISTANCE
        if hero.x > WIDTH:
            hero.x = WIDTH
    elif keyboard.left:
        hero.x -= MOVE_DISTANCE
        if hero.x < 0:
            hero.x = 0
    elif keyboard.down:
        hero.y += MOVE_DISTANCE
        if hero.y > HEIGHT:
            hero.y = HEIGHT
    elif keyboard.up:
        hero.y -= MOVE_DISTANCE
        if hero.y < 0:
            hero.y = 0
    check_for_collisions()

def check_for_collisions():
    global lairs, eggs_collected, lives, reset_required, game_complete
    for lair in lairs:
        if lair["egg_hidden"] is False:
            check_for_egg_collision(lair)
        if lair["dragon"].image == "dragon-awake" and reset_required is False:
            check_for_dragon_collision(lair)

def check_for_dragon_collision(lair):
    x_distance = hero.x - lair["dragon"].x
    y_distance = hero.y - lair["dragon"].y
    distance = math.hypot(x_distance, y_distance)
    if distance < ATTACK_DISTANCE:
        handle_dragon_collision()

def handle_dragon_collision():
    global reset_required
    reset_required = True
    animate(hero, pos= HERO_START, on_finished=subtract_life, duration= 0.01)

def subtract_life():
    global lives, reset_required, game_over
    lives -= 1
    if lives == 0:
        game_over = True
    reset_required = False

def check_for_egg_collision(lair):
    global eggs_collected, game_complete
    if hero.colliderect(lair["eggs"]):
        lair["egg_hidden"] = True
        eggs_collected += lair["egg_count"]
        if eggs_collected >= EGG_TARGET:
            game_complete = True

def update_lairs():
    global lairs, hero, lives
    for lair in lairs:
        if lair["dragon"].image == "dragon-asleep":
            update_sleeping_dragon(lair)
        elif lair["dragon"].image == "dragon-awake":
            update_waking_dragon(lair)
        update_egg(lair)

def update_sleeping_dragon(lair):
    if lair["sleep_counter"] >= lair["sleep_length"]:
        lair["dragon"].image = "dragon-awake"
        lair["sleep_counter"] = 0
    else:
        lair["sleep_counter"] += 1

def update_waking_dragon(lair):
    if lair["wake_counter"] >= DRAGON_AWAKE_TIME:
        lair["dragon"].image = "dragon-asleep"
        lair["wake_counter"] = 0
    else:
        lair["wake_counter"] += 1

def update_egg(lair):
    if lair["egg_hidden"] is True:
        if lair["egg_hide_counter"] >= EGG_HIDE_TIME:
            lair["egg_hidden"] = False
            lair["egg_hide_counter"] = 0
        else:
            lair["egg_hide_counter"] += 1

clock.schedule_interval(update_lairs, 1)

pgzrun.go()
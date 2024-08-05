import math
import pgzrun
import random
from pgzero import clock
from pgzero.animation import animate
from pgzero.actor import Actor

WIDTH = 2400
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
FONT_COLOR = (0, 0, 0)
EGG_TARGET = 100
HERO_START = (200, 300)
ATTACK_DISTANCE = 200
DRAGON_AWAKE_TIME = 10
EGG_HIDE_TIME = 5
MOVE_DISTANCE = 5
FREEZE_TIME = 10

lives = 3
eggs_collected = 0
game_over = False
game_complete = False
reset_required = False

# first 6 dragon lairs
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

easy_lair_2 = {
    "dragon": Actor("dragon-asleep", pos=(600, 160)),
    "eggs": Actor("one-egg", pos=(450, 200)),
    "egg_count": 1,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(7, 10),
    "sleep_counter": 0,
    "wake_counter": 0
}

easy_lair_3 = {
    "dragon": Actor("dragon-asleep", pos=(600, 560)),
    "eggs": Actor("one-egg", pos=(450, 100)),
    "egg_count": 1,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(7, 10),
    "sleep_counter": 0,
    "wake_counter": 0
}

medium_lair_2 = {
    "dragon": Actor("dragon-asleep", pos=(600, 360)),
    "eggs": Actor("two-eggs", pos=(450, 400)),
    "egg_count": 2,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(4, 7),
    "sleep_counter": 0,
    "wake_counter": 0
}

# secound 6 dragon lairs 
hard_lair_2 = {
    "dragon": Actor("dragon-asleep", pos=(1000, 60)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 4),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_3 = {
    "dragon": Actor("dragon-asleep", pos=(1000, 160)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 4),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_4 = {
    "dragon": Actor("dragon-asleep", pos=(1000, 260)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 4),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_5 = {
    "dragon": Actor("dragon-asleep", pos=(1000, 360)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 4),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_6 = {
    "dragon": Actor("dragon-asleep", pos=(1000, 460)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 4),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_7 = {
    "dragon": Actor("dragon-asleep", pos=(1000, 560)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 4),
    "sleep_counter": 0,
    "wake_counter": 0
}

# third 6 dragon lairs
hard_lair_8 = {
    "dragon": Actor("dragon-asleep", pos=(1400, 60)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 2),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_9 = {
    "dragon": Actor("dragon-asleep", pos=(1400, 160)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 2),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_10 = {
    "dragon": Actor("dragon-asleep", pos=(1400, 260)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 2),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_11 = {
    "dragon": Actor("dragon-asleep", pos=(1400, 360)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 2),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_12 = {
    "dragon": Actor("dragon-asleep", pos=(1400, 460)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 2),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_13 = {
    "dragon": Actor("dragon-asleep", pos=(1400, 560)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 2),
    "sleep_counter": 0,
    "wake_counter": 0
}

# fourth 6 dragon lairs
hard_lair_14 = {
    "dragon": Actor("dragon-asleep", pos=(1700, 60)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 1),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_15 = {
    "dragon": Actor("dragon-asleep", pos=(1700, 160)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 1),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_16 = {
    "dragon": Actor("dragon-asleep", pos=(1700, 260)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 1),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_17 = {
    "dragon": Actor("dragon-asleep", pos=(1700, 360)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 1),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_18 = {
    "dragon": Actor("dragon-asleep", pos=(1700, 460)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 1),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_19 = {
    "dragon": Actor("dragon-asleep", pos=(1700, 560)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.randint(1, 1),
    "sleep_counter": 0,
    "wake_counter": 0
}

# last 6 dragon lairs
hard_lair_20 = {
    "dragon": Actor("dragon-asleep", pos=(2000, 60)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.choice([0.1, 0.2, 0.3, 0.4, 0.5]),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_21 = {
    "dragon": Actor("dragon-asleep", pos=(2000, 160)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.choice([0.1, 0.2, 0.3, 0.4, 0.5]),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_22 = {
    "dragon": Actor("dragon-asleep", pos=(2000, 260)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.choice([0.1, 0.2, 0.3, 0.4, 0.5]),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_23 = {
    "dragon": Actor("dragon-asleep", pos=(2000, 360)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.choice([0.1, 0.2, 0.3, 0.4, 0.5]),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_24 = {
    "dragon": Actor("dragon-asleep", pos=(2000, 460)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.choice([0.1, 0.2, 0.3, 0.4, 0.5]),
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair_25 = {
    "dragon": Actor("dragon-asleep", pos=(2000, 560)),
    "eggs": Actor("three-eggs", pos=(450, 700)),
    "egg_count": 0,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": random.choice([0.1, 0.2, 0.3, 0.4, 0.5]),
    "sleep_counter": 0,
    "wake_counter": 0
}

# list of dragon lairs
lairs = [easy_lair, medium_lair, hard_lair, medium_lair_2, easy_lair_2, easy_lair_3, hard_lair_2, hard_lair_3, hard_lair_4, hard_lair_5, hard_lair_6, 
        hard_lair_7, hard_lair_8, hard_lair_9, hard_lair_10, hard_lair_11, hard_lair_12, hard_lair_13, hard_lair_14, hard_lair_15, hard_lair_16,
        hard_lair_17, hard_lair_18, hard_lair_19, hard_lair_20, hard_lair_21, hard_lair_22, hard_lair_23, hard_lair_24, hard_lair_25]

hero = Actor("hero", pos= HERO_START)
golden_egg = Actor("golden-egg", pos= (WIDTH - 100, HEIGHT / 2))
golden_egg_collided = False
freeze = 0
freeze_stop = False

def draw():
    global lairs, eggs_collected, lives, game_complete, golden_egg_collided, freeze, freeze_stop
    screen.blit("dungeon", (0, 0))
    screen.blit("dungeon", (800, 0))
    screen.blit("dungeon", (1600, 0))
    if game_over:
        screen.draw.text("GAME OVER", fontsize= 60, center= CENTER, color= FONT_COLOR)
    elif game_complete:
        screen.draw.text("YOU WON", fontsize= 60, center= CENTER, color= FONT_COLOR)
    else:
        hero.draw()
        draw_lairs(lairs)
        draw_counters(eggs_collected, lives)
        if not golden_egg_collided:
            golden_egg.draw()
        if freeze > FREEZE_TIME:
            screen.draw.text(f"DRAGONS FROZEN for {FREEZE_TIME - freeze + 1}. GO!", fontsize= 60, center= (CENTER_X - 300, CENTER_Y), color= FONT_COLOR)
            screen.draw.text(f"DRAGONS FROZEN for {FREEZE_TIME - freeze + 1}. GO!", fontsize= 60, center= (CENTER_X + 300, CENTER_Y), color= FONT_COLOR)
        if freeze == 1 + FREEZE_TIME:
            freeze = 0

def draw_lairs(lairs_to_draw):
    for lair in lairs_to_draw:
        lair["dragon"].draw()
        if lair["egg_hidden"] is False:
            lair["eggs"].draw()

def draw_counters(eggs_collected, lives):
    screen.blit("egg-count", (0, HEIGHT - 50))
    screen.draw.text(str(eggs_collected) + " / " + str(EGG_TARGET), fontsize = 40, pos=(30, HEIGHT - 50), color= FONT_COLOR)
    screen.blit("life-count", (125, HEIGHT -50))
    screen.draw.text(str(lives), fontsize = 40, pos=(155, HEIGHT - 50), color= FONT_COLOR)

def update():
    global lives
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
    if keyboard.a:
        lives += 1
    elif keyboard.d:
        lives -= 1
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
    global eggs_collected, game_complete, golden_egg_collided
    if hero.colliderect(lair["eggs"]):
        lair["egg_hidden"] = True
        eggs_collected += lair["egg_count"]
        if eggs_collected >= EGG_TARGET:
            game_complete = True
    if hero.colliderect(golden_egg):
        golden_egg_collided = True
        eggs_collected += 100
        if eggs_collected >= EGG_TARGET:
            game_complete = True

def update_lairs():
    global lairs, hero, lives, freeze, freeze_stop
    for lair in lairs:
        if lair["dragon"].image == "dragon-asleep":
            update_sleeping_dragon(lair)
        elif lair["dragon"].image == "dragon-awake":
            update_waking_dragon(lair)
        update_egg(lair)
    if not freeze_stop:
        freeze += 1

def update_sleeping_dragon(lair):
    if freeze < FREEZE_TIME:
        if lair["sleep_counter"] >= lair["sleep_length"]:
            lair["dragon"].image = "dragon-awake"
            lair["sleep_counter"] = 0
        else:
            lair["sleep_counter"] += 1
    else:
        lair["dragon"].image = "dragon-asleep"

def update_waking_dragon(lair):
    if freeze < FREEZE_TIME:
        if lair["wake_counter"] >= DRAGON_AWAKE_TIME:
            lair["dragon"].image = "dragon-asleep"
            lair["wake_counter"] = 0
        else:
            lair["wake_counter"] += 1
    else:
        lair["dragon"].image = "dragon-asleep"

def update_egg(lair):
    if lair["egg_hidden"] is True:
        if lair["egg_hide_counter"] >= EGG_HIDE_TIME:
            lair["egg_hidden"] = False
            lair["egg_hide_counter"] = 0
        else:
            lair["egg_hide_counter"] += 1

clock.schedule_interval(update_lairs, 1)

pgzrun.go()
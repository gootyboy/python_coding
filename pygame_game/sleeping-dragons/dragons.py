import math
import pgzrun
import random
from pgzero import clock
from pgzero.animation import animate
from pgzero.actor import Actor
from pgzero.keyboard import keyboard

WIDTH = 900
HEIGHT = 600

EGG_TARGET = 1000
ATTACK_DISTANCE = 200
GOLDEN_EGG_HIDE_TIME = 60
FREEZE_TIME = 10
DRAGON_AWAKE_TIME = 10
HERO_SPEED = 5
EGG_HIDE_TIME = 5

CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

CENTER = (CENTER_X, CENTER_Y)
FONT_COLOR = (0, 0, 0)
HERO_START = (200, 300)

eggs_collected = 0
golden_egg_hide_timer = 0
freeze = 0
lives = 3

game_over = False
game_complete = False
reset_required = False
golden_egg_collided = False
golden_egg_hidden = False
freeze_stop = False
secret_pass= False
up_mouse_counter = 0
down_mouse_counter = 0
press_mouse_counter = 0

hero = Actor("hero", pos= HERO_START)
golden_egg = Actor("golden-egg", pos= (WIDTH - 100, HEIGHT / 2))

def create_lair(difficulty, dragon_pos, eggs_pos, egg_count, sleep_range):
    if difficulty == "hard-2":
        amount_of_eggs = 0
        egg_hidden = True
        sleep_length = random.choice([0.1, 0.2, 0.3, 0.4, 0.5])
    else:
        amount_of_eggs = egg_count
        egg_hidden = False
        sleep_length = random.randint(sleep_range[0], sleep_range[1])
    return {
            "dragon": Actor("dragon-asleep", pos=dragon_pos),
            "eggs": Actor(f"{egg_count}-eggs", pos=eggs_pos),
            "egg_count": amount_of_eggs,
            "egg_hidden": egg_hidden,
            "egg_hide_counter": 0,
            "sleep_length": sleep_length,
            "sleep_counter": 0,
            "wake_counter": 0
        }

lairs = [
    create_lair("easy", (600, 60), (450, 100), 1, (7, 10)), create_lair("medium", (600, 260), (450, 300), 2, (4, 7)), 
    create_lair("hard", (600, 460), (450, 460), 3, (1, 4)), create_lair("medium", (600, 360), (450, 400), 2, (4, 7)), 
    create_lair("easy", (600, 160), (450, 200), 1, (7, 10)), create_lair("easy", (600, 560), (450, 100), 1, (7, 10)), 
    create_lair("hard", (1000, 60), (450, 700), 3, (1, 4)), create_lair("hard", (1000, 160), (450, 700), 3, (1, 4)),
    create_lair("hard", (1000, 260), (450, 700), 3, (1, 4)), create_lair("hard", (1000, 360), (450, 700), 3, (1, 4)),
    create_lair("hard", (1000, 460), (450, 700), 3, (1, 4)), create_lair("hard", (1000, 560), (450, 700), 3, (1, 4)), 
    create_lair("hard", (1400, 60), (450, 700), 3, (1, 2)), create_lair("hard", (1400, 160), (450, 700), 3, (1, 2)), 
    create_lair("hard", (1400, 260), (450, 700), 3, (1, 2)), create_lair("hard", (1400, 360), (450, 700), 3, (1, 2)),
    create_lair("hard", (1400, 460), (450, 700), 3, (1, 2)), create_lair("hard", (1400, 560), (450, 700), 3, (1, 2)),
]

lairs_2 = [create_lair("hard", (300, 60), (450, 700), 3, (1, 2)), create_lair("hard", (300, 160), (450, 700), 3, (1, 2)),
    create_lair("hard", (300, 260), (450, 700), 3, (1, 2)), create_lair("hard", (300, 360), (450, 700), 3, (1, 2)),
    create_lair("hard", (300, 460), (450, 700), 3, (1, 2)), create_lair("hard", (300, 560), (450, 700), 3, (1, 2)),
    create_lair("hard-2", (600, 60), (450, 700), 3, (1, 2)), create_lair("hard-2", (600, 160), (450, 700), 3, (1, 2)),
    create_lair("hard-2", (600, 260), (450, 700), 3, (1, 2)), create_lair("hard-2", (600, 360), (450, 700), 3, (1, 2)),
    create_lair("hard-2", (600, 460), (450, 700), 3, (1, 2)), create_lair("hard-2", (600, 560), (450, 700), 3, (1, 2))]

def draw():
    global lairs, eggs_collected, lives, game_complete, golden_egg_collided, freeze, freeze_stop, golden_egg_hide_timer, golden_egg_hidden
    draw_background()
    if game_over:
        screen.draw.text("GAME OVER", fontsize=60, center=(CENTER_X - 400, CENTER_Y), color=FONT_COLOR)
        screen.draw.text("GAME OVER", fontsize=60, center=(CENTER_X + 400, CENTER_Y), color=FONT_COLOR)
    elif game_complete:
        screen.draw.text("YOU WON", fontsize=60, center=(CENTER_X - 400, CENTER_Y), color=FONT_COLOR)
        screen.draw.text("YOU WON", fontsize=60, center=(CENTER_X + 400, CENTER_Y), color=FONT_COLOR)
    else:
        hero.draw()
        draw_lairs(lairs)
        draw_counters(eggs_collected, lives)
        if not golden_egg_hidden:
            golden_egg.draw()
        handle_freeze()
        handle_golden_egg()

def draw_background():
    screen.blit("dungeon", (0, 0))
    screen.blit("dungeon", (800, 0))
    screen.blit("dungeon", (1600, 0))
    if secret_pass:
        screen.blit("dungeon", (0, 600))
        screen.blit("dungeon", (800, 600))
        screen.blit("dungeon", (1600, 600))

def handle_freeze():
    global freeze
    if freeze > FREEZE_TIME:
        screen.draw.text(f"DRAGONS FROZEN for {FREEZE_TIME - freeze + 12}. GO!", fontsize=60, center=(CENTER_X - 400, CENTER_Y), color=FONT_COLOR)
        screen.draw.text(f"DRGONS FROZEN for {FREEZE_TIME - freeze + 12}. GO!", fontsize=60, center=(CENTER_X + 400, CENTER_Y), color=FONT_COLOR)
    if freeze == FREEZE_TIME * 2 + 1:
        freeze = 0

def handle_golden_egg():
    global golden_egg_hide_timer, golden_egg_hidden

    if not golden_egg_hidden:
        if golden_egg_hide_timer < GOLDEN_EGG_HIDE_TIME:
            screen.draw.text(f"Golden Egg will hide in {GOLDEN_EGG_HIDE_TIME - golden_egg_hide_timer} seconds. GO!", fontsize=60, topleft=(10, 10), color=FONT_COLOR)
        else:
            golden_egg_hidden = True
            golden_egg_hide_timer = 0
    else:
        if golden_egg_hide_timer < GOLDEN_EGG_HIDE_TIME:
            screen.draw.text(f"Golden Egg will appear in {GOLDEN_EGG_HIDE_TIME - golden_egg_hide_timer} seconds. GO!", fontsize=60, topleft=(10, 10), color=FONT_COLOR)
        else:
            golden_egg_hidden = False
            golden_egg_hide_timer = 0

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

def check_for_collisions():
    global lairs, eggs_collected, lives, reset_required, game_complete
    for lair in lairs:
        if lair["egg_hidden"] is False:
            check_for_egg_collision(lair)
        if lair["dragon"].image == "dragon-awake" and reset_required is False:
            check_for_dragon_collision(lair)
        if not golden_egg_hidden:
            check_for_golden_egg_collision()

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
    global eggs_collected, game_complete, lives
    if hero.colliderect(lair["eggs"]):
        lair["egg_hidden"] = True
        eggs_collected += lair["egg_count"]
        if eggs_collected >= EGG_TARGET:
            game_complete = True

def check_for_golden_egg_collision():
    global golden_egg_collided, game_complete, golden_egg_hidden, eggs_collected, lives
    if hero.colliderect(golden_egg):
        golden_egg_collided = True
        animate(hero, pos= HERO_START, duration= 0.01)
        golden_egg_hidden = True
        eggs_collected += 100
        if eggs_collected >= EGG_TARGET:
            game_complete = True

def update_lairs():
    global lairs, hero, lives, freeze, freeze_stop, golden_egg_hidden, golden_egg_hide_timer
    for lair in lairs:
        if lair["dragon"].image == "dragon-asleep":
            update_sleeping_dragon(lair)
        elif lair["dragon"].image == "dragon-awake":
            update_waking_dragon(lair)
        update_egg(lair)
    if not freeze_stop:
        freeze += 1

def update_golden_egg_timer():
    global golden_egg_hide_timer
    golden_egg_hide_timer += 1

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

def update():
    global lives
    if keyboard.right:
        hero.x += HERO_SPEED
        if hero.x > WIDTH:
            hero.x = WIDTH
    elif keyboard.left:
        hero.x -= HERO_SPEED
        if hero.x < 0:
            hero.x = 0
    elif keyboard.down:
        hero.y += HERO_SPEED
        if hero.y > HEIGHT:
            hero.y = HEIGHT
    elif keyboard.up:
        hero.y -= HERO_SPEED
        if hero.y < 0:
            hero.y = 0
    if keyboard.a:
        lives += 1
    elif keyboard.d:
        lives -= 1
    check_for_collisions()
    if hero.x > 1500:
        hero.x = 0
        move_screen()

def on_mouse_down(pos, button):
    global HEIGHT, secret_pass, up_mouse_counter, down_mouse_counter, press_mouse_counter
    if not secret_pass:
        if up_mouse_counter == 20 and down_mouse_counter == 20 and press_mouse_counter == 20:
            if hero.collidepoint(pos):
                HEIGHT = 1000
                secret_pass = True
            up_mouse_counter = 0
            down_mouse_counter = 0
            press_mouse_counter = 0
    else:
        if hero.collidepoint(pos):
            if up_mouse_counter == 20 and down_mouse_counter == 20 and press_mouse_counter == 20:
                HEIGHT = 1000
                secret_pass = True
            up_mouse_counter = 0
            down_mouse_counter = 0
            press_mouse_counter = 0
    if button == 3:
        if press_mouse_counter <= 20:
            press_mouse_counter += 1
    elif button == 4:
        if up_mouse_counter <= 20:
            up_mouse_counter += 1
    elif button == 5:
        if down_mouse_counter <= 20:
            down_mouse_counter += 1

def move_screen():
    global lairs, lairs_2
    lairs = lairs_2

clock.schedule_interval(update_lairs, 1)
clock.schedule_interval(update_golden_egg_timer, 1)

pgzrun.go()
import time
import pgzrun
from pgzero.actor import Actor
from random import randint
from pgzero import clock

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
TIME_TO_WATER = 5

game_over = False
finalized = False
garden_happy = True
fangflower_collision = False
raining = False
water_time = 0
time_to_rain = randint(1, 10)
not_raining_time = 0

time_elapsed = 0
start_time = time.time()

flower_list = []
wilted_list = []
fangflower_list = []
fangflower_vy_list = []
fangflower_vx_list = []

cow = Actor("cow", pos=(100, 500))

def draw():
    global game_over, time_elapsed, finalized, raining
    if not game_over:
        if not raining:
            screen.blit("garden", (0, 0))
        else:
            screen.blit("garden-raining", (0, 0))
        cow.draw()
        for flower in flower_list:
            flower.draw()
        for fangflower in fangflower_list:
            fangflower.draw()
        time_elapsed = round(float(time.time() - start_time), 1)
        screen.draw.text("Garden happy for " + str(time_elapsed) + " seconds", topleft= (10, 10), color= "black")
    else:
        if not finalized:
            screen.blit("garden", (0, 0))
            screen.blit("garden", (0, 0))
            cow.draw()
            screen.draw.text("Garden happy for " + str(time_elapsed) + " seconds", topleft= (10, 10), color= "black")
            if not garden_happy:
                screen.draw.text("GARDEN UNHAPPY- GAME OVER", topleft= (10, 50), color= "black")
                finalized = True
            else:
                screen.draw.text("FANGFLOWER ATTACK- GAME OVER", topleft= (10, 50), color= "black")
                finalized = True

def update_raining_time():
    global time_to_rain, raining, not_raining_time
    if not_raining_time < time_to_rain:
        not_raining_time += 1
    else:
        raining = True

def new_flower():
    global flower_list, wilted_list
    flower_new = Actor("flower", (randint(50, WIDTH - 50), randint(150, HEIGHT - 100)))
    flower_list.append(flower_new)
    wilted_list.append("happy")

def add_flower():
    global game_over
    if not game_over:
        new_flower()
        clock.schedule(add_flower, 10)

def check_wilt_times():
    global wilted_list, game_over, garden_happy
    if wilted_list:
        for wilted_since in wilted_list:
            if not wilted_since == "happy":
                time_wilted = round(float(time.time() - wilted_since), 1)
                if time_wilted > 10.0:
                    garden_happy = False
                    game_over = True
                    break

def wilt_flower():
    global flower_list, wilted_list
    if not game_over:
        if flower_list:
            rand_flower = randint(0, len(flower_list) - 1)
            if flower_list[rand_flower].image == "flower":
                flower_list[rand_flower].image = "flower-wilt"
                wilted_list[rand_flower] = time.time()
        clock.schedule(wilt_flower, 10)

def update_water_time():
    global game_over, water_time
    if not game_over:
        water_time += 1

def check_flower_collision():
    global cow, flower_list, wilted_list, water_time, raining
    index = 0
    water_time = 0
    for flower in flower_list:
        if (flower.colliderect(cow) and flower.image == "flower-wilt") or (raining and flower.image == "flower-wilt"): 
            if water_time < TIME_TO_WATER:
                clock.schedule_interval(update_water_time, 1)
            else:
                flower.image = "flower"
                wilted_list[index] = "happy" 
            break
        index += 1

def check_fangflower_collision():
    global cow, fangflower_list, fangflower_collision, game_over
    for fangflower in fangflower_list:
        if fangflower.colliderect(cow):
            cow.image = "zap"
            game_over = True
            break

def velocity():
    random_dir = randint(0, 1)
    random_velocity = randint(1, 2)
    if random_dir == 0:
        return -random_velocity
    else:
        return random_velocity

def mutate():
    global flower_list, fangflower_list, fangflower_vx_list, fangflower_vy_list, game_over
    if not game_over and flower_list:
        rand_flower = randint(0, len(flower_list) - 1)
        fangflower_pos_x = flower_list[rand_flower].x
        fangflower_pos_y = flower_list[rand_flower].y
        del flower_list[rand_flower]
        fangflower = Actor("fangflower", pos=(fangflower_pos_x, fangflower_pos_y))
        fangflower_vx = velocity()
        fangflower_vy = velocity()
        fangflower = fangflower_list.append(fangflower)
        fangflower_vx_list.append(fangflower_vx)
        fangflower_vy_list.append(fangflower_vy)

def schedule_mutate():
    global raining
    if not raining:
        clock.schedule_interval(mutate, 20)
    else:
        clock.schedule_interval(mutate, 10)

def update_fangflowers():
    global fangflower_list, game_over
    if not game_over:
        index = 0
        for fangflower in fangflower_list:
            fangflower_vx = fangflower_vx_list[index]
            fangflower_vy = fangflower_vy_list[index]
            fangflower.pos = fangflower.x + fangflower_vx, fangflower.y + fangflower_vy
            if fangflower.left < 0:
                fangflower_vx_list[index] = -fangflower_vx
            if fangflower.right > WIDTH:
                fangflower_vx_list[index] = -fangflower_vx
            if fangflower.left < 0:
                fangflower_vy_list[index] = -fangflower_vy
            if fangflower.right > WIDTH:
                fangflower_vy_list[index] = -fangflower_vy
            index += 1

def reset_cow():
    global game_over
    if not game_over:
        cow.image = "cow"

def update():
    global score, game_over, fangflower_collision, flower_list, fangflower_list, time_elapsed
    fangflower_collision = check_fangflower_collision()
    check_wilt_times()
    if not game_over:
        if keyboard.SPACE:
            cow.image = "cow-water"
            clock.schedule(reset_cow, 0.5)
            check_flower_collision()                                                 
        if keyboard.left and cow.x > 0:
            cow.x -= 5
        elif keyboard.right and cow.x < WIDTH:
            cow.x += 5
        elif keyboard.up and cow.y > 143:
            cow.y -= 5
        elif keyboard.down and cow.y < HEIGHT:
            cow.y += 5
        update_fangflowers()

add_flower()
wilt_flower()
clock.schedule_interval(update_raining_time, 1)

pgzrun.go()
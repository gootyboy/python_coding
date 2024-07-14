import pgzrun
import pygame
from pgzero.actor import Actor
from random import randint

WIDTH = 700
HEIGHT = 600
fox_score = 0
hedgehog_score = 0
game_over = False
player_speed = 10
scores = []
high_score_run = True
time_left = 60 # this is the amount of time (in seconds). Feel Free to change it how like
multiplayer = False
start_game = False

one_player_box = pygame.Rect(0, 0, 54, 54)
one_player_box.move_ip(240, 330)
two_player_box = pygame.Rect(0, 0, 54, 54)
two_player_box.move_ip(350, 330)
play_agian_no_box = pygame.Rect(0, 0, 54, 54)
play_agian_no_box.move_ip(200, 500)
play_agian_yes_box = pygame.Rect(0, 0, 54, 54)
play_agian_yes_box.move_ip(300, 500)

fox = Actor("fox")
fox.pos = 100, 100
hedgehog = Actor("hedgehog")
hedgehog.pos = 400, 400
coin = Actor("coin")
coin.pos = 200, 200

def on_mouse_down(pos):
    global start_game, multiplayer, game_over, time_left, high_score_run

    if start_game == False:
        if one_player_box.collidepoint(pos):
            start_game = True
            multiplayer = False
        if two_player_box.collidepoint(pos):
            start_game = True
            multiplayer = True
    if game_over == True:
        if play_agian_no_box.collidepoint(pos):
            pygame.quit()
        if play_agian_yes_box.collidepoint(pos):
            game_over = False
            high_score_run = True
            time_left = 5
            multiplayer = False
            start_game = False
            
def draw():
    global game_over, high_score_run, yes_circle_x, yes_circle_y, multiplayer, start_game

    if not game_over:
        screen.fill("green")
        screen.draw.text("Select the amount of players", color= "black", center = (WIDTH / 2, HEIGHT / 2), fontsize = 35)
        screen.draw.filled_rect(one_player_box, "sky blue")
        screen.draw.textbox("1", one_player_box, color= "black")
        screen.draw.filled_rect(two_player_box, "sky blue")
        screen.draw.textbox("2", two_player_box, color= "black")

    if not game_over and start_game == True:
        screen.fill("green")
        fox.draw()
        coin.draw()
        if multiplayer == True:
            hedgehog.draw()
        screen.draw.text("Fox score: " + str(fox_score), color="black", topleft =(10, 10))
        if multiplayer == True:
            screen.draw.text("Hedgehog score: " + str(hedgehog_score), color="black", topleft =(10, 30))
        screen.draw.text(str(time_left), color=("Black"), topright =(700, 0), fontsize= 50)

    if game_over:
        screen.fill("green")
        screen.draw.text("Fox Score: " + str(fox_score), color= "black", topleft = (10, 10), fontsize = 30)
        screen.draw.text("Hedgehog Score: " + str(hedgehog_score), color= "black", topleft = (10, 30), fontsize = 30)
        if high_score_run == True:
            update_high_scores()
        high_score_run = False
        display_high_scores()
        screen.draw.filled_rect(play_agian_no_box, "purple")
        screen.draw.textbox("No", play_agian_no_box, color="black")
        screen.draw.filled_rect(play_agian_yes_box, "purple")
        screen.draw.textbox("Yes", play_agian_yes_box, color="black")
        screen.draw.text("Do you want", color="black", center = (250, 400), fontsize = 50)
        screen.draw.text("to play again?", color="black", center = (250, 450), fontsize = 50)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update_time_left():
    global time_left, start_game

    if start_game == True:
        if time_left:
            time_left -= 1
        else:
            time_up()

def update_high_scores():
    global fox_score, hedgehog_score, fox_scores, hedgehog_scores, high_scores, multiplayer

    filename = r"C:\\Users\\igres\\Desktop\boy\\pygame_game\\coin_collector\\fox_high_scores.txt"
    fox_scores = []
    with open(filename, "r") as file:
        line = file.readline()
        fox_scores = line.split()
        fox_scores.insert(0, fox_score)    
    with open(filename, "w") as file:
        for high_score in fox_scores:
            file.write(str(high_score) + " ")
    fox_score = 0

    if multiplayer == True:
        filename = r"C:\\Users\\igres\\Desktop\boy\\pygame_game\\coin_collector\\hedgehog_high_scores.txt"
        hedgehog_scores = []
        with open(filename, "r") as file:
            line = file.readline()
            hedgehog_scores = line.split()
            hedgehog_scores.append(str(hedgehog_score) + " ")
        with open(filename, "w") as file:
            for high_score in hedgehog_scores:
                file.write(str(high_score) + " ")
    hedgehog_score = 0

def display_high_scores():
    if multiplayer == True:
        all_high_scores = fox_scores+hedgehog_scores
    else:
        all_high_scores = fox_scores
    all_high_scores = list(map(int, all_high_scores))
    all_high_scores.sort(reverse=True)
    screen.draw.text("High Scores", (600, 25), color="black")
    y = 50
    position = 1
    for high_score in all_high_scores:
        screen.draw.text(str(position) + ". " + str(high_score), (600, y), color="black")
        y += 25
        position += 1

def update():
    global hedgehog_score, fox_score

    if fox.x > 20:
        if keyboard.left:
            fox.x -= player_speed
    if fox.x < (WIDTH -20):
        if keyboard.right:
            fox.x += player_speed
    if fox.y > 20:
        if keyboard.up:
            fox.y -= player_speed
    if fox.y < (HEIGHT -20):
        if keyboard.down:
            fox.y += player_speed

    if hedgehog.x > 20:
        if keyboard.a:
            hedgehog.x -= player_speed
    if hedgehog.x < (WIDTH -20):
        if keyboard.d:
            hedgehog.x += player_speed
    if hedgehog.y > 20:
        if keyboard.w:
            hedgehog.y -= player_speed
    if hedgehog.y < (HEIGHT -20):
        if keyboard.s:
            hedgehog.y += player_speed


    fox_coin_collected = fox.colliderect(coin)
    hedgehog_coin_collected = hedgehog.colliderect(coin)

    if fox_coin_collected:
        fox_score += 10
        place_coin()
    
    if hedgehog_coin_collected:
        hedgehog_score += 10
        place_coin()

clock.schedule_interval(update_time_left, 1.0)
place_coin()

pgzrun.go()
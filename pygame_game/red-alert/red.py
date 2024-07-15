import random
import pgzrun
import pygame
from pgzero.actor import Actor

FONT_COLOR = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
FINAL_LEVEL = 10
START_SPEED = 5
PLAY_AGIAN_NO_X = 350
PLAY_AGIAN_YES_X = 250
NUMBER_STARS_ON_ROW = 5
COLORS = ["green", "blue"]

game_over = False
game_complete = False
current_level = 1
stars = []
animations = []

play_agian_yes_box = pygame.Rect(0, 0, 54, 54)
play_agian_yes_box.move_ip(PLAY_AGIAN_NO_X, CENTER_Y + 130)
play_agian_no_box = pygame.Rect(0, 0, 54, 54)
play_agian_no_box.move_ip(PLAY_AGIAN_YES_X, CENTER_Y + 130)

def draw():
    global stars, current_level, game_over, game_complete

    screen.clear()
    screen.blit("space", (0, 0))
    draw_level_number()
    if game_over:
        display_message("GAME OVER", "Try agian.")
        play_agian_q()
    elif game_complete:
        display_message("YOU WON", "Well done.")
        play_agian_q()
    else:
        for star in stars:
            star.draw()

def update():
    global stars

    if len(stars) == 0:
        stars = make_stars(current_level)

def make_stars(number_of_extra_stars):
    colors_to_create = get_colors_to_create(number_of_extra_stars)
    new_stars = create_stars(colors_to_create)
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars

def get_colors_to_create(number_of_extra_stars):
    colors_to_create = ["red"]
    for i in range(0, number_of_extra_stars):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create

def create_stars(color_to_create):
    new_stars = []
    for color in color_to_create:
        star = Actor(color + "-star")
        new_stars.append(star)
    return new_stars

def split_array_to_subarrays(list_to_split, stars_on_each_row):
    subarrays = []
    while len(list_to_split) >= stars_on_each_row:
        subarray = list_to_split[:stars_on_each_row]
        subarrays.append(subarray)
        list_to_split = list_to_split[stars_on_each_row:]
    if list_to_split:
        subarrays.append(list_to_split)

    return subarrays

def layout_stars(stars_to_layout):
    if len(stars_to_layout) > NUMBER_STARS_ON_ROW:
        star_placment_array = split_array_to_subarrays(stars_to_layout, NUMBER_STARS_ON_ROW)
        first_row_stars_to_layout = star_placment_array[0]
        secound_row_stars_to_layout = star_placment_array[1]
        one_row = True
    else:
        first_row_stars_to_layout = stars_to_layout
        one_row = False
    first_row_number_of_gaps = len(first_row_stars_to_layout) + 1
    first_row_gap_size = WIDTH / first_row_number_of_gaps
    random.shuffle(first_row_stars_to_layout)
    for index, star in enumerate(first_row_stars_to_layout):
        first_new_x_pos = (index + 1) * first_row_gap_size
        star.x = first_new_x_pos
    if one_row == True:
        two_row_number_of_gaps = len(secound_row_stars_to_layout)
        two_row_gap_size = WIDTH / two_row_number_of_gaps
        for two_row_index, two_row_stars in enumerate(secound_row_stars_to_layout):
            new_y_pos = 200
            secound_new_x_pos = (two_row_index + 1) * two_row_gap_size
            two_row_stars.x = secound_new_x_pos
            two_row_stars.y = new_y_pos

def animate_stars(stars_to_animate):
    for star in stars_to_animate:
        duration = START_SPEED - current_level / 2
        if duration < 1:
            duration = START_SPEED - current_level / 5
        star.anchor = ("center", "bottom")
        animation = animate(star, duration=duration, on_finished=handle_game_over, y = HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global stars, current_level, game_over, game_complete, animations

    if game_complete == False or game_over == False:
        for star in stars:
            if star.collidepoint(pos):
                if "red" in star.image:
                    red_star_click()
                else:
                    handle_game_over()
    if game_over == True or game_complete == True:
        if play_agian_yes_box.collidepoint(pos):
            game_complete = False
            game_over = False
            current_level = 1
            stars = []
            animations = []
        elif play_agian_no_box.collidepoint(pos):
            pygame.quit()

def red_star_click():
    global current_level, stars, animations, game_complete

    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level += 1
        stars = []
        animations = []

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize = 70, center = (CENTER_X, CENTER_Y - 100), color= FONT_COLOR)
    screen.draw.text(sub_heading_text, fontsize = 40, center = (CENTER_X, CENTER_Y -70), color= FONT_COLOR)

def draw_level_number():
    global current_level

    screen.draw.text(f"level {str(current_level)}", color= FONT_COLOR, topleft = (30, 30), fontsize = 45)

def play_agian_q():
    screen.draw.text("Do you want to play agian?", fontsize = 35, center = (((PLAY_AGIAN_NO_X + PLAY_AGIAN_YES_X) / 2), CENTER_Y + 100), color= FONT_COLOR)
    screen.draw.filled_rect(play_agian_no_box, FONT_COLOR)
    screen.draw.textbox("No", play_agian_no_box, color="black")
    screen.draw.filled_rect(play_agian_yes_box, FONT_COLOR)
    screen.draw.textbox("Yes", play_agian_yes_box, color="black")

pgzrun.go()
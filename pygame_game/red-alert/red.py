import random
import pgzrun
import pgzero

FONT_COLOR = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
FINAL_LEVEL = 6
COLORS = ["green", "blue"]

game_over = False
game_complete = False
current_level = 1
stars = []
animations = []

def draw():
    global stars, current_level, game_over, game_complete

    screen.clear()
    screen.blit("space", (0, 0))
    if game_over:
        screen.draw.text("GAME OVER", color= FONT_COLOR, center = (CENTER_X, (CENTER_Y - 20)), fontsize = 40)
        screen.draw.text("Try agian", color= FONT_COLOR, center = (CENTER_X, (CENTER_Y + 20)), fontsize = 40)
    elif game_complete:
        screen.draw.text("YOU WON", color= FONT_COLOR, center = (CENTER_X, (CENTER_Y - 20)), fontsize = 40)
        screen.draw.text("Well done", color= FONT_COLOR, center = (CENTER_X, (CENTER_Y + 20)), fontsize = 40)
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

def create_stars(color_to_create):
    return []

def layout_stars(stars_to_layout):
    pass

def animate_stars(stars_to_animate):
    pass

pgzrun.go()
# TODO: Move all imports to a different file. import that file
import pgzrun
import pygame
import pgzero
import math
import time
from pgzero.actor import Actor
from pgzero.animation import animate
from pgzero.clock import clock
from pgzero.builtins import mouse
from pgzero.rect import Rect
from pgzero.keyboard import keys

TITLE = "Gautam's mini movie"
WIDTH = 800
HEIGHT = 600

MOVIE_TIME = 20 # seconds
MOUSE_HOVER_TIME = 200 # milliseconds

bg_color = (255, 255, 255)
mouse_hover = False
paused = True
milliseconds_shown = 0
text_y_pos = 275
credits = ["Directed by Gautam Pulugurta","Produced by Gautam Pulugurta", "Screenplay by Gautam Pulugurta", "Music Director: Gautam Pulugurta", "Story by Gautam Pulugurta and Anvika Sarpatwar"]
forward_10 = Actor("forward_10", (WIDTH - 120, 280))
backward_10 = Actor("backward_10", (120, 280))
mouse_hover_timer = 0
the_end = False
the_end_timer = 0
the_end_fontsize = 100
thanks_for_watching = False


def draw_filled_triangle(color, point_1, point_2, point_3):
    pygame.draw.polygon(screen.surface, color, [point_1, point_2, point_3], 0)

def get_tens_and_ones(number):
    ones_digit = number % 10
    tens_digit = (number // 10) % 10
    return f"{tens_digit}{ones_digit}"

def draw():
    global bg_color, milliseconds_shown, text_y_pos, the_end, the_end_fontsize, the_end_timer, thanks_for_watching
    if milliseconds_shown <= MOVIE_TIME * 100:
        screen.fill(bg_color)
        if mouse_hover:
            if paused:
                draw_filled_triangle((200, 200, 200), (400, 250), (400, 325), (475, (250 + 325) / 2))
            else:
                screen.draw.filled_rect(Rect(400, 250, 10, 75), (200, 200, 200))
                screen.draw.filled_rect(Rect(450, 250, 10, 75), (200, 200, 200))
            screen.draw.text(f"{milliseconds_shown // 100}:{get_tens_and_ones(milliseconds_shown)}", bottomleft=(20, HEIGHT - 20), color=(0, 0, 0))

            remaining_time = (MOVIE_TIME * 100) - milliseconds_shown
            screen.draw.text(f"{remaining_time // 100}:{get_tens_and_ones(remaining_time)}", bottomleft=(WIDTH - 50, HEIGHT - 20), color=(0, 0, 0))
            forward_10.draw()
            backward_10.draw()
    else:
        if not thanks_for_watching:
            if not the_end:
                screen.fill((0, 0, 0))
                screen.draw.text("Credits", center=(WIDTH / 2, text_y_pos), color=(255, 255, 255), fontsize=100)
                for i in range(len(credits)):
                    screen.draw.text(credits[i], center=(WIDTH / 2, text_y_pos + 100 + 75 * i), color=(255, 255, 255), fontsize=35)
            else:
                screen.fill((0, 0, 0))
                if the_end_timer == 0:
                    screen.draw.text("The End", center=(WIDTH / 2, HEIGHT / 2), color=(255, 255, 255), fontsize=100)
                    clock.schedule(start_growing_the_end, 1.5)
                else:
                    screen.draw.text("The End", center=(WIDTH / 2, HEIGHT / 2), color=(255, 255, 255), fontsize=the_end_fontsize)
                    the_end_fontsize += 2
                    if the_end_fontsize >= 200:
                        thanks_for_watching = True
                        the_end_fontsize = 0
                        clock.schedule(show_thanks_for_watching, 2.0)
        else:
            screen.fill((0, 0, 0))
            screen.draw.text("Thanks for watching!", center=(WIDTH / 2, HEIGHT / 2), color=(255, 255, 255), fontsize=100)
            screen.draw.text("Part 2 expected to be released in 2027!", center=(WIDTH / 2, HEIGHT / 2 + 100), color=(255, 255, 255), fontsize=50)

def start_growing_the_end():
    global the_end_timer, the_end_fontsize
    the_end_timer += 1
    the_end_fontsize = 100

def show_thanks_for_watching():
    global thanks_for_watching
    thanks_for_watching = True
    clock.schedule(pgzrun.sys.exit(), 5.0)

def update():
    global text_y_pos, milliseconds_shown, credits, the_end
    if milliseconds_shown >= MOVIE_TIME * 100:
        if text_y_pos + 100 + 75 * (len(credits)-1) > 0:
            text_y_pos -= 1
        else:
            the_end = True

def on_key_down(key):
    global paused, mouse_hover, milliseconds_shown
    if key == keys.SPACE:
        paused = paused == False
    if key == keys.RIGHT:
        milliseconds_shown += 1000
        if paused:
            paused = False
    if key == keys.LEFT:
        new_milliseconds_shown = milliseconds_shown - 1000
        if new_milliseconds_shown >= 0:
            milliseconds_shown = new_milliseconds_shown
        else:
            milliseconds_shown = 0
        if paused:
            paused = False

def on_mouse_down(pos, button):
    global paused
    if Rect(380, 225, 100, 125).collidepoint(pos) and button == mouse.LEFT:
        paused = paused == False

def on_mouse_up(pos, button):
    global milliseconds_shown, paused
    if forward_10.collidepoint(pos) and button == mouse.LEFT:
        milliseconds_shown += 1000
        if paused:
            paused = False
    if backward_10.collidepoint(pos) and button == mouse.LEFT:
        new_milliseconds_shown = milliseconds_shown - 1000
        if new_milliseconds_shown >= 0:
            milliseconds_shown = new_milliseconds_shown
        else:
            milliseconds_shown = 0
        if paused:
            paused = False

def on_mouse_move(pos):
    global mouse_hover
    if 0 < pos[0] < WIDTH - 10 and 0 < pos[1] < HEIGHT - 10:
        mouse_hover = True
    else:
        mouse_hover = False

def update_milliseconds_shown():
    global milliseconds_shown
    if not paused:
        milliseconds_shown += 1

def update_mouse_hover():
    global mouse_hover, mouse_hover_timer
    org_mouse_pos = pygame.mouse.get_pos()
    if mouse_hover_timer >= MOUSE_HOVER_TIME:
        if org_mouse_pos == pygame.mouse.get_pos():
            mouse_hover = False
        else:
            org_mouse_pos = pygame.mouse.get_pos()
        mouse_hover_timer = 0
    else:
        mouse_hover_timer += 1

clock.schedule_interval(update_mouse_hover, 0.01)
clock.schedule_interval(update_milliseconds_shown, 0.01)

pgzrun.go()
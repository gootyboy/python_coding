import pgzrun
import pygame
from pgzero.actor import Actor
from pgzero.animation import animate
from pgzero.clock import clock
from pgzero.builtins import mouse
from pgzero.rect import Rect
from pgzero.keyboard import keys
from pgzero.spellcheck import spellcheck

TITLE = "Gautam's mini movie"
WIDTH = 800
HEIGHT = 600

bg_color = (255, 255, 255)
mouse_hover = False
paused = False

def filled_triangle(color, point_1, point_2, point_3):
    pygame.draw.polygon(screen.surface, color, [point_1, point_2, point_3], 0)

def draw():
    global bg_color
    screen.fill(bg_color)
    if mouse_hover:
        if paused:
            filled_triangle((200, 200, 200), (400, 250), (400, 325), (475, (250 + 325) / 2))
        else:
            screen.draw.filled_rect(Rect(400, 250, 10, 75), (200, 200, 200))
            screen.draw.filled_rect(Rect(450, 250, 10, 75), (200, 200, 200))

def update():
    pass

def on_key_down(key):
    global paused, mouse_hover
    if key == keys.SPACE:
        mouse_hover = True
        paused = paused == False

def on_mouse_down(pos, button):
    global paused
    if Rect(380, 225, 100, 125).collidepoint(pos) and button == mouse.LEFT:
        paused = paused == False

def on_mouse_move(pos):
    global mouse_hover
    if 0 < pos[0] < WIDTH - 10 and 0 < pos[1] < HEIGHT - 10:
        mouse_hover = True
    else:
        mouse_hover = False

pgzrun.go()
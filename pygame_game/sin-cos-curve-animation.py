import pgzrun
import math
from pgzero import clock
import pygame

WIDTH = 800
HEIGHT = 600
SPEED_OF_ANIMATION = 10

x = 50
draw_text = 0

sin_points = []
cos_points = []
sin_cos_points = []
sec_points = []
csc_points = []

def draw_graphs():
    global x, sin_points, cos_points, sec_points
    if x < WIDTH:
        sin_val = math.sin(math.radians(x))
        cos_val = math.cos(math.radians(x))
        sec_val = 1 / cos_val
        csc_val = 1 / sin_val

        sin_points.append((x, HEIGHT / 2 + sin_val * 100))
        cos_points.append((x, HEIGHT / 2 + cos_val * 100))
        if cos_val != 0:
            sec_y = HEIGHT / 2 + sec_val * 100
            if -HEIGHT < sec_y < HEIGHT * 2:
                sec_points.append((x, sec_y))

        if sin_val != 0:
            csc_y = HEIGHT / 2 + csc_val * 100
            if -HEIGHT < csc_y < HEIGHT * 2:
                csc_points.append((x, csc_y))

        sin_cos = sin_val ** 2 + cos_val ** 2
        sin_cos_points.append((x, HEIGHT / 2 + sin_cos * 100))
        sin_cos_points.append((x, HEIGHT / 2 - sin_cos * 100))
        x += 0.1

def draw():
    global x
    screen.fill("white")
    for point in sin_points:
        screen.draw.circle(point, 1, (0, 0, 255))
    for point in cos_points:
        screen.draw.circle(point, 1, (255, 0, 0))
    for point in sin_cos_points:
        screen.draw.circle(point, 1, (0, 255, 0))
    for point in sec_points:
        screen.draw.circle(point, 1, (255, 0, 255))
    for point in csc_points:
        screen.draw.circle(point, 1, (255, 165, 0))

    screen.draw.line((0, HEIGHT / 2), (WIDTH, HEIGHT / 2), (0, 0, 0))
    screen.draw.line((0, HEIGHT / 2 + 1), (WIDTH, HEIGHT / 2 + 1), (0, 0, 0))
    screen.draw.line((50, 0), (50, HEIGHT), (0, 0, 0))
    screen.draw.line((50, 1), (50, HEIGHT + 1), (0, 0, 0))
    for i in range(0, WIDTH, 50):
        screen.draw.text(str(i), color="black", bottomleft=(i + 50, HEIGHT / 2), fontsize=30)

    screen.draw.filled_rect(pygame.Rect(WIDTH - 100, 20, 30, 5), (0, 0, 255))
    screen.draw.filled_rect(pygame.Rect(WIDTH - 100, 40, 30, 5), (255, 0, 0))
    screen.draw.filled_rect(pygame.Rect(WIDTH - 100, 60, 30, 5), (255, 0, 255))
    screen.draw.filled_rect(pygame.Rect(WIDTH - 100, 80, 30, 5), (255, 165, 0))
    screen.draw.text("= sin", color="black", topleft = (WIDTH - 60, 10), fontsize=30)
    screen.draw.text("= cos", color="black", topleft = (WIDTH - 60, 30), fontsize=30)
    screen.draw.text("= sec", color="black", topleft = (WIDTH - 60, 50), fontsize=30)
    screen.draw.text("= csc", color="black", topleft = (WIDTH - 60, 70), fontsize=30)

def update_draw_text():
    global draw_text
    if draw_text < 11:
        draw_text += 1

for i in range(0, SPEED_OF_ANIMATION):
    clock.schedule_interval(draw_graphs, 0.01)

clock.schedule_interval(update_draw_text, 1)

pgzrun.go()
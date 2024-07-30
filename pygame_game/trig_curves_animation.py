import pgzrun
import math
from pgzero import clock
import pygame

WIDTH = 800
HEIGHT = 600
SPEED_OF_ANIMATION = 30
X_VALUE_STEP = 0.5
Y_VALUE_STEP = 0.5
MULTIPLING_FACTOR = 100

x = 0.1

animation_rect_open = False

sin_points = []
cos_points = []
sin_cos_points = []
sec_points = []
csc_points = []

sin_2_points = []

def append_x_y_cor_for_graphs():
    global x, sin_points, cos_points, sec_points, sin_2_points

    if x < WIDTH:
        sin_val = math.sin(math.radians(x))
        cos_val = math.cos(math.radians(x))
        sec_val = 1 / cos_val
        csc_val = 1 / sin_val

        sin_points.append((50 + x, HEIGHT / 2 - sin_val * MULTIPLING_FACTOR))
        sin_2_points.append((50 + x, HEIGHT / 2 - (sin_val ** 2) * MULTIPLING_FACTOR))
        cos_points.append((50 + x, HEIGHT / 2 + cos_val * MULTIPLING_FACTOR))

        if cos_val != 0:
            sec_y = HEIGHT / 2 + sec_val * MULTIPLING_FACTOR
            if -HEIGHT < sec_y < HEIGHT * 2:
                sec_points.append((50 + x, sec_y))

        if sin_val != 0:
            csc_y = HEIGHT / 2 + csc_val * MULTIPLING_FACTOR
            if -HEIGHT < csc_y < HEIGHT * 2:
                csc_points.append((50 + x, csc_y))

        sin_cos = sin_val ** 2 + cos_val ** 2
        sin_cos_points.append((50 + x, HEIGHT / 2 + sin_cos * MULTIPLING_FACTOR))
        sin_cos_points.append((50 + x, HEIGHT / 2 - sin_cos * MULTIPLING_FACTOR))
        x += 0.1

def draw_grid_and_values():
    # Horz X axis
    screen.draw.line((0, HEIGHT / 2), (WIDTH, HEIGHT / 2), (0, 0, 0))
    screen.draw.line((0, HEIGHT / 2 + 1), (WIDTH, HEIGHT / 2 + 1), (0, 0, 0))
    
    # Vertical y-axis line
    screen.draw.line((50, 0), (50, HEIGHT), (0, 0, 0))
    screen.draw.line((50, 1), (50, HEIGHT + 1), (0, 0, 0))
    screen.draw.line((50, -1), (50, HEIGHT - 1), (0, 0, 0))

    x_step_with_mf = int(X_VALUE_STEP * MULTIPLING_FACTOR)
    y_step_with_mf = int(Y_VALUE_STEP * MULTIPLING_FACTOR)
    for i in range(0, WIDTH + 1, x_step_with_mf):
        angles_in_degress = str(i)
        screen.draw.text(angles_in_degress, color="black", bottomleft=(i + 50, HEIGHT / 2), fontsize=20)
        screen.draw.line((i, HEIGHT), (i, 0), (150, 150, 150))
    for i in range(0, HEIGHT // 2 + 1, y_step_with_mf):
        if i != 0:
            screen.draw.text(str(-(i / MULTIPLING_FACTOR)), color="black", bottomright=(50, i + HEIGHT / 2), fontsize=30)
            screen.draw.text(str(i / MULTIPLING_FACTOR), color="black", bottomright=(50, HEIGHT / 2 - i), fontsize=30)
            screen.draw.line((WIDTH, HEIGHT - i), (0, HEIGHT - i), (150, 150, 150))
            screen.draw.line((WIDTH, i), (0, i), (150, 150, 150))

def draw_legend_and_options_rect():
    screen.draw.filled_rect(pygame.Rect(WIDTH - 120, 20, 30, 5), (0, 0, 255))
    screen.draw.filled_rect(pygame.Rect(WIDTH - 120, 40, 30, 5), (255, 0, 0))
    screen.draw.filled_rect(pygame.Rect(WIDTH - 120, 60, 30, 5), (255, 0, 255))
    screen.draw.filled_rect(pygame.Rect(WIDTH - 120, 80, 30, 5), (255, 165, 0))
    screen.draw.filled_rect(pygame.Rect(WIDTH - 120, 100, 30, 5), (0, 255, 255))
    screen.draw.text("Degrees", color="black", center = ((WIDTH - 50) / 2, HEIGHT / 2 + 10), fontsize=30)
    screen.draw.text("= sin", color="black", topleft = (WIDTH - 80, 10), fontsize=30)
    screen.draw.text("= cos", color="black", topleft = (WIDTH - 80, 30), fontsize=30)
    screen.draw.text("= sec", color="black", topleft = (WIDTH - 80, 50), fontsize=30)
    screen.draw.text("= csc", color="black", topleft = (WIDTH - 80, 70), fontsize=30)
    screen.draw.text("= sin ^ 2", color="black", topleft = (WIDTH - 80, 90), fontsize=30)

    resart_animation_1 = pygame.Rect(WIDTH / 2, 0, 75, 20)
    resart_animation_2 = pygame.Rect(WIDTH / 2 - 10, 20, 95, 20)
    screen.draw.filled_rect(resart_animation_1, (130, 130, 130))
    if not animation_rect_open:
        screen.draw.textbox("options", resart_animation_1, color=(255, 255, 255))
    else:
        screen.draw.filled_rect(resart_animation_2, (130, 130, 130))
        screen.draw.textbox("Restart", resart_animation_1, color=(255, 255, 255))
        screen.draw.textbox("animation", resart_animation_2, color=(255, 255, 255))

def draw():
    global x, resart_animation_1, resart_animation_2, animation_rect_open
    screen.fill("white")
    draw_grid_and_values()
    draw_legend_and_options_rect()
    for point in sin_points:
        screen.draw.circle(point, 1, (0, 0, 255))
    for point in sin_2_points:
        screen.draw.circle(point, 1, (0, 255, 255))
    for point in cos_points:
        screen.draw.circle(point, 1, (255, 0, 0))
    for point in sin_cos_points:
        screen.draw.circle(point, 1, (0, 255, 0))
    for point in sec_points:
        screen.draw.circle(point, 1, (255, 0, 255))
    for point in csc_points:
        screen.draw.circle(point, 1, (255, 165, 0))

def on_mouse_down(pos):
    global resart_animation_1, resart_animation_2, x, sin_points, cos_points, sin_cos_points, sec_points, csc_points, animation_rect_open, sin_2_points
    if resart_animation_1.collidepoint(pos) or resart_animation_2.collidepoint(pos):
        if animation_rect_open:
            x = 0.1
            sin_points = []
            cos_points = []
            sin_cos_points = []
            sec_points = []
            csc_points = []
            sin_2_points = []
            animation_rect_open = False
    if resart_animation_1.collidepoint(pos) and not animation_rect_open:
        animation_rect_open = True

for i in range(0, SPEED_OF_ANIMATION):
    clock.schedule_interval(append_x_y_cor_for_graphs, 0.01)

pgzrun.go()
import pgzrun
import math
from pgzero import clock
import pygame

WIDTH = 800
HEIGHT = 600
SPEED_OF_ANIMATION = 30
MULTIPLYING_FACTOR = 150
X_VALUE_STEP = MULTIPLYING_FACTOR / 2
Y_VALUE_STEP = X_VALUE_STEP / MULTIPLYING_FACTOR

x = 0.1

options_open = False
points = [[(0, 0, 255), "sin"], [(255, 0, 0), "cos"], [(0, 255, 0)], [(255, 0, 255), "sec"], [(255, 165, 0), "csc"]]

def append_x_y_cor_for_graphs():
    global x, points

    if x < WIDTH:
        sin_val = math.sin(math.radians(x))
        cos_val = math.cos(math.radians(x))
        sin_2_cos_2_val = sin_val ** 2 + cos_val ** 2
        sec_val = 1 / cos_val
        csc_val = 1 / sin_val

        points[0].append((X_VALUE_STEP + x, HEIGHT / 2 - sin_val * MULTIPLYING_FACTOR))
        points[1].append((X_VALUE_STEP + x, HEIGHT / 2 + cos_val * MULTIPLYING_FACTOR))
        points[2].append((X_VALUE_STEP + x, HEIGHT / 2 - sin_2_cos_2_val * MULTIPLYING_FACTOR))
        points[2].append((X_VALUE_STEP + x, HEIGHT / 2 + sin_2_cos_2_val * MULTIPLYING_FACTOR))

        if cos_val != 0:
            sec_y = HEIGHT / 2 + sec_val * MULTIPLYING_FACTOR
            if -HEIGHT < sec_y < HEIGHT * 2:
                points[3].append((X_VALUE_STEP + x, sec_y))

        if sin_val != 0:
            csc_y = HEIGHT / 2 + csc_val * MULTIPLYING_FACTOR
            if -HEIGHT < csc_y < HEIGHT * 2:
                points[4].append((X_VALUE_STEP + x, csc_y))
        x += 0.1

def draw_grid_and_values():
    # Horz x-axis line
    screen.draw.line((0, HEIGHT / 2), (WIDTH, HEIGHT / 2), (0, 0, 0))
    screen.draw.line((0, HEIGHT / 2 + 1), (WIDTH, HEIGHT / 2 + 1), (0, 0, 0))
    
    # Vertical y-axis line
    screen.draw.line((X_VALUE_STEP + 1, 0), (X_VALUE_STEP + 1, HEIGHT), (0, 0, 0))

    x_step_with_mf = int(X_VALUE_STEP)
    y_step_with_mf = int(Y_VALUE_STEP * MULTIPLYING_FACTOR)
    for i in range(0, WIDTH + 1, x_step_with_mf):
        screen.draw.text(str(i), color="black", bottomleft=(i + X_VALUE_STEP, HEIGHT / 2), fontsize=20)
        screen.draw.line((i, HEIGHT), (i, 0), (150, 150, 150))
    for i in range(0, HEIGHT // 2 + 1, y_step_with_mf):
        if i != 0:
            screen.draw.text(str(-(i / MULTIPLYING_FACTOR)), color="black", bottomright=(X_VALUE_STEP, i + HEIGHT / 2), fontsize=30)
            screen.draw.text(str(i / MULTIPLYING_FACTOR), color="black", bottomright=(X_VALUE_STEP, HEIGHT / 2 - i), fontsize=30)
            screen.draw.line((WIDTH, HEIGHT - i), (0, HEIGHT - i), (150, 150, 150))
            screen.draw.line((WIDTH, i), (0, i), (150, 150, 150))

def draw_legend_and_options_rect():
    global points, resart_animation_1, resart_animation_2, options_open, options_rect

    screen.draw.text("Degrees", color="black", center = ((WIDTH - X_VALUE_STEP) / 2, HEIGHT / 2 + 10), fontsize=30)
    for i in range(0, len(points)):
        if i != 2:
            if i < 2:
                screen.draw.filled_rect(pygame.Rect(WIDTH - 120, (i + 1) * 20, 30, 5), points[i][0])
                screen.draw.text("= " + points[i][1], color="black", topleft = (WIDTH - 80, ((i + 1) * 20) - 10), fontsize=30)
            else:
                screen.draw.filled_rect(pygame.Rect(WIDTH - 120, (i) * 20, 30, 5), points[i][0])
                screen.draw.text("= " + points[i][1], color="black", topleft = (WIDTH - 80, (i * 20) - 10), fontsize=30)

    resart_animation_1 = pygame.Rect(WIDTH / 2, 40, 75, 20)
    resart_animation_2 = pygame.Rect(WIDTH / 2 - 10, 60, 95, 20)
    options_rect = pygame.Rect(WIDTH / 2, 0, 75, 20)
    screen.draw.filled_rect(options_rect, (130, 130, 130))

    screen.draw.textbox("Options", options_rect, color=(255, 255, 255))

    if options_open:
        screen.draw.filled_rect(resart_animation_1, (130, 130, 130))
        screen.draw.filled_rect(resart_animation_2, (130, 130, 130))
        screen.draw.textbox("Restart", resart_animation_1, color=(255, 255, 255))
        screen.draw.textbox("animation", resart_animation_2, color=(255, 255, 255))

def draw():
    global x, resart_animation_1, resart_animation_2, options_open, options_rect
    screen.fill("white")
    draw_grid_and_values()
    draw_legend_and_options_rect()
    for graph_points in points:
        for index, point in enumerate(graph_points):
            if index != 0 and index != 1:
                screen.draw.circle(point, 1, graph_points[0])

def on_mouse_down(pos):
    global resart_animation_1, resart_animation_2, x, points, options_open
    if resart_animation_1.collidepoint(pos) or resart_animation_2.collidepoint(pos):
        if options_open:
            x = 0.1
            points = [[(0, 0, 255), "sin"], [(255, 0, 0), "cos"], [(0, 255, 0)], [(255, 0, 255), "sec"], [(255, 165, 0), "csc"]]
            options_open = False
    if options_rect.collidepoint(pos) and not options_open:
        options_open = True

for i in range(0, SPEED_OF_ANIMATION):
    clock.schedule_interval(append_x_y_cor_for_graphs, 0.01)

pgzrun.go()
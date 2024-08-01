import pgzrun
import pygame
import math
from pgzero.clock import clock

WIDTH = 800
HEIGHT = 600
SPEED_OF_ANIMATION = 20
MULTIPLYING_FACTOR = 100
X_VALUE_STEP = MULTIPLYING_FACTOR / 2
Y_VALUE_STEP = X_VALUE_STEP / MULTIPLYING_FACTOR

points = [[(0, 0, 255)], [(255, 0, 0)]]
x = -1

def append_points_for_graphs():
    global x, points
    if x >= -1 and x <= 1:
        arcsin_value = math.asin(x)
        arccos_value = math.acos(x)
        points[0].append((WIDTH // 2 + x * MULTIPLYING_FACTOR, HEIGHT // 2 - (arcsin_value * MULTIPLYING_FACTOR)))
        points[1].append((WIDTH // 2 + x * MULTIPLYING_FACTOR, HEIGHT // 2 - (arccos_value * MULTIPLYING_FACTOR)))
    x += 0.0005

def draw_grid_and_values():
    screen.draw.line((0, HEIGHT // 2), (WIDTH, HEIGHT // 2), (0, 0, 0))
    screen.draw.line((0, HEIGHT // 2 + 1), (WIDTH + 0, HEIGHT // 2 + 1), (0, 0, 0))
    
    screen.draw.line((WIDTH // 2 + 1, 0), (WIDTH // 2 + 1, HEIGHT), (0, 0, 0))
    
    x_step_with_mf = int(X_VALUE_STEP)
    y_step_with_mf = int(Y_VALUE_STEP * MULTIPLYING_FACTOR)
    for i in range(0, WIDTH // 2 + 1, x_step_with_mf):
        screen.draw.text(str(i), color="black", bottomleft=(i + WIDTH / 2, HEIGHT / 2), fontsize=20)
        screen.draw.text(str(-i), color="black", bottomleft=(WIDTH / 2 - i, HEIGHT / 2), fontsize=20)
    for i in range(0, WIDTH + 1, x_step_with_mf):
        screen.draw.line((i + WIDTH / 2, HEIGHT), (i + WIDTH / 2, 0), (150, 150, 150))
    for i in reversed(range(0, WIDTH + 1, x_step_with_mf)):
            screen.draw.line((i + WIDTH / 2, HEIGHT), (i + WIDTH / 2, 0), (150, 150, 150))
            # screen.draw.line((i, HEIGHT), (i, 0), (150, 150, 150))
    
    for i in range(0, HEIGHT // 2 + 1, y_step_with_mf):
        if i != 0:
            screen.draw.text(str(-(i / MULTIPLYING_FACTOR)), color="black", bottomright=(WIDTH / 2, i + HEIGHT / 2), fontsize=20)
            screen.draw.text(str(i / MULTIPLYING_FACTOR), color="black", bottomright=(WIDTH / 2, HEIGHT / 2 - i), fontsize=20)
            screen.draw.line((WIDTH, HEIGHT - i), (0, HEIGHT - i), (150, 150, 150))
            screen.draw.line((WIDTH, i), (0, i), (150, 150, 150))

def draw_legend_and_options_rect():
    screen.draw.filled_rect(pygame.Rect(WIDTH - 120, 20, 30, 5), (0, 0, 255))
    screen.draw.filled_rect(pygame.Rect(WIDTH - 120, 40, 30, 5), (255, 0, 0))
    screen.draw.filled_rect(pygame.Rect(WIDTH - 120, 60, 30, 5), (255, 0, 255))
    screen.draw.filled_rect(pygame.Rect(WIDTH - 120, 80, 30, 5), (255, 165, 0))
    screen.draw.filled_rect(pygame.Rect(WIDTH - 120, 100, 30, 5), (0, 255, 255))
    screen.draw.text("Degrees", color="black", center = ((WIDTH - 50) / 2, HEIGHT / 2 + 10), fontsize=30)
    screen.draw.text("= arcsin", color="black", topleft = (WIDTH - 80, 10), fontsize=30)
    screen.draw.text("= arccos", color="black", topleft = (WIDTH - 80, 30), fontsize=30)
    # screen.draw.text("= sec", color="black", topleft = (WIDTH - 80, 50), fontsize=30)
    # screen.draw.text("= csc", color="black", topleft = (WIDTH - 80, 70), fontsize=30)
    # screen.draw.text("= sin ^ 2", color="black", topleft = (WIDTH - 80, 90), fontsize=30)

def draw():
    global points
    screen.fill("white")
    draw_grid_and_values()
    draw_legend_and_options_rect()
    for graph_points in points:
        for index, point in enumerate(graph_points):
            if index != 0:
                screen.draw.circle(point, 1, graph_points[0])

for i in range(0, SPEED_OF_ANIMATION):
    clock.schedule_interval(append_points_for_graphs, 0.01)

pgzrun.go()
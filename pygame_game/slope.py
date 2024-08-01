import pgzrun
from pgzero import clock

WIDTH = 800
HEIGHT = 600
X_VALUE_STEP = 50
Y_VALUE_STEP = 50
NUM_OF_LINES = 60 # number of lines must be a multiple of 60. if not, it will round. number must not be 0

slope = -15

def draw_grid_and_values():
    screen.draw.line((0, HEIGHT // 2), (WIDTH, HEIGHT // 2), (0, 0, 0))
    screen.draw.line((0, HEIGHT // 2 + 1), (WIDTH + 0, HEIGHT // 2 + 1), (0, 0, 0))
    
    screen.draw.line((WIDTH // 2 + 1, 0), (WIDTH // 2 + 1, HEIGHT), (0, 0, 0))
    
    x_step_with_mf = int(X_VALUE_STEP)
    y_step_with_mf = int(Y_VALUE_STEP)
    for i in range(0, WIDTH // 2 + 1, x_step_with_mf):
        screen.draw.text(str(i), color="black", bottomleft=(i + WIDTH / 2, HEIGHT / 2), fontsize=20)
        screen.draw.text(str(-i), color="black", bottomleft=(WIDTH / 2 - i, HEIGHT / 2), fontsize=20)
    for i in range(0, WIDTH + 1, x_step_with_mf):
        screen.draw.line((i + WIDTH / 2, HEIGHT), (i + WIDTH / 2, 0), (150, 150, 150))
        screen.draw.line((i, HEIGHT), (i, 0), (150, 150, 150))
    
    for i in range(0, HEIGHT // 2 + 1, y_step_with_mf):
        if i != 0:
            screen.draw.text(str(-(i)), color="black", bottomright=(WIDTH / 2, i + HEIGHT / 2), fontsize=20)
            screen.draw.text(str(i), color="black", bottomright=(WIDTH / 2, HEIGHT / 2 - i), fontsize=20)
            screen.draw.line((WIDTH, HEIGHT - i), (0, HEIGHT - i), (150, 150, 150))
            screen.draw.line((WIDTH, i), (0, i), (150, 150, 150))

def draw():
    global slope, slope_points
    screen.fill("white")
    draw_grid_and_values()
    for i in range(slope * int(NUM_OF_LINES / 60), 0):
        screen.draw.line((700 - (50 * i / (NUM_OF_LINES / 60)), 0), (WIDTH / 2, HEIGHT / 2), (0, 0, 0))
        screen.draw.line((700 - (50 * i / (NUM_OF_LINES / 60)) + 1, 0), (WIDTH / 2 + 1, HEIGHT / 2), (0, 0, 0))
        screen.draw.line((WIDTH / 2, HEIGHT / 2), (WIDTH - (700 - (50 * i / (NUM_OF_LINES / 60))), HEIGHT), (0, 0, 0))
        screen.draw.line((WIDTH / 2 + 1, HEIGHT / 2), (WIDTH - (700 - (50 * i / (NUM_OF_LINES / 60)) - 1), HEIGHT), (0, 0, 0))
    for i in range(0, abs(slope * int(NUM_OF_LINES / 60)) + 1):
        screen.draw.line((700 - (50 * i / (NUM_OF_LINES / 60)), 0), (WIDTH / 2, HEIGHT / 2), (0, 0, 0))
        screen.draw.line((700 - (50 * i / (NUM_OF_LINES / 60)) + 1, 0), (WIDTH / 2 + 1, HEIGHT / 2), (0, 0, 0))
        screen.draw.line((WIDTH / 2, HEIGHT / 2), (WIDTH - (700 - (50 * i / (NUM_OF_LINES / 60))), HEIGHT), (0, 0, 0))
        screen.draw.line((WIDTH / 2 + 1, HEIGHT / 2), (WIDTH - (700 - (50 * i / (NUM_OF_LINES / 60)) - 1), HEIGHT), (0, 0, 0))

pgzrun.go()
import pgzrun
import math

WIDTH = 800
HEIGHT = 600

def draw():
    screen.fill("white")
    for i in range(0, WIDTH, 75):
        screen.draw.line((i, 0), (i, HEIGHT), (0, 0, 0))
        screen.draw.line((0, i), (WIDTH, i), (0, 0, 0))
    screen.draw.text("Degrees", color="black", center=(75 / 2, 75 / 2), fontsize=30)
    screen.draw.text("Sin", color="black", center=(75 / 2, (75 / 2) + 75), fontsize=30)
    screen.draw.text("Cos", color="black", center=(75 / 2, (75 / 2) + 75 * 2), fontsize=30)
    screen.draw.text("Tan", color="black", center=(75 / 2, (75 / 2) + 75 * 3), fontsize=30)
    for i in range(0, 91, 10):
        screen.draw.text(str(i), color="black", center=((75 / 2) + 75 * ((i / 10) + 1), 75 / 2), fontsize=30)
        screen.draw.text(str(round(math.sin(math.radians(i)), 2)), color="black", center=((75 / 2) + 75 * ((i / 10) + 1), (75 / 2) + 75), fontsize=30)
        screen.draw.text(str(round(math.cos(math.radians(i)), 2)), color="black", center=((75 / 2) + 75 * ((i / 10) + 1), (75 / 2) + 75 * 2), fontsize=30)
        if i != 90:
            screen.draw.text(str(round(math.tan(math.radians(i)), 2)), color="black", center=((75 / 2) + 75 * ((i / 10) + 1), (75 / 2) + 75 * 3 ), fontsize=30)
        else:
            screen.draw.text("*", color="black", center=((75 / 2) + 75 * ((i / 10) + 1), (75 / 2) + 75 * 3), fontsize=70)
    
def update():
    pass

pgzrun.go()
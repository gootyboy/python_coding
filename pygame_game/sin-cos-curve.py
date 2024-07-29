import pgzrun, math

WIDTH = 800
HEIGHT = 600

def draw():
    screen.fill("white")
    for i in range(0, WIDTH, 1):
        if i % 90 != 0:
            screen.draw.circle((i, HEIGHT / 2 + (10 / math.tan(math.radians(i))) * 100), 1, (0, 0, 100))
            screen.draw.circle((i, HEIGHT / 2 + (math.tan(math.radians(i))) * 100), 1, (0, 0, 100))

    screen.draw.line((0, HEIGHT / 2), (WIDTH, HEIGHT / 2), (0, 0, 0))
    screen.draw.line((0, HEIGHT / 2 + 1), (WIDTH, HEIGHT / 2 + 1), (0, 0, 0))
    screen.draw.line((50, 0), (50, HEIGHT), (0, 0, 0))
    screen.draw.line((50, 1), (50, HEIGHT + 1), (0, 0, 0))

def update():
    pass

pgzrun.go()
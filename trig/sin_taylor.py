import pgzrun, math
import numpy as np

WIDTH = 800
HEIGHT = 600
MF = 100

# def draw():
#     screen.fill("white")
#     for i in range(0, WIDTH, 1):
#         radians_i = math.radians(i)
#         taylor_sinx = radians_i - ((radians_i**3)/math.factorial(3)) + ((radians_i**5)/math.factorial(5)) - ((radians_i**7)/math.factorial(7))
#         # screen.draw.circle((i, HEIGHT / 2 + (math.sin(radians_i)) * MF), 1, (255, 0, 0))
#         screen.draw.circle((i, HEIGHT / 2 + taylor_sinx * MF), 1, (0, 0, 255))

#     screen.draw.line((0, HEIGHT / 2), (WIDTH, HEIGHT / 2), (0, 0, 0))
#     screen.draw.line((0, HEIGHT / 2 + 1), (WIDTH, HEIGHT / 2 + 1), (0, 0, 0))
#     screen.draw.line((50, 0), (50, HEIGHT), (0, 0, 0))
#     screen.draw.line((50, 1), (50, HEIGHT + 1), (0, 0, 0))

def draw():
    screen.fill("white")

    raidans = np.arange(0, 6, 0.5).tolist()
    for radians_i in raidans:
        taylor_sinx = radians_i - ((radians_i**3)/math.factorial(3)) + ((radians_i**5)/math.factorial(5)) - ((radians_i**7)/math.factorial(7))
        # screen.draw.circle((i, HEIGHT / 2 + (math.sin(radians_i)) * MF), 1, (255, 0, 0))
        print(math.degrees(radians_i) , taylor_sinx)
        # print(i, taylor_sinx)
        screen.draw.circle((math.degrees(radians_i), HEIGHT / 2 + taylor_sinx * MF), 1, (0, 0, 255))
        # print(i)

    screen.draw.line((0, HEIGHT / 2), (WIDTH, HEIGHT / 2), (0, 0, 0))
    screen.draw.line((0, HEIGHT / 2 + 1), (WIDTH, HEIGHT / 2 + 1), (0, 0, 0))
    screen.draw.line((50, 0), (50, HEIGHT), (0, 0, 0))
    screen.draw.line((50, 1), (50, HEIGHT + 1), (0, 0, 0))

def update():
    pass

pgzrun.go()
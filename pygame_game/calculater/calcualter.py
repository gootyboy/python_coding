import pgzero
import pgzrun
from pgzero.rect import Rect

WIDTH = 800
HEIGHT = 600
TITLE = "Calculator"
NUM_COLOR = (128, 128, 128)
OPERATER_COLOR = (255, 127.5, 0)
list_numbers_1 = []
number_1 = None
operater_pressed = False
operater = None
list_numbers_2 = []
result = None

number_rects = {
    "1": Rect(400, 400, 75, 75),
    "2": Rect(500, 400, 75, 75),
    "3": Rect(600, 400, 75, 75),
    "4": Rect(400, 300, 75, 75),
    "5": Rect(500, 300, 75, 75),
    "6": Rect(600, 300, 75, 75),
    "7": Rect(400, 200, 75, 75),
    "8": Rect(500, 200, 75, 75),
    "9": Rect(600, 200, 75, 75),
    "0": Rect(500, 500, 75, 75),
    ".": Rect(600, 500, 75, 75)
}

operators_rects = {
    "÷": Rect(700, 100, 75, 75),
    "x": Rect(700, 200, 75, 75),
    "-": Rect(700, 300, 75, 75),
    "+": Rect(700, 400, 75, 75),
    "=": Rect(700, 500, 75, 75)
}

def restart_calculation(start_number):
    global number_rects, operators_rects, list_numbers_1, operater, result, list_numbers_2, operater_pressed
    list_numbers_1 = list(str(result))
    operater_pressed = False
    operater = None
    list_numbers_2 = []
    result = None

def draw():
    global number_rects, operators_rects, list_numbers_1, operater, result
    screen.fill((255, 255, 255))

    for number, rect in number_rects.items():
        screen.draw.circle((rect.centerx, rect.centery), 40, (0, 0, 0))
        screen.draw.filled_circle((rect.centerx, rect.centery), 40, NUM_COLOR)
        screen.draw.textbox(rect=rect, text=str(number), color=(255, 255, 255))

    for symbol, rect in operators_rects.items():
        screen.draw.circle((rect.centerx, rect.centery), 40, (0, 0, 0))
        screen.draw.filled_circle((rect.centerx, rect.centery), 40, OPERATER_COLOR)
        screen.draw.textbox(rect=rect, text=str(symbol), color=(255, 255, 255))

    if result == None:
        if not operater_pressed and len(list_numbers_1) > 0 and len(list_numbers_2) == 0:
            screen.draw.text("".join(list_numbers_1), topright= (800, 0), fontsize=100, color=(0, 0, 0))
        if operater_pressed and len(list_numbers_1) > 0 and len(list_numbers_2) == 0:
            screen.draw.text("".join(list_numbers_1) + operater, topright= (800, 0), fontsize=100, color=(0, 0, 0))
        if operater_pressed and len(list_numbers_1) > 0 and len(list_numbers_2) > 0:
            screen.draw.text("".join(list_numbers_1) + operater + "".join(list_numbers_2), topright= (800, 0), fontsize=100, color=(0, 0, 0))
    else:
        screen.draw.text(str(result), topright= (800, 0), fontsize=100, color=(0, 0, 0))
        restart_calculation(result)

def on_mouse_down(pos):
    global operater_pressed, list_numbers_2, list_numbers_1, operater
    for number, rect in number_rects.items():
        if rect.collidepoint(pos):
            if operater_pressed:
                list_numbers_2.append(number)
                print(list_numbers_2)
            else:
                list_numbers_1.append(number)
                print(list_numbers_1)
    
    for symbol, rect in operators_rects.items():
        if rect.collidepoint(pos) and len(list_numbers_1) > 0:
            if symbol != "=" and len(list_numbers_2) >= 0 and len(list_numbers_1) > 0:
                operater = symbol
                operater_pressed = True
                print(operater)
            if symbol == "=" and len(list_numbers_1) > 0 and len(list_numbers_2) > 0:
                operater_pressed = False
                if operater == "+":
                    result = float("".join(list_numbers_1)) + float("".join(list_numbers_2))
                elif operater == "-":
                    result = float("".join(list_numbers_1)) - float("".join(list_numbers_2))
                elif operater == "x":
                    result = float("".join(list_numbers_1)) * float("".join(list_numbers_2))
                elif operater == "÷":
                    result = float("".join(list_numbers_1)) / float("".join(list_numbers_2))
                else:
                    result = None
                print(result)

pgzrun.go()
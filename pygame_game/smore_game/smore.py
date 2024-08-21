import pgzrun
from pgzero.actor import Actor
from pgzero.rect import Rect

WIDTH = 800
HEIGHT = 600

items = {
    "stick": {
        "image": Actor("stick", (700, 300)),
        "is_clicked": False,
        "disappear": False
    },
    "marshmellow": {
        "image": Actor("marshmellow"),
        "is_clicked": False,
        "disappear": False
    },
}

marshmellow_stick_rect = Rect(items["stick"]["image"].x - 40, items["stick"]["image"].y - 170, 75, 100)

def draw():
    screen.fill("white")
    for item in items.values():
        if not item["disappear"]:
            item["image"].draw()

def update():
    pass

def on_mouse_down(pos):
    if items["marshmellow"]["image"].collidepoint(pos) and not items["marshmellow"]["disappear"]:
        items["marshmellow"]["is_clicked"] = True
    if items["stick"]["image"].collidepoint(pos) and items["marshmellow"]["disappear"]:
        items["stick"]["is_clicked"] = True

def on_mouse_up():
    if not items["marshmellow"]["disappear"]:
        items["marshmellow"]["is_clicked"] = False
    if not items["stick"]["disappear"] and items["marshmellow"]["disappear"]:
        items["stick"]["is_clicked"] = False

def on_mouse_move(pos):
    global marshmellow_stick_rect
    if not items["marshmellow"]["image"].colliderect(marshmellow_stick_rect):
        if items["marshmellow"]["is_clicked"] and pos[0] > 0 and pos[0] < WIDTH and pos[1] > 0 and pos[1] < HEIGHT:
            items["marshmellow"]["image"].pos = pos
    else:
        items["marshmellow"]["disappear"] = True
        items["stick"]["image"].image = "stick_marshmellow"
    if items["stick"]["is_clicked"] and pos[0] > 0 and pos[0] < WIDTH and pos[1] > 0 and pos[1] < HEIGHT:
        if items["marshmellow"]["disappear"]:
            items["stick"]["image"].pos = pos

pgzrun.go()
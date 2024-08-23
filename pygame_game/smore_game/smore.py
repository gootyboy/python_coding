import pgzrun
import pygame
from PIL import Image, ImageSequence
from pgzero.actor import Actor
from pgzero.rect import Rect
from pgzero.clock import clock
from pygame.rect import Rect

WIDTH = 800
HEIGHT = 600

STICK_ANGLE = 55
TIME_TO_ROAST = 5 # seconds
TIME_TO_BURN = 10 # seconds

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
    }
}

marshmellow_stick_rect = Rect(items["stick"]["image"].x - 40, items["stick"]["image"].y - 170, 75, 100)
fire_rect = Rect(Actor("fire").x - Actor("fire").width * 0.5 / 4 + 75, Actor("fire").y + Actor("fire").height * 0.5 / 4 - 200, Actor("fire").width - 400, Actor("fire").height - 100)
frames = [frame.copy() for frame in ImageSequence.Iterator(Image.open(r'boy/pygame_game/smore_game/images/fire.gif'))]

arrow_clicked = False
time_roasted = 0
current_frame = 0
frame_delay = 0.1
last_update_time = 0

def draw_fire_gif(pos):
    frame_image = frames[current_frame]
    size = frame_image.size
    data = frame_image.convert("RGBA").tobytes()

    frame_surface = pygame.image.fromstring(data, size, "RGBA")
    screen.blit(frame_surface, pos)

def draw():
    global time_roasted, fire_rect
    if not arrow_clicked:
        screen.clear()
        draw_fire_gif((WIDTH / 2 - Actor("fire").width / 2, 50))
        items["stick"]["image"].angle = STICK_ANGLE
        screen.draw.text("Press the arrow to continue", fontsize=60, center=(WIDTH / 2, 50), color=(255, 255, 255))
        screen.draw.text("->", fontsize=80, center=(WIDTH - 50, 50), color=(255, 255, 255))
        for item in items.values():
            if not item["disappear"]:
                item["image"].draw()
        if time_roasted >= TIME_TO_ROAST and time_roasted < TIME_TO_BURN:
            items["stick"]["image"].image = "stick_roasted_marshmellow"
        if time_roasted == TIME_TO_BURN:
            items["stick"]["image"].image = "stick_burnt_marshmellow"
        
def update():
    global current_frame, last_update_time
    if pygame.time.get_ticks() - last_update_time > frame_delay * 1000 and not arrow_clicked:
        current_frame = (current_frame + 1) % len(frames)
        last_update_time = pygame.time.get_ticks()

def on_mouse_down(pos):
    if not arrow_clicked:
        if items["marshmellow"]["image"].collidepoint(pos) and not items["marshmellow"]["disappear"]:
            items["marshmellow"]["is_clicked"] = True
        if items["stick"]["image"].collidepoint(pos) and items["marshmellow"]["disappear"]:
            items["stick"]["is_clicked"] = True

def on_mouse_up():
    if not arrow_clicked:
        if not items["marshmellow"]["disappear"]:
            items["marshmellow"]["is_clicked"] = False
        if not items["stick"]["disappear"] and items["marshmellow"]["disappear"]:
            items["stick"]["is_clicked"] = False

def on_mouse_move(pos):
    global marshmellow_stick_rect
    if not arrow_clicked:
        if not items["marshmellow"]["image"].colliderect(marshmellow_stick_rect):
            if items["marshmellow"]["is_clicked"] and pos[0] > 0 and pos[0] < WIDTH and pos[1] > 0 and pos[1] < HEIGHT:
                items["marshmellow"]["image"].pos = pos
        else:
            items["marshmellow"]["disappear"] = True
            if items["stick"]["image"].image == "stick":
                items["stick"]["image"].image = "stick_marshmellow"
        if items["stick"]["is_clicked"] and pos[0] > 0 and pos[0] < WIDTH and pos[1] > 0 and pos[1] < HEIGHT:
            if items["marshmellow"]["disappear"]:
                items["stick"]["image"].pos = pos

def update_time_roasted():
    global time_roasted
    if not arrow_clicked:
        if time_roasted < TIME_TO_ROAST and items["stick"]["image"].colliderect(fire_rect) and items["stick"]["image"].image == "stick_marshmellow":
            time_roasted += 1
        if time_roasted >= TIME_TO_ROAST and time_roasted < TIME_TO_BURN and items["stick"]["image"].colliderect(fire_rect) and items["stick"]["image"].image == "stick_roasted_marshmellow":
            time_roasted += 1

clock.schedule_interval(update_time_roasted, 1)

pgzrun.go()
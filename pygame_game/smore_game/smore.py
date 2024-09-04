import pgzrun
import pygame
import os
import inspect
from PIL import Image, ImageSequence
from pgzero.actor import Actor
from pgzero.rect import Rect
from pgzero.clock import clock

WIDTH = 800
HEIGHT = 600

TIME_TO_ROAST = 5 # seconds
TIME_TO_BURN = 10 # seconds
TIME_TO_CHOCO_MELT = 3 # seconds
FIRE_SPEED = 0.1

BASE_PATH = os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))),"images")

items = {
    "stick": {
        "image": Actor("stick", (700, 300)),
        "is_clicked": False,
        "disappear": False
    },
    "marshmellow": {
        "image": Actor("marshmellow", (33.5, 37.5)),
        "is_clicked": False,
        "disappear": False
    },
}

smore_items = {
    "cracker": {
            "image": Actor("cracker", (Actor("cracker").width / 2, Actor("cracker").height / 2)),
            "image_copy": Actor("cracker", (WIDTH / 2, HEIGHT / 2)),
            "is_clicked": False
        },
    "chocolate": {
            "image": Actor("dark_chocolate", (Actor("dark_chocolate").width / 2, Actor("dark_chocolate").height / 2 + 200)),
            "image_copy": Actor("dark_chocolate", (WIDTH / 2, HEIGHT / 2)),
            "is_clicked": False
        }
    }

rects = {
    "marshmellow_stick_rect": Rect(550, 175, 75, 100),
    "fire_rect": Rect(300, 80, 200, 350),
    "arrow_rect": Rect(WIDTH / 2 + 300, 0, 80, 80),
    "restart_rect": Rect(10, HEIGHT - 75, 240, 65)
}

frames = [frame.copy() for frame in ImageSequence.Iterator(Image.open(r'boy/pygame_game/smore_game/images/fire.gif'))]

arrow_clicked = False
image_updated = False
time_roasted = 0
current_frame = 0
last_update_time = 0
time_choco_melted = 0

def restart_game():
    global items, smore_items, frames, arrow_clicked, image_updated, time_roasted, current_frame, last_update_time
    items = {
        "stick": {
            "image": Actor("stick", (700, 300)),
            "is_clicked": False,
            "disappear": False
        },
        "marshmellow": {
            "image": Actor("marshmellow", (33.5, 37.5)),
            "is_clicked": False,
            "disappear": False
        },
    }

    smore_items = {
        "cracker": {
                "image": Actor("cracker", (Actor("cracker").width / 2, Actor("cracker").height / 2)),
                "image_copy": Actor("cracker", (Actor("cracker").width / 2, Actor("cracker").height / 2)),
                "new_pos": (WIDTH / 2, HEIGHT / 2)
            }
        }

    arrow_clicked = False
    image_updated = False
    time_roasted = 0
    last_update_time = 0

def text(text, fontsize, topleft, color):
    screen.draw.text(str(text), fontsize=fontsize, topleft=topleft, color=color)

def resize_image(actor_path, increase_pixels, angle):
    actor_image = Image.open(actor_path)
    actor_image.rotate(angle).resize((actor_image.width + increase_pixels, actor_image.height + increase_pixels), Image.LANCZOS).save(f"{actor_path.removesuffix(".png")}_resized.png")

def draw_fire_gif(pos):
    frame_image = frames[current_frame]
    screen.blit(pygame.image.fromstring(frame_image.convert("RGBA").tobytes(), frame_image.size, "RGBA"), pos)

def update_marshmellow_image(marshmellow_image):
    org_image = os.path.join(BASE_PATH,f"{marshmellow_image.image.removesuffix(".png")}") + ".png"
    remove_image = os.path.join(BASE_PATH,f"{marshmellow_image.image.removesuffix(".png")}_resized.png")

    resize_image(org_image, 20, 31.5)
    marshmellow_actor = Actor(remove_image, (WIDTH / 2 - 4, HEIGHT / 2 - 5))

    if os.path.exists(remove_image):
        os.remove(remove_image)

    return marshmellow_actor

def update_cracker_image(cracker_image):
    cracker_name = cracker_image.image
    cracker_image = os.path.join(BASE_PATH,f"{cracker_name.removesuffix(".png")}") + ".png"
    remove_cracker_image = os.path.join(BASE_PATH,f"{cracker_name.removesuffix(".png")}_resized.png")

    resize_image(cracker_image, 60, 0)
    cracker_actor = Actor(remove_cracker_image, (WIDTH / 2, HEIGHT / 2))

    if os.path.exists(remove_cracker_image):
        os.remove(remove_cracker_image)

    return cracker_actor

def draw():
    global time_roasted, current_frame, last_update_time, arrow_clicked, image_updated
    if not arrow_clicked:
        screen.fill("black")
        draw_fire_gif((WIDTH / 2 - Actor("fire").width / 2, 50))
        items["stick"]["image"].angle = 55
        text("Press the arrow to continue", fontsize=60, topleft=(WIDTH / 2 - 300, 10), color=(255, 255, 255))
        text("->", fontsize=80, topleft=(WIDTH / 2 + 300, 0), color="purple")
        for item in items.values():
            if not item["disappear"]:
                item["image"].draw()
        if time_roasted >= TIME_TO_ROAST and time_roasted < TIME_TO_BURN:
            items["stick"]["image"].image = "stick_roasted_marshmellow"
            items["marshmellow"]["image"].image = "roasted_marshmellow"
        elif time_roasted == TIME_TO_BURN:
            items["stick"]["image"].image = "stick_burnt_marshmellow"
            items["marshmellow"]["image"].image = "burnt_marshmellow"
    else:
        screen.fill("white")
        for smore_item in smore_items.values():
            smore_item["image"].draw()
            text(f"{smore_item["image"].image}", 50, (smore_item["image"].x - (smore_item["image"].width / 4), smore_item["image"].y + (smore_item["image"].height / 2)), "black")
            if smore_item["is_clicked"]:
                text(f"(added)", 30, (smore_item["image"].x - (smore_item["image"].width / 4), smore_item["image"].y + smore_item["image"].height), "black")
        if smore_items["cracker"]["is_clicked"]:
            smore_items["cracker"]["image_copy"].draw()
        if not image_updated:
            items["marshmellow"]["image"] = update_marshmellow_image(items["marshmellow"]["image"])
            image_updated = True
        items["marshmellow"]["image"].draw()
        if smore_items["chocolate"]["is_clicked"]:
            smore_items["chocolate"]["image_copy"].draw()
        if time_choco_melted == TIME_TO_CHOCO_MELT:
            smore_items["chocolate"]["image"].image = "chocolate_melted"
    text("Restart", fontsize=100, topleft=(10, HEIGHT - 75), color="red")

def update():
    global current_frame, last_update_time
    if pygame.time.get_ticks() - last_update_time > FIRE_SPEED * 1000 and not arrow_clicked:
        current_frame = (current_frame + 1) % len(frames)
        last_update_time = pygame.time.get_ticks()

def on_mouse_down(pos):
    global arrow_clicked
    if not arrow_clicked:
        if items["marshmellow"]["image"].collidepoint(pos) and not items["marshmellow"]["disappear"]:
            items["marshmellow"]["is_clicked"] = True
        if items["stick"]["image"].collidepoint(pos) and items["marshmellow"]["disappear"]:
            items["stick"]["is_clicked"] = True
        if rects["arrow_rect"].collidepoint(pos):
            arrow_clicked = True
    else:
        for smore_item in smore_items.values():
            if smore_item["image"].collidepoint(pos):
                smore_item["is_clicked"] = True 
    if rects["restart_rect"].collidepoint(pos):
        restart_game()

def on_mouse_up():
    if not arrow_clicked:
        if not items["marshmellow"]["disappear"]:
            items["marshmellow"]["is_clicked"] = False
        if not items["stick"]["disappear"] and items["marshmellow"]["disappear"]:
            items["stick"]["is_clicked"] = False
        if items["marshmellow"]["image"].colliderect(rects["marshmellow_stick_rect"]):
            items["marshmellow"]["disappear"] = True
            if items["stick"]["image"].image == "stick":
                items["stick"]["image"].image = "stick_marshmellow"

def on_mouse_move(pos):
    if not arrow_clicked:
        if items["marshmellow"]["is_clicked"] and pos[0] > 0 and pos[0] < WIDTH and pos[1] > 0 and pos[1] < HEIGHT:
            items["marshmellow"]["image"].pos = pos
        if items["stick"]["is_clicked"] and pos[0] > 0 and pos[0] < WIDTH and pos[1] > 0 and pos[1] < HEIGHT:
            if items["marshmellow"]["disappear"]:
                items["stick"]["image"].pos = pos

def update_time_roasted():
    global time_roasted, rects
    if not arrow_clicked:
        if time_roasted < TIME_TO_ROAST and items["stick"]["image"].colliderect(rects["fire_rect"]) and items["stick"]["image"].image == "stick_marshmellow":
            time_roasted += 1
        if time_roasted >= TIME_TO_ROAST and time_roasted < TIME_TO_BURN and items["stick"]["image"].colliderect(rects["fire_rect"]) and items["stick"]["image"].image == "stick_roasted_marshmellow":
            time_roasted += 1

def update_time_choco_melted():
    global time_choco_melted
    if arrow_clicked and smore_items["chocolate"]["clicked"]:
        if time_choco_melted < TIME_TO_CHOCO_MELT:
            time_choco_melted += 1

clock.schedule_interval(update_time_roasted, 1)
smore_items["cracker"]["image_copy"] = update_cracker_image(smore_items["cracker"]["image_copy"])

pgzrun.go()
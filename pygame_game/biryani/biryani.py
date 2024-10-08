import pgzrun
import pygame
from PIL import Image, ImageSequence
from pgzero.clock import clock
from pgzero.actor import Actor
from pgzero.rect import Rect

WIDTH = 800
HEIGHT = 600
TIME_TO_COOK = 5

ingredients = {
    "rice": {"image": Actor("rice", (Actor("rice").width / 2 + 10, Actor("rice").height / 2 + 10)), 
             "clicked": False},
    "egg": {"image": Actor("egg", (Actor("egg").width / 2 + 10, 150 + Actor("egg").height / 2 + 10)), 
            "clicked": False},
    "jackfruit": {"image": Actor("jackfruit", (Actor("jackfruit").width / 2 + 10, 250 + Actor("jackfruit").height / 2 + 10)), 
                  "clicked": False},
    "pepper": {"image": Actor("pepper", (Actor("pepper").width / 2 + 10, 375 + Actor("pepper").height / 2 + 10)), 
               "clicked": False},
    "onion": {"image": Actor("onion", (Actor("onion").width / 2 + 10, 475 + Actor("onion").height / 2 + 10)), 
              "clicked": False}
}

bowl_name = "bowl"
frames = [frame.copy() for frame in ImageSequence.Iterator(Image.open(r'boy/pygame_game/biryani/images/fire.gif'))]

current_frame = 0
frame_delay = 0.01  # Delay in seconds between frames
last_update_time = 0
fire_timer = TIME_TO_COOK
fire_on = False
fire_on_rect = Rect(690, 10, 100, 100)

sides = {"raita": {"image": Actor("raita", (WIDTH - Actor("raita").height * 1.5 / 2, 150 + Actor("raita").height / 2 + 60)), 
        "clicked": False,
        "pos": (550, 320)},
        "soda": {"image": Actor("soda", (WIDTH - Actor("soda").height * 1 / 2, 250+ Actor("soda").height / 2 + 110)), 
        "clicked": False,
        "pos": (250, 320)}}

play_agian = {
    "yes": [Rect(WIDTH / 2 - 150, 200, 80, 80), "green"],
    "no": [Rect(WIDTH / 2 + 50, 200, 80, 80), "red"]
}

clicked_ingredients = []

def list_contains(contain, lst, only_contain):
    return set(contain) == set(lst) if only_contain else all(item in lst for item in contain)

def reset_or_end_game(reset):
    global ingredients, bowl_name, frames, current_frame, frame_delay, last_update_time, fire_timer, fire_on, clicked_ingredients, sides
    if not reset:
        pgzrun.sys.exit()
    else:
        ingredients = {
    "rice": {"image": Actor("rice", (Actor("rice").width / 2 + 10, Actor("rice").height / 2 + 10)), 
             "clicked": False},
    "egg": {"image": Actor("egg", (Actor("egg").width / 2 + 10, 150 + Actor("egg").height / 2 + 10)), 
            "clicked": False},
    "jackfruit": {"image": Actor("jackfruit", (Actor("jackfruit").width / 2 + 10, 250 + Actor("jackfruit").height / 2 + 10)), 
                  "clicked": False},
    "pepper": {"image": Actor("pepper", (Actor("pepper").width / 2 + 10, 375 + Actor("pepper").height / 2 + 10)), 
               "clicked": False},
    "onion": {"image": Actor("onion", (Actor("onion").width / 2 + 10, 475 + Actor("onion").height / 2 + 10)), 
              "clicked": False}
}

        sides = {"raita": {"image": Actor("raita", (WIDTH - Actor("raita").height * 1.5 / 2, 150 + Actor("raita").height / 2 + 60)), 
        "clicked": False,
        "pos": (550, 320)},
        "soda": {"image": Actor("soda", (WIDTH - Actor("soda").height * 1 / 2, 250+ Actor("soda").height / 2 + 110)), 
        "clicked": False,
        "pos": (250, 320)}}
        bowl_name = "bowl"
        frames = [frame.copy() for frame in ImageSequence.Iterator(Image.open(r'boy/pygame_game/biryani/images/fire.gif'))]
        current_frame = 0
        frame_delay = 0.01
        last_update_time = 0
        fire_timer = TIME_TO_COOK
        fire_on = False
        clicked_ingredients = []

def draw_ingredients():
    global bowl, bowl_name
    screen.fill("white")
    bowl = Actor(bowl_name, (WIDTH / 2, HEIGHT / 2 + 100))
    for name, ingredient in ingredients.items():
        ingredient["image"].draw()
        screen.draw.text(name, topleft=(ingredient["image"].x - ingredient["image"].width / 2, ingredient["image"].y + ingredient["image"].height / 2), fontsize=40, color="black")
        if ingredient["clicked"]:
            screen.draw.text("(added)", topleft=(ingredient["image"].x - ingredient["image"].width / 2, ingredient["image"].y + (ingredient["image"].height * (2.5 if name != "rice" else 2) / 2)), fontsize=30, color="black")
    bowl.draw()
    screen.draw.text("sides", midleft=(680, 145), fontsize=60, color="black")
    for side_name, side in sides.items():
        side["image"].draw()
        screen.draw.text(side_name, center=(side["image"].x - side["image"].width * 0.5 / 2 + (20 if side_name == "raita" else 10), side["image"].y + side["image"].height / 2 + 20), fontsize=40, color="black")
        if side["clicked"]:
            screen.draw.text("(added)", center=(side["image"].x, side["image"].y + (side["image"].height / 2 + 50)), fontsize=30, color="black")
            Actor(side_name, side["pos"]).draw()

def handle_end_of_game():
    global bowl, bowl_name
    if clicked_ingredients:
        if list_contains(["rice", "egg", "pepper", "onion"], clicked_ingredients, False):
            bowl_name = "biryani"
        elif list_contains(["rice", "pepper"], clicked_ingredients, True) or list_contains(["rice", "onion"], clicked_ingredients, True) or \
            list_contains(["rice", "pepper", "onion"], clicked_ingredients, True):
            bowl_name = "biryani_rice"
        elif list_contains(["rice", "jackfruit", "pepper", "onion"], clicked_ingredients, True) or list_contains(["rice", "jackfruit", "pepper"], clicked_ingredients, True) or \
            list_contains(["rice", "jackfruit", "onion"], clicked_ingredients, True) or list_contains(["rice", "jackfruit"], clicked_ingredients, True):
            bowl_name = "biryani_jackfruit"
        elif list_contains(["rice"], clicked_ingredients, True):
            bowl_name = "rice_biryani"
        screen.draw.text("Cooking finished!", center=(bowl.x, 50), fontsize=50, color="black")
        ingredients_text = "You added: "
        for index, ingredient in enumerate(clicked_ingredients):
            ingredients_text += ingredient + (", " if index != len(clicked_ingredients) - 1 else "")

        screen.draw.text(ingredients_text, center=(bowl.x, 100), fontsize=50, color="black")
        screen.draw.text("Would you like to play again?", center=(bowl.x, 150), fontsize=50, color="black")
        for text, box in play_agian.items():
            screen.draw.filled_rect(box[0], box[1])
            screen.draw.textbox(text, box[0], color= "black")

def draw():
    global bowl, bowl_name, fire_on, fire_on_rect
    draw_ingredients()

    frame_image = frames[current_frame]
    size = frame_image.size
    data = frame_image.convert("RGBA").tobytes()

    frame_surface = pygame.image.fromstring(data, size, "RGBA")
    if fire_on and fire_timer > 0:
        screen.blit(frame_surface, (bowl.x - 225, bowl.y - 75))
    screen.draw.filled_rect(fire_on_rect, "gray")
    screen.draw.textbox("Start fire", fire_on_rect)
    if fire_timer > 0 and fire_on:
        screen.draw.text("time left to finish cooking: " + str(fire_timer), center=(bowl.x, 100), fontsize=30, color="black")
    if fire_timer == 0:
        handle_end_of_game()

def update():
    global current_frame, last_update_time
    if pygame.time.get_ticks() - last_update_time > frame_delay * 1000 and fire_on:
        current_frame = (current_frame + 1) % len(frames)
        last_update_time = pygame.time.get_ticks()

def update_bowl_name(bowl_name):
    if ingredients["rice"]["clicked"] and ingredients["jackfruit"]["clicked"] and not ingredients["egg"]["clicked"] and not ingredients["pepper"]["clicked"] and not ingredients["onion"]["clicked"]:
        name = "bowl_rice_jackfruit"
    elif ingredients["egg"]["clicked"] and ingredients["jackfruit"]["clicked"] and not ingredients["rice"]["clicked"] and not ingredients["pepper"]["clicked"] and not ingredients["onion"]["clicked"]:
        name = "bowl_egg_jackfruit"
    elif ingredients["rice"]["clicked"] and ingredients["egg"]["clicked"] and not ingredients["jackfruit"]["clicked"] and not ingredients["pepper"]["clicked"] and not ingredients["onion"]["clicked"]:
        name = "bowl_rice_egg"
    elif ingredients["rice"]["clicked"] and ingredients["egg"]["clicked"] and ingredients["jackfruit"]["clicked"] and not ingredients["pepper"]["clicked"] and not ingredients["onion"]["clicked"]:
        name = "bowl_rice_egg_jackfruit"
    elif ingredients["jackfruit"]["clicked"] and ingredients["onion"]["clicked"] and not ingredients["rice"]["clicked"] and not ingredients["pepper"]["clicked"] and not ingredients["egg"]["clicked"]:
        name = "bowl_jackfruit_onion"
    elif ingredients["jackfruit"]["clicked"] and ingredients["onion"]["clicked"] and ingredients["rice"]["clicked"] and not ingredients["pepper"]["clicked"] and not ingredients["egg"]["clicked"]:
        name = "bowl_rice_jackfruit_onion"
    elif ingredients["jackfruit"]["clicked"] and ingredients["onion"]["clicked"] and ingredients["rice"]["clicked"] and ingredients["egg"]["clicked"] and not ingredients["pepper"]["clicked"]:
        name = "bowl_rice_egg_jackfruit_onion"
    elif ingredients["jackfruit"]["clicked"] and ingredients["onion"]["clicked"] and ingredients["egg"]["clicked"] and not ingredients["rice"]["clicked"] and not ingredients["pepper"]["clicked"]:
        name = "bowl_egg_jackfruit_onion"
    elif ingredients["egg"]["clicked"] and ingredients["onion"]["clicked"] and not ingredients["jackfruit"]["clicked"] and not ingredients["rice"]["clicked"] and not ingredients["pepper"]["clicked"]:
        name = "bowl_egg_onion"
    elif ingredients["egg"]["clicked"] and ingredients["onion"]["clicked"] and ingredients["rice"]["clicked"] and not ingredients["jackfruit"]["clicked"] and not ingredients["pepper"]["clicked"]:
        name = "bowl_rice_egg_onion"
    elif ingredients["onion"]["clicked"] and ingredients["rice"]["clicked"] and not ingredients["egg"]["clicked"] and not ingredients["jackfruit"]["clicked"] and not ingredients["pepper"]["clicked"]:
        name = "bowl_rice_onion"
    elif ingredients["onion"]["clicked"] and ingredients["pepper"]["clicked"] and not ingredients["egg"]["clicked"] and not ingredients["jackfruit"]["clicked"] and not ingredients["rice"]["clicked"]:
        name = "bowl_pepper_onion"
    elif ingredients["onion"]["clicked"] and ingredients["pepper"]["clicked"] and ingredients["jackfruit"]["clicked"] and not ingredients["egg"]["clicked"] and not ingredients["rice"]["clicked"]:
        name = "bowl_jackfruit_pepper_onion"
    elif ingredients["onion"]["clicked"] and ingredients["pepper"]["clicked"] and ingredients["jackfruit"]["clicked"] and ingredients["egg"]["clicked"] and not ingredients["rice"]["clicked"]:
        name = "bowl_egg_jackfruit_pepper_onion"
    elif ingredients["onion"]["clicked"] and ingredients["pepper"]["clicked"] and ingredients["jackfruit"]["clicked"] and ingredients["egg"]["clicked"] and ingredients["rice"]["clicked"]:
        name = "bowl_rice_egg_jackfruit_pepper_onion"
    elif ingredients["onion"]["clicked"] and ingredients["pepper"]["clicked"] and ingredients["jackfruit"]["clicked"] and ingredients["rice"]["clicked"] and not ingredients["egg"]["clicked"]:
        name = "bowl_rice_jackfruit_pepper_onion"
    elif ingredients["onion"]["clicked"] and ingredients["pepper"]["clicked"] and ingredients["jackfruit"]["clicked"] and ingredients["rice"]["clicked"] and not ingredients["egg"]["clicked"]:
        name = "bowl_egg_pepper_onion"
    elif ingredients["onion"]["clicked"] and ingredients["pepper"]["clicked"] and ingredients["egg"]["clicked"] and not ingredients["rice"]["clicked"] and not ingredients["jackfruit"]["clicked"]:
        name = "bowl_egg_pepper_onion"
    elif ingredients["onion"]["clicked"] and ingredients["pepper"]["clicked"] and ingredients["egg"]["clicked"] and ingredients["rice"]["clicked"] and not ingredients["jackfruit"]["clicked"]:
        name = "bowl_rice_egg_pepper_onion"
    elif ingredients["egg"]["clicked"] and ingredients["pepper"]["clicked"] and not ingredients["onion"]["clicked"] and not ingredients["rice"]["clicked"] and not ingredients["jackfruit"]["clicked"]:
        name = "bowl_egg_pepper"
    elif ingredients["jackfruit"]["clicked"] and ingredients["pepper"]["clicked"] and not ingredients["onion"]["clicked"] and not ingredients["rice"]["clicked"] and not ingredients["egg"]["clicked"]:
        name = "bowl_jackfruit_pepper"
    elif ingredients["rice"]["clicked"] and ingredients["pepper"]["clicked"] and not ingredients["onion"]["clicked"] and not ingredients["egg"]["clicked"] and not ingredients["jackfruit"]["clicked"]:
        name = "bowl_rice_pepper"
    elif ingredients["egg"]["clicked"] and ingredients["pepper"]["clicked"] and ingredients["rice"]["clicked"] and not ingredients["onion"]["clicked"] and not ingredients["jackfruit"]["clicked"]:
        name = "bowl_rice_egg_pepper"
    elif ingredients["jackfruit"]["clicked"] and ingredients["pepper"]["clicked"] and ingredients["rice"]["clicked"] and not ingredients["onion"]["clicked"] and not ingredients["egg"]["clicked"]:
        name = "bowl_rice_jackfruit_pepper"
    elif ingredients["jackfruit"]["clicked"] and ingredients["pepper"]["clicked"] and ingredients["egg"]["clicked"] and not ingredients["onion"]["clicked"] and not ingredients["rice"]["clicked"]:
        name = "bowl_egg_jackfruit_pepper"
    elif ingredients["jackfruit"]["clicked"] and ingredients["pepper"]["clicked"] and ingredients["egg"]["clicked"] and ingredients["rice"]["clicked"] and not ingredients["onion"]["clicked"]:
        name = "bowl_rice_egg_jackfruit_pepper"
    elif ingredients["rice"]["clicked"] and ingredients["pepper"]["clicked"] and ingredients["onion"]["clicked"] and ingredients["jackfruit"]["clicked"] and not ingredients["egg"]["clicked"]:
        name = "bowl_rice_jackfruit_pepper_onion"
    elif ingredients["rice"]["clicked"] and ingredients["pepper"]["clicked"] and ingredients["onion"]["clicked"] and not ingredients["jackfruit"]["clicked"] and not ingredients["egg"]["clicked"]:
        name = "bowl_rice_pepper_onion"
    else:
        name = bowl_name
    return name

def on_mouse_down(pos):
    global fire_on, fire_on_rect, clicked_ingredients, bowl_name, fire_timer
    for name, ingredient in ingredients.items():
        if ingredient["image"].collidepoint(pos) and not ingredient["clicked"] and fire_timer > 0:
            ingredient["clicked"] = True
            clicked_ingredients.append(name)
            bowl_name += "_" + name
    bowl_name = update_bowl_name(bowl_name)
    if fire_timer > 0:
        if fire_on_rect.collidepoint(pos):
            fire_on = True
    for side in sides.values():
        if side["image"].collidepoint(pos):
            side["clicked"] = True
    if fire_timer == 0:
        if play_agian["yes"][0].collidepoint(pos):
            reset_or_end_game(True)
        if play_agian["no"][0].collidepoint(pos):
            reset_or_end_game(False)
    
def update_fire_timer():
    global fire_timer, fire_on
    if fire_on and fire_timer > 0:
        fire_timer -= 1

clock.schedule_interval(update_fire_timer, 1)

pgzrun.go()
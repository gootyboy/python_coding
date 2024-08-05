import pgzrun
import time
import pygame
from pgzero.actor import Actor
import random

WIDTH = 800
HEIGHT = 600

box_index = 0
settings_width = 451
settings_height = 451
settings_x = 70
settings_y = 76

key_pressed = None
icon_clicked = None

screen_clicked = False
password_done = False
digit_correct_list = [False, False, False, False, False, False, False, False]
on_home_page = False
setting_rect_open = False
windows_rect_open = False
backround_icon_open = False
settings_rect_full_screen = False

windows_rect = pygame.Rect(70, 200, 351, 312)

setting_icon = Actor("setting-icon", pos=(450, 570))

windows_icon = Actor("windows-icon", pos=(400, 572))

power_off = Actor("power-button", pos=(405, 500))

backround_icon = Actor("backround-setting", pos=(270, 150))

x_button_1 = Actor("x-button", pos=(500, 93))

x_button_2 = Actor("x-button", pos=(405, 210))

full_screen_icon_1 = Actor("full-screen-icon", pos=(465, 93))

full_screen_icon_2 = Actor("full-screen-icon", pos=(365, 210))

garden_icon = Actor("garden-background-icon", pos=(400, 250))

sky_icon = Actor("sky-background-icon", pos=(200, 250))

dungeon_icon = Actor("dungeon-background-icon", pos=(200, 400))

stage_icon = Actor("stage-background-icon", pos=(400, 400))

def create_password_coding_digits():
    global a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, q, w, x, y, z
    a = random.randint(random.randint(0, 50), random.randint(50, 150))
    b = random.randint(random.randint(0, 50), random.randint(50, 150))
    c = random.randint(random.randint(0, 50), random.randint(50, 150))
    d = random.randint(random.randint(0, 50), random.randint(50, 150))
    e = random.randint(random.randint(0, 50), random.randint(50, 150))
    f = random.randint(random.randint(0, 50), random.randint(50, 150))
    g = random.randint(random.randint(0, 50), random.randint(50, 150))
    h = random.randint(random.randint(0, 50), random.randint(50, 150))
    i = random.randint(random.randint(0, 50), random.randint(50, 150))
    j = random.randint(random.randint(0, 50), random.randint(50, 150))
    k = random.randint(random.randint(0, 50), random.randint(50, 150))
    l = random.randint(random.randint(0, 50), random.randint(50, 150))
    m = random.randint(random.randint(0, 50), random.randint(50, 150))
    n = random.randint(random.randint(0, 50), random.randint(50, 150))
    o = random.randint(random.randint(0, 50), random.randint(50, 150))
    p = random.randint(random.randint(0, 50), random.randint(50, 150))
    q = random.randint(random.randint(0, 50), random.randint(50, 150))
    r = random.randint(random.randint(0, 50), random.randint(50, 150))
    s = random.randint(random.randint(0, 50), random.randint(50, 150))
    t = random.randint(random.randint(0, 50), random.randint(50, 150))
    u = random.randint(random.randint(0, 50), random.randint(50, 150))
    v = random.randint(random.randint(0, 50), random.randint(50, 150))
    w = random.randint(random.randint(0, 50), random.randint(50, 150))
    x = random.randint(random.randint(0, 50), random.randint(50, 150))
    y = random.randint(random.randint(0, 50), random.randint(50, 150))
    z = random.randint(random.randint(0, 50), random.randint(50, 150))

create_password_coding_digits()

password_coding = {
    "a": bin(a)[2:],
    "b": bin(b)[2:],
    "c": bin(c)[2:],
    "d": bin(d)[2:],
    "e": bin(e)[2:],
    "f": bin(f)[2:],
    "g": bin(g)[2:],
    "h": bin(h)[2:],
    "i": bin(i)[2:],
    "j": bin(j)[2:],
    "k": bin(k)[2:],
    "l": bin(l)[2:],
    "m": bin(m)[2:],
    "n": bin(n)[2:],
    "o": bin(o)[2:],
    "p": bin(p)[2:],
    "q": bin(q)[2:],
    "r": bin(r)[2:],
    "s": bin(s)[2:],
    "t": bin(t)[2:],
    "u": bin(u)[2:],
    "v": bin(v)[2:],
    "w": bin(w)[2:],
    "x": bin(x)[2:],
    "y": bin(y)[2:],
    "z": bin(z)[2:],
}

def get_letter_from_number(digits, index_of_item):
    for letter, number in password_coding.items():
        if str(number) == digits[index_of_item]:
            return letter

def decode_password(digits):
    one_to_4 = [get_letter_from_number(digits, 0), get_letter_from_number(digits, 1), get_letter_from_number(digits, 2), get_letter_from_number(digits, 3)]
    print(one_to_4 + [get_letter_from_number(digits, 4), get_letter_from_number(digits, 5), get_letter_from_number(digits, 6), get_letter_from_number(digits, 7)])
    return one_to_4 + [get_letter_from_number(digits, 4), get_letter_from_number(digits, 5), get_letter_from_number(digits, 6), get_letter_from_number(digits, 7)]

def check_if_digits_are_letters(digits):
    digits_is_letter_list = [False, False, False, False, False, False, False, False]
    for i in range(0, 8):
        if digits[i].isalpha():
            digits_is_letter_list[i] = True
    return digits_is_letter_list

def check_if_numbers_are_in_range(digits):
    return True

def check_if_digits_are_coded(digits):
    try:
        for digit in digits:
            digit_int = int(digit)
        return True
    except ValueError:
        return False

def make_password_coded(digits):
    coded_digits_1_to_4 = [password_coding[digits[0]], password_coding[digits[1]], password_coding[digits[2]],password_coding[digits[3]]]
    coded_digits_5_to_8 = [password_coding[digits[4]], password_coding[digits[5]], password_coding[digits[6]], password_coding[digits[7]]]
    coded_digits = coded_digits_1_to_4 + coded_digits_5_to_8
    filename = r"C:\Projects\boy\pygame_game\computer-game\password.txt"
    with open(filename, "w") as file:
        for coded_digit in coded_digits:
            file.write(str(coded_digit) + " ")

def get_error_places(digits):
    error_places = []
    for index, value in enumerate(digits):
        if value == False:
            if index == 1:
                error_places.append(str(index + 1) + "st")
            elif index == 2:
                error_places.append(str(index + 1) + "nd")
            elif index == 3:
                error_places.append(str(index + 1) + "rd")
            else:
                error_places.append(str(index + 1) + "th")
    return error_places

def get_password_digits():
    filename = r"C:\Projects\boy\pygame_game\computer-game\password.txt"
    with open(filename, "r") as file:
        line = file.readline()
        password_digits_coded = line.split()
        coded = check_if_digits_are_coded(password_digits_coded)
        if coded:
            numbers_in_range = check_if_numbers_are_in_range(password_digits_coded)
            if numbers_in_range:
                password_digits = decode_password(password_digits_coded)
                return ["p", "a", "s", "s", "w", "o", "r", "d"]
            else:
                print("TypeError in the password.txt file")
                print("Numbers provided for coded password is out of range. Please type numbers in the range (1 to 26) or type letters")
                pgzrun.sys.exit()
        else:
            digits_are_letters = check_if_digits_are_letters(password_digits_coded)
            if all(digits_are_letters):
                password_digits = password_digits_coded
                make_password_coded(password_digits)
                return password_digits
            else:
                error_places = get_error_places(digits_are_letters)
                print("TypeError in the password.txt file")
                print(f"digits provided for password digits are not all letters. The error is in the {error_places} digit")
                print("Please type letters or type the coded password with numbers")
                pgzrun.sys.exit()

def get_backround():
    global backround_image,blurred_backround_image
    filename = r"C:\Projects\boy\pygame_game\computer-game\background-setting.txt"
    with open(filename, "r") as file:
        line = file.readline()
        background_images = line.split()
        backround_image = background_images[0]
        blurred_backround_image = background_images[1]

def update_background(background):
    global backround_image,blurred_backround_image
    filename = r"C:\Projects\boy\pygame_game\computer-game\background-setting.txt"
    with open(filename, "w") as file:
        file.write(background + " " + background + "-blurred")

def get_answer_boxes():    
    global password_boxes_x
    password_boxes_x = [276, 306, 336, 366, 396, 426, 456, 486]
    password_boxes_1_to_4 = [pygame.Rect(276, 300, 43, 43), pygame.Rect(306, 300, 43, 43), pygame.Rect(336, 300, 43, 43), pygame.Rect(366, 300, 43, 43)]
    password_boxes_5_to_8 = [pygame.Rect(396, 300, 43, 43), pygame.Rect(426, 300, 43, 43), pygame.Rect(456, 300, 43, 43), pygame.Rect(486, 300, 43, 43)]
    password_boxes = password_boxes_1_to_4 + password_boxes_5_to_8
    return password_boxes

def draw_answer_boxes():
    global password_digits, password_boxes
    password_boxes = get_answer_boxes()
    for box in password_boxes:
        screen.draw.filled_rect(box, "sky blue")
    screen.draw.text("Password", color= "black", center = (WIDTH / 2, 250), fontsize = 60)

def get_x_of_circles():
    return [297.5, 327.5, 357.5, 387.5, 417.5, 447.5, 477.5, 507.5]

def draw_home_screen():
    screen.draw.filled_rect(pygame.Rect(0, 550, WIDTH, 50), (212,226,249))
    setting_icon.draw()
    windows_icon.draw()

def start_home_page():
    global settings_rect_full_screen
    draw_home_screen()
    if setting_rect_open:
        screen.draw.filled_rect(settings_rect, (239,244,249))
        x_button_1.draw()
        if not settings_rect_full_screen:
            full_screen_icon_1.draw()
        if backround_icon_open:
            backround_icon.draw()
        elif not backround_icon_open and icon_clicked == "background":
            screen.draw.text("Images", color= "black", center=(270, 170), fontsize = 30)
            sky_icon.draw()
            garden_icon.draw()
            dungeon_icon.draw()
            stage_icon.draw()
    if windows_rect_open:
        screen.draw.filled_rect(windows_rect, "gray")
        x_button_2.draw()
        power_off.draw()
        full_screen_icon_2.draw()

def rect_full_screen(rect):
    global settings_width, settings_height, settings_x, settings_y
    if rect == "settings":
        settings_width = WIDTH
        settings_height = HEIGHT - 50
        settings_x = 0
        settings_y = 0

def draw():
    global screen_clicked, box_index, key_pressed, password_boxes_x,digit_correct_list, on_home_page, password_done, setting_rect_open, backround_icon_open
    global settings_rect, settings_x, settings_y, settings_width, settings_height
    settings_rect = pygame.Rect(settings_x, settings_x, settings_width, settings_height)    
    get_backround()
    password_digits = get_password_digits()
    time_now = time.localtime()
    time_minutes = time.strftime("%M", time_now)
    time_hours = time.strftime("%I", time_now).lstrip("0")
    if screen_clicked == False:
        screen.blit(backround_image, (0, 0)) 
    if screen_clicked and not password_done:
        screen.blit(blurred_backround_image, (0, 0))
        draw_answer_boxes()
        circles_x = get_x_of_circles()
        circle_y = 300 + (43 / 2)
        for i in range(0, 8):
            if box_index > i:
                screen.draw.filled_circle((circles_x[i], circle_y), 10, "black")
    if screen_clicked == False and on_home_page == False:
        if backround_image == "stage":
            screen.draw.text(f"{time_hours}:{time_minutes}", color="dark gray", center=(WIDTH / 2, 50), fontsize=100)
        else:
            screen.draw.text(f"{time_hours}:{time_minutes}", color="black", center=(WIDTH / 2, 50), fontsize=100)
    if screen_clicked == True and key_pressed != None and password_done == False:
        screen.draw.textbox(key_pressed, password_boxes[box_index], color= "black")
        if box_index >= 0 and  box_index<=8 and key_pressed == password_digits[box_index]:
            digit_correct_list[box_index] = True   
        key_pressed = None
    if password_done == True and all(digit_correct_list):
        screen_clicked = False
        on_home_page = True
    elif password_done == True:
        screen_clicked = True
        password_done = False
        box_index = 0
        digit_correct_list = [False, False, False, False, False, False, False, False]
    if on_home_page:
        start_home_page()
                                
def on_key_up():
    global box_index, key_pressed, password_done, password_digits,digit_1

    if box_index < 7:
        box_index += 1
    else:
        password_done = True

def check_for_background_pressed(pos):
    global icon_clicked
    if sky_icon.collidepoint(pos) and icon_clicked == "background":
        update_background("sky")
        icon_clicked = None
    if garden_icon.collidepoint(pos) and icon_clicked == "background":
        update_background("garden")
        icon_clicked = None
    if dungeon_icon.collidepoint(pos) and icon_clicked == "background":
        update_background("dungeon")
        icon_clicked = None
    if stage_icon.collidepoint(pos) and icon_clicked == "background":
        update_background("stage")
        icon_clicked = None

def check_for_other_icons_pressed(pos):
    global on_home_page, setting_rect_open, backround_icon_open, backround_image, icon_clicked, windows_rect_open, settings_rect_full_screen
    if setting_icon.collidepoint(pos):
        setting_rect_open = True
    if windows_icon.collidepoint(pos):
        windows_rect_open = True
    if x_button_1.collidepoint(pos):
        setting_rect_open = False
        backround_icon_open = False
    if x_button_2.collidepoint(pos):
        windows_rect_open = False
    if power_off.collidepoint(pos) and windows_rect_open:
        pgzrun.sys.exit()
    if full_screen_icon_1.collidepoint(pos) and setting_rect_open:
        rect_full_screen("settings")
        settings_rect_full_screen = True
    if full_screen_icon_1.collidepoint(pos) and windows_rect_open:
        pass
    
def on_mouse_down(pos, button):
    global screen_clicked, on_home_page, setting_rect_open, backround_icon_open, backround_image, icon_clicked, windows_rect_open
    if on_home_page == False:
        screen_clicked = True
    elif on_home_page and button == mouse.LEFT:
        if backround_icon.collidepoint(pos) and backround_icon_open:
            backround_icon_open = False
            icon_clicked = "background"
        else:
            backround_icon_open = True
        check_for_background_pressed(pos)
        check_for_other_icons_pressed(pos)

def get_letter_pressed():
    keys = {
    keyboard.q: "q",
    keyboard.w: "w",
    keyboard.e: "e",
    keyboard.r: "r",
    keyboard.t: "t",
    keyboard.y: "y",
    keyboard.u: "u",
    keyboard.i: "i",
    keyboard.o: "o",
    keyboard.p: "p",
    keyboard.a: "a",
    keyboard.s: "s",
    keyboard.d: "d",
    keyboard.f: "f",
    keyboard.g: "g",
    keyboard.h: "h",
    keyboard.j: "j",
    keyboard.k: "k",
    keyboard.l: "l",
    keyboard.z: "z",
    keyboard.x: "x",
    keyboard.c: "c",
    keyboard.v: "v",
    keyboard.b: "b",
    keyboard.n: "n",
    keyboard.m: "m"
}
    for key, letter in keys.items():
        if key:
            return letter

def update():
    global key_pressed, change_password_key_pressed
    if not password_done and screen_clicked:
        key_pressed = get_letter_pressed()

pgzrun.go()
import pgzrun
import tkinter
from pgzero.rect import Rect
from tkinter import simpledialog

WIDTH = 800
HEIGHT = 600

DRAW_TEXT_TIME = 5

rects = {
        "topleft": {"rect": Rect(10, 10, WIDTH / 3 - 10, HEIGHT / 3 - 10),
                     "clicked": False}, 
         "topcenter": {"rect": Rect(WIDTH / 3 + 10, 10, WIDTH / 3 - 10, HEIGHT / 3 - 10), 
                       "clicked": False}, 
         "topright": {"rect": Rect(WIDTH * 2 / 3 + 10, 10, WIDTH / 3 - 10, HEIGHT / 3 - 10),
                      "clicked": False},
         "centerleft": {"rect": Rect(10, HEIGHT / 3 + 10, WIDTH / 3 - 10, HEIGHT / 3 - 10),
                        "clicked": False}, 
         "center": {"rect": Rect(WIDTH / 3 + 10, HEIGHT / 3 + 10, WIDTH / 3 - 10, HEIGHT / 3 - 10),
                    "clicked": False}, 
         "centerright": {"rect": Rect(WIDTH * 2 / 3 + 10, HEIGHT / 3 + 10, WIDTH / 3 - 10, HEIGHT / 3 - 10),
                         "clicked": False},
         "bottomleft": {"rect": Rect(10, HEIGHT * 2 / 3 + 10, WIDTH / 3 - 10, HEIGHT / 3 - 10),
                        "clicked": False}, 
         "bottomcenter": {"rect": Rect(WIDTH / 3 + 10, HEIGHT * 2 / 3 + 10, WIDTH / 3 - 10, HEIGHT / 3 - 10),
                          "clicked": False}, 
         "bottomright": {"rect": Rect(WIDTH * 2 / 3 + 10, HEIGHT * 2 / 3 + 10, WIDTH / 3 - 10, HEIGHT / 3 - 10),
                         "clicked": False}
}

player_one_turn = True
times_ran = 0

index_clicked = []
player_one_name = None
player_two_name = None

winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

draw_rects = []
draw_time = 0

turn_message_printed = False
screen_clicked = True

def screeninput(title, prompt):
    root = tkinter.Tk()
    root.withdraw()
    user_input = simpledialog.askstring(title, prompt)
    root.destroy()
    return user_input

def ask_names():
    global player_one_name, player_two_name, index_clicked
    player_one_name = screeninput("Player 1: \"O\"", "Enter your name. You are player one. You will be \"O\"")
    player_two_name = screeninput("Player 2: \"X\"", "Enter your name. You are player two. You will be \"X\"")

def draw_text(text):
    screen.draw.text(str(text), fontsize=200, center=(WIDTH / 2, HEIGHT / 2), color=(0, 0, 0))

def draw():
    global player_one_name, player_two_name, rects, player_one_turn, times_ran, turn_message_printed,draw_rects, screen_clicked,draw_time
    screen.fill("white")
    if player_one_name == None and player_two_name == None:
        ask_names()
    else:
        screen.draw.line((WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 'black')
        screen.draw.line((2 * WIDTH / 3, 0), (2 * WIDTH / 3, HEIGHT), 'black')
        screen.draw.line((0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 'black')
        screen.draw.line((0, 2 * HEIGHT / 3), (WIDTH, 2 * HEIGHT / 3), 'black')
        if not turn_message_printed:
            if player_one_turn:
                draw_text(f"{player_one_name}'s turn")
            else:
                draw_text(f"{player_two_name}'s turn")
            turn_message_printed = True
        for draw_rect in draw_rects:
            if not screen_clicked:
                screen.draw.textbox(f"|__|", rects[draw_rect], color="black")
        for i in range(0, len(index_clicked)):
            if len(index_clicked) > i:
                if i % 2 == 0:
                    screen.draw.textbox("X", rects[index_clicked[i]["rect"]], color=(0, 0, 0))
                    player_one_turn = False
                else:
                    screen.draw.textbox("O", rects[index_clicked[i]["rect"]], color=(0, 0, 0))
                    player_one_turn = True

def on_mouse_down(pos):
    global draw_rects, screen_clicked,draw_time
    screen_clicked = False
    for i in rects:
        if rects[i]["rect"].collidepoint(pos):
            draw_rects.clear()
            draw_rects.append(i)

def on_mouse_up(pos):
    global index_clicked, turn_message_printed, screen_clicked
    screen_clicked = True
    if player_one_name == None and player_two_name == None:
        pass
    else:
        for i in rects:
            if rects[i]["rect"].collidepoint(pos):
                if i not in index_clicked:
                    index_clicked.append(i)
                    turn_message_printed = False
                    if check_winner():
                        if player_one_turn:
                            draw_text(f"{player_one_name} wins!")
                        else:
                            draw_text(f"{player_two_name} wins!")
                        play_agian()
                        if play_agian == "yes":
                            pgzrun.go()
                        else:
                            pgzrun.sys.exit()
                        break
                elif len(index_clicked) == 9:
                    draw_text("It's a tie!")
                    play_agian()
                    break

def check_winner():
    for win_combo in winning_combinations:
        if all(index in index_clicked for index in win_combo):
            if index_clicked.index(win_combo[0]) % 2 == index_clicked.index(win_combo[1]) % 2 == index_clicked.index(win_combo[2]) % 2:
                return True
    else:
        return False

def play_agian():
    while True:
        print(" ")
        play_agian = screeninput("Play Agian","Would you like to play agian. Enter \"yes\" or \"no\"")
        if play_agian == "yes" or play_agian == "no":
            break
    if play_agian == "yes":
        pgzrun.go()
    else:
        pgzrun.sys.exit()
    return

def update():
    pass

pgzrun.go()
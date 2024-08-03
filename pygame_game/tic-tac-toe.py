import pgzrun
from pgzero.rect import Rect

WIDTH = 800
HEIGHT = 600

# Top three rectangles
top_left_rect = Rect(10, 10, WIDTH / 3 - 10, HEIGHT / 3 - 10)
top_center_rect = Rect(WIDTH / 3 + 10, 10, WIDTH / 3 - 10, HEIGHT / 3 - 10)
top_right_rect = Rect(WIDTH * 2 / 3 + 10, 10, WIDTH / 3 - 10, HEIGHT / 3 - 10)

# Center three rectangles
center_left_rect = Rect(10, HEIGHT / 3 + 10, WIDTH / 3 - 10, HEIGHT / 3 - 10)
center_rect = Rect(WIDTH / 3 + 10, HEIGHT / 3 + 10, WIDTH / 3 - 10, HEIGHT / 3 - 10)
center_right_rect = Rect(WIDTH * 2 / 3 + 10, HEIGHT / 3 + 10, WIDTH / 3 - 10, HEIGHT / 3 - 10)

# Bottom three rectangles
bottom_left_rect = Rect(10, HEIGHT * 2 / 3 + 10, WIDTH / 3 - 10, HEIGHT / 3 - 10)
bottom_center_rect = Rect(WIDTH / 3 + 10, HEIGHT * 2 / 3 + 10, WIDTH / 3 - 10, HEIGHT / 3 - 10)
bottom_right_rect = Rect(WIDTH * 2 / 3 + 10, HEIGHT * 2 / 3 + 10, WIDTH / 3 - 10, HEIGHT / 3 - 10)

rects = [top_left_rect, top_center_rect, top_right_rect, center_left_rect, center_rect, center_right_rect, bottom_left_rect, bottom_center_rect, bottom_right_rect]

stop_printing_player_turn = False

player_one_turn = True
times_ran = 0

index_clicked = []
player_one_name = None
player_two_name = None

# Define winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

# Flag to track if the turn message has been printed
turn_message_printed = False

def ask_names():
    global player_one_name, player_two_name, index_clicked
    player_one_name = input("Enter your name. You are player one. You will be \"O\"")
    player_two_name = input("Enter your name. You are player two. You will be \"X\"")
    print("Please click in the center of the place you want to put an \"X\" or an \"O\"")

def draw():
    global player_one_name, player_two_name, stop_printing_player_turn, rects, player_one_turn, times_ran, turn_message_printed
    screen.fill("white")
    if player_one_name == None and player_two_name == None:
        screen.draw.text("Click to enter your", color="black", center=(WIDTH / 2, HEIGHT / 4), fontsize=100)
        screen.draw.text("name in the console", color="black", center=(WIDTH / 2, HEIGHT / 2), fontsize=100)
    else:
        screen.draw.line((WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 'black')
        screen.draw.line((2 * WIDTH / 3, 0), (2 * WIDTH / 3, HEIGHT), 'black')
        screen.draw.line((0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 'black')
        screen.draw.line((0, 2 * HEIGHT / 3), (WIDTH, 2 * HEIGHT / 3), 'black')
        if not turn_message_printed:
            if player_one_turn:
                print(f"{player_one_name}'s turn")
            else:
                print(f"{player_two_name}'s turn")
            turn_message_printed = True
        for rect in rects:
            screen.draw.filled_rect(rect, (255, 255, 255))
        for i in range(0, len(index_clicked)):
            if len(index_clicked) > i:
                if i % 2 == 0:
                    screen.draw.textbox("X", rects[index_clicked[i]], color=(0, 0, 0))
                    stop_printing_player_turn = False
                    player_one_turn = False
                else:
                    screen.draw.textbox("O", rects[index_clicked[i]], color=(0, 0, 0))
                    stop_printing_player_turn = False
                    player_one_turn = True

def on_mouse_down(pos):
    global index_clicked, turn_message_printed
    if player_one_name == None and player_two_name == None:
        ask_names()
    else:
        for i in range(0, len(rects)):
            if rects[i].collidepoint(pos):
                if i not in index_clicked:
                    index_clicked.append(i)
                    turn_message_printed = False
                    if check_winner():
                        if player_one_turn:
                            print(f"{player_one_name} wins!")
                        else:
                            print(f"{player_two_name} wins!")
                        while True:
                            print(" ")
                            play_agian = input("Would you like to play agian. Enter \"yes\" or \"no\"")
                            if play_agian == "yes" or play_agian == "no":
                                break
                        if play_agian == "yes":
                            pgzrun.go()
                        else:
                            pgzrun.sys.exit()
                elif len(index_clicked) == 9:
                    print("It's a tie!")
                    while True:
                        print(" ")
                        play_agian = input("Would you like to play agian. Enter \"yes\" or \"no\"")
                        if play_agian == "yes" or play_agian == "no":
                            break
                    if play_agian == "yes":
                        pgzrun.go()
                    else:
                        pgzrun.sys.exit()

def check_winner():
    for win_combo in winning_combinations:
        if all(index in index_clicked for index in win_combo):
            if index_clicked.index(win_combo[0]) % 2 == index_clicked.index(win_combo[1]) % 2 == index_clicked.index(win_combo[2]) % 2:
                return True
    return False

def update():
    pass

pgzrun.go()
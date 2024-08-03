import pgzrun
from pgzero.rect import Rect

WIDTH = 800
HEIGHT = 600

#top three rectangles
top_left_rect = Rect(10, 10, WIDTH / 3 - 10, HEIGHT / 3 - 10)
top_center_rect = Rect(WIDTH / 3 + 10, 10, WIDTH / 3 - 10, HEIGHT / 3 - 10)
top_right_rect = Rect(WIDTH * 2 / 3 + 10, 10, WIDTH / 3 - 10, HEIGHT / 3 - 10)

#centet three rectangles
center_left_rect = Rect(10, HEIGHT / 3 + 10, WIDTH / 3 - 10, HEIGHT / 3 - 10)
center_rect = Rect(WIDTH / 3 + 10, HEIGHT / 3 + 10, WIDTH / 3 - 10, HEIGHT / 3 - 10)
center_right_rect = Rect(WIDTH * 2 / 3 + 10, HEIGHT / 3 + 10, WIDTH / 3 - 10, HEIGHT / 3 - 10)

#bottom three rectangles
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

def ask_names():
    global player_one_name, player_two_name, index_clicked
    player_one_name = input("Enter your name. You are player one. You will be \"O\"")
    player_two_name = input("Enter your name. You are player two. You will be \"X\"")
    print("Please click in the center of the place you want to put an \"X\" or an \"O\"")

def draw():
    global player_one_name, player_two_name, stop_printing_player_turn, rects, player_one_turn, times_ran
    screen.fill("white")
    if player_one_name == None and player_two_name == None:
        screen.draw.text("Click to enter your", color="black", center=(WIDTH / 2, HEIGHT / 4), fontsize=100)
        screen.draw.text("name in the console", color="black", center=(WIDTH / 2, HEIGHT / 2), fontsize=100)
    else:
        screen.draw.line((WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 'black')
        screen.draw.line((2 * WIDTH / 3, 0), (2 * WIDTH / 3, HEIGHT), 'black')
        screen.draw.line((0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 'black')
        screen.draw.line((0, 2 * HEIGHT / 3), (WIDTH, 2 * HEIGHT / 3), 'black')
        if not stop_printing_player_turn:
            if player_one_turn:
                print(f"{player_one_name}'s turn")
            else:
                print(f"{player_two_name}'s turn")
            stop_printing_player_turn = True
        for rect in rects:
            screen.draw.filled_rect(rect, (255, 255, 255))
        for i in range(0, len(index_clicked)):
            if len(index_clicked) > i:
                if i % 2 == 0:
                    screen.draw.textbox("X", rects[index_clicked[i]], color=(0, 0, 0))
                    if times_ran == 0:
                        print(f"{player_one_name}'s turn")
                        times_ran == 1
                else:
                    screen.draw.textbox("O", rects[index_clicked[i]], color=(0, 0, 0))
                    if times_ran == 0:
                        print(f"{player_two_name}'s turn")
                        times_ran == 1

def on_mouse_down(pos):
    global index_clicked
    if player_one_name == None and player_two_name == None:
        ask_names()
    else:
        for i in range(0, len(rects)):
            if rects[i].collidepoint(pos):
                index_clicked.append(i)
    
def update():
    pass

pgzrun.go()
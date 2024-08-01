import pgzrun

WIDTH = 800
HEIGHT = 600

player_one_name = None
player_two_name = None

def ask_names():
    global player_one_name, player_two_name
    player_one_name = input("Enter your name. You are player one. You will be \"O\"")
    player_two_name = input("Enter your name. You are player two. You will be \"X\"")

def draw():
    global player_one_name, player_two_name
    screen.fill("white")
    # Vertical lines
    screen.draw.line((WIDTH // 3, 0), (WIDTH // 3, HEIGHT), 'black')
    screen.draw.line((2 * WIDTH // 3, 0), (2 * WIDTH // 3, HEIGHT), 'black')
    # Horizontal lines
    screen.draw.line((0, HEIGHT // 3), (WIDTH, HEIGHT // 3), 'black')
    screen.draw.line((0, 2 * HEIGHT // 3), (WIDTH, 2 * HEIGHT // 3), 'black')
    if player_one_name == None and player_two_name == None:
        screen.draw.text("Click to enter your", color="black", center=(WIDTH / 2, HEIGHT / 4), fontsize=100)
        screen.draw.text("name in the console", color="black", center=(WIDTH / 2, HEIGHT / 2), fontsize=100)

def on_mouse_down():
    if player_one_name == None and player_two_name == None:
        ask_names()

pgzrun.go()
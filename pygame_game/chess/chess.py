import pgzrun
import random
from pgzero.rect import Rect
from pgzero.actor import Actor

WIDTH = 800
HEIGHT = WIDTH
BOX_SIZE = 90
OUTER_EDGE = 50

WHITE_PAWN_Y = HEIGHT - (BOX_SIZE * 3 / 2) - OUTER_EDGE + 5
BLACK_PAWN_Y = (BOX_SIZE * 5 / 2) - OUTER_EDGE
WHITE_ROOK_Y = HEIGHT - (BOX_SIZE / 2) - OUTER_EDGE + 10
BLACK_ROOK_Y = (BOX_SIZE / 2) + OUTER_EDGE - 10
WHITE_QUEEN_Y = HEIGHT - (BOX_SIZE / 2) - OUTER_EDGE + 10
BLACK_QUEEN_Y = (BOX_SIZE / 2) + OUTER_EDGE - 10
WHITE_KING_Y = HEIGHT - (BOX_SIZE / 2) - OUTER_EDGE + 10
BLACK_KING_Y = (BOX_SIZE / 2) + OUTER_EDGE - 10

CIRCLE_RADIUS = 75

black_top_rect = Rect(WIDTH / 2 - 200 - CIRCLE_RADIUS, HEIGHT / 2 - CIRCLE_RADIUS, CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2)
black_bottom_rect = Rect(WIDTH / 2 + 200 - CIRCLE_RADIUS, HEIGHT / 2 - CIRCLE_RADIUS, CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2)
black_random_rect = Rect(WIDTH / 2 - CIRCLE_RADIUS, HEIGHT / 2 - CIRCLE_RADIUS, CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2)
game_started = False

colors_reversed = random.choice([True, False])

def create_piece(num, color, name):
    if name == "pawn":
        return Actor(color + "_" + name, (OUTER_EDGE + (BOX_SIZE * (num - 1)) + (BOX_SIZE / 2), BLACK_PAWN_Y if (color == "black") != colors_reversed else WHITE_PAWN_Y))
    elif name == "rook":
        return Actor(color + "_" + name, (OUTER_EDGE + (0 if num == 1 else BOX_SIZE * 7) + (BOX_SIZE / 2), BLACK_ROOK_Y if (color == "black") != colors_reversed else WHITE_ROOK_Y))
    elif name == "knight":
        return Actor(color + "_" + name, (OUTER_EDGE + (BOX_SIZE * (1 if num == 1 else 6)) + (BOX_SIZE / 2), BLACK_ROOK_Y if (color == "black") != colors_reversed else WHITE_ROOK_Y))
    elif name == "bishop":
        return Actor(color + "_" + name, (OUTER_EDGE + (BOX_SIZE * (2 if num == 1 else 5)) + (BOX_SIZE / 2), BLACK_ROOK_Y if (color == "black") != colors_reversed else WHITE_ROOK_Y))
    elif name == "queen":
        return Actor(color + "_" + name, (OUTER_EDGE + (BOX_SIZE * 3.5), BLACK_QUEEN_Y if (color == "black") != colors_reversed else WHITE_QUEEN_Y))
    elif name == "king":
        return Actor(color + "_" + name, (OUTER_EDGE + (BOX_SIZE * 4.5), BLACK_KING_Y if (color == "black") != colors_reversed else WHITE_KING_Y))

def create_chess_pieces():
    pieces = {f"{color}_pawn_{num}": create_piece(num, color, "pawn") for color in ["white", "black"] for num in range(1, 9)}
    pieces.update({
        "white_rook_1": create_piece(1, "white", "rook"),
        "white_rook_2": create_piece(2, "white", "rook"),
        "black_rook_1": create_piece(1, "black", "rook"),
        "black_rook_2": create_piece(2, "black", "rook"),
        "white_knight_1": create_piece(1, "white", "knight"),
        "white_knight_2": create_piece(2, "white", "knight"),
        "black_knight_1": create_piece(1, "black", "knight"),
        "black_knight_2": create_piece(2, "black", "knight"),
        "white_bishop_1": create_piece(1, "white", "bishop"),
        "white_bishop_2": create_piece(2, "white", "bishop"),
        "black_bishop_1": create_piece(1, "black", "bishop"),
        "black_bishop_2": create_piece(2, "black", "bishop"),
        "white_queen": create_piece(1, "white", "queen"),
        "black_queen": create_piece(1, "black", "queen"),
        "white_king": create_piece(1, "white", "king"),
        "black_king": create_piece(1, "black", "king")
    })
    return pieces

def set_up_board():
    screen.blit("chess_board", (0, 0))
    for piece in pieces.values():
        piece.draw()

def draw():
    screen.fill("white")
    screen.draw.text("Where would you like black?", center=(WIDTH / 2, HEIGHT / 2 - 100), fontsize=75, color="black")
    screen.draw.filled_circle((WIDTH / 2 - 200, HEIGHT / 2), CIRCLE_RADIUS, "green")
    screen.draw.filled_circle((WIDTH / 2 + 200, HEIGHT / 2), CIRCLE_RADIUS, "red")
    screen.draw.filled_circle((WIDTH / 2, HEIGHT / 2), CIRCLE_RADIUS, "blue")
    screen.draw.textbox("Top", black_top_rect, color="black")
    screen.draw.textbox("Bottom", black_bottom_rect, color="black")
    screen.draw.textbox("Random", black_random_rect, color="black")
    
    if game_started:
        set_up_board()
        set_up_board()

def update():
    pass

def is_path_clear(piece, y):
    for p in pieces.values():
        if p != piece and p.collidepoint((piece.x, y)):
            return False
    return True

def check_for_box_collisions(pos):
    global game_started, colors_reversed, pieces
    if black_bottom_rect.collidepoint(pos):
        game_started = True
        colors_reversed = True
        pieces = create_chess_pieces()
    elif black_top_rect.collidepoint(pos):
        game_started = True
        colors_reversed = False
        pieces = create_chess_pieces()
    elif black_random_rect.collidepoint(pos):
        game_started = True
        colors_reversed = random.choice([True, False])
        pieces = create_chess_pieces()

def check_for_piece_collision(pos):
    for name, piece in pieces.items():
        if piece.collidepoint(pos):
            moving_direction = -BOX_SIZE if (name.startswith("white") != colors_reversed) else BOX_SIZE
            new_y = piece.y + moving_direction
            if "pawn" in name and OUTER_EDGE + BOX_SIZE - 10 < piece.y < HEIGHT - OUTER_EDGE - BOX_SIZE + 10:
                if is_path_clear(piece, new_y):
                    piece.y = new_y
            elif "rook" in name or "knight" in name or "bishop" in name or "queen" in name or "king" in name:
                if is_path_clear(piece, new_y):
                    piece.y = new_y

def on_mouse_up(pos):
    global colors_reversed, game_started, pieces
    if game_started:
        check_for_piece_collision(pos)
    else:
        check_for_box_collisions(pos)

pgzrun.go()
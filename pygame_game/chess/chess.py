import pgzrun
from pgzero.actor import Actor

WIDTH = 800
HEIGHT = WIDTH + 11
BOX_SIZE = 90
OUTER_EDGE_HORZ = 50
OUTER_EDGE_VER = 50
WHITE_PAWN_Y = HEIGHT - (BOX_SIZE * 3 / 2) - OUTER_EDGE_VER
BLACK_PAWN_Y = (BOX_SIZE * 5 / 2) - OUTER_EDGE_VER

def create_pawn(pawn_num, pawn_color):
    return Actor(pawn_color + "_pawn", (OUTER_EDGE_HORZ + (BOX_SIZE * (pawn_num - 1)) + (BOX_SIZE / 2), BLACK_PAWN_Y if pawn_color == "black" else WHITE_PAWN_Y))

pieces = {
    "white_pawn_1": create_pawn(1, "white"),
    "white_pawn_2": create_pawn(2, "white"),
    "white_pawn_3": create_pawn(3, "white"),
    "white_pawn_4": create_pawn(4, "white"),
    "white_pawn_5": create_pawn(5, "white"),
    "white_pawn_6": create_pawn(6, "white"),
    "white_pawn_7": create_pawn(7, "white"),
    "white_pawn_8": create_pawn(8, "white"),
    "black_pawn_1": create_pawn(1, "black"),
    "black_pawn_2": create_pawn(2, "black"),
    "black_pawn_3": create_pawn(3, "black"),
    "black_pawn_4": create_pawn(4, "black"),
    "black_pawn_5": create_pawn(5, "black"),
    "black_pawn_6": create_pawn(6, "black"),
    "black_pawn_7": create_pawn(7, "black"),
    "black_pawn_8": create_pawn(8, "black")
}

def draw_chess_board():
    screen.blit("chess_board", (0, 0))

def draw_chess_pieces():
    for piece_name, piece in pieces.items():
        piece.draw()

def draw():
    draw_chess_board()
    draw_chess_pieces()

def update():
    pass

pgzrun.go()

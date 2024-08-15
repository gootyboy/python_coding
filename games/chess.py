import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
pieces = ["pawn", "rook", "queen", "king", "bishop", "knight (horse)"]
places_letters = [letters[random.randint(0, 7)], letters[random.choice[0, 7]], letters[3]]
random_piece = random.choice(pieces)
if random_piece == pieces[0]:
    letter_of_piece = letters[random.randint(0, 7)]
    number_of_piece = 2
elif random_piece == "rook":
    letter_of_piece = letters[random.choice[0, 7]]
    number_of_piece = 1
elif random_piece == "queen":
    letter_of_piece = letters[3]
    number_of_piece = 1
elif random_piece == "king":
    letter_of_piece = letters[4]
    number_of_piece = 1
elif random_piece == "bishop":
    letter_of_piece = letters[random.choice[0, 7]]
    number_of_piece = 1
elif random_piece == "knight (horse)":
    letter_of_piece = letters[random.choice[0, 7]]
    number_of_piece = 1

print(f"move {random_piece} on {letter_of_piece}{number_of_piece} to {random.choice(["a", "b", "c", "d", "e", "f", "g", "h"])}{random.choice([i for i in range(0, 9)])}.")
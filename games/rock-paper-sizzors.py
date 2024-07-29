import random

print("rock, paper, sizzors!")
print(" ")
move = input("Enter \"rock\", \"paper\", or \"sizzors\". INPUT SHOULD BE EXACTLY HOW IT IS WRITTEN")
computer_move = random.choice(["rock", "paper", "sizzors"])
print(" ")
print(f"computer move: {computer_move}")
if move == "rock":
    if computer_move == "paper":
        print("You lost. Computer won")
    elif computer_move == "sizzors":
        print("You won. Computer lost")
    else:
        print("Tie")
elif move == "paper":
    if computer_move == "sizzors":
        print("You lost. Computer won")
    elif computer_move == "rock":
        print("You won. Computer lost")
    else:
        print("Tie")
else:
    if computer_move == "rock":
        print("You lost. Computer won")
    elif computer_move == "paper":
        print("You won. Computer lost")
    else:
        print("Tie")
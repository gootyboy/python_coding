import random
import sys

def get_and_clear_input(text):
    while True:
        user_input = input(text)
        if check_if_correct_input(user_input, ["rock", "paper", "scissors"]):
            break
        else:
            sys.stdout.write('\033[F')
            sys.stdout.write('\033[K')
            sys.stdout.flush()
            print("You didn't enter \"rock\", \"paper\", or \"scissors\"")
            print(" ")
            continue
    sys.stdout.write('\033[F')
    sys.stdout.write('\033[K')
    sys.stdout.flush()
    return user_input

def check_winner(player_1_move, player_2_move, player_1_name, player_2_name):
    if player_1_move == player_2_move:
        return "Tie"
    elif (player_1_move == "rock" and player_2_move == "scissors") or (player_1_move == "scissors" and player_2_move == "paper") or (player_1_move == "paper" and player_2_move == "rock"):
        return f"{player_1_name} won. {player_2_name} lost"
    else:
        return f"{player_2_name} won. {player_1_name} lost"

def print_winner():
    global player_1_move, computer_player, player_2_move, player_1_name, player_2_name, computer_move
    try:
        if computer_player == "no":
            print(f"{player_1_name} ---> {player_1_move}")
            print(f"{player_2_name} ---> {player_2_move}")
            winner = check_winner(player_1_move, player_2_move, player_1_name, player_2_name)
        else:
            winner = check_winner(player_1_move, computer_move, player_1_name, "computer")
        print(winner)
    except KeyboardInterrupt:
        print("Keyboard Interrupt. Game Over")
        print(" ")
        ask_play_again()

def ask_play_again():
    while True:
        try:
            while True:
                play_again = input("Would you like to play again? Enter \"yes\" or \"no\": ")
                if check_if_correct_input(play_again, ["yes", "no"]):
                    break
                else:
                    print("You didn't enter \"yes\" or \"no\"")
                    print(" ")
                    continue
            print(" ")
            return play_again
        except KeyboardInterrupt:
            print("Keyboard Interrupt. Game Over")
            print(" ")
            continue

def check_if_correct_input(input, correct_inputs):
    for correct_input in correct_inputs:
        if input.lower() == correct_input:
            return True
    else:
        return False

while True:
    try:
        print("rock, paper, scissors!")
        print(" ")
        while True:
            computer_player = input("Would you like to play with a computer? Enter \"yes\" or \"no\": ")
            if check_if_correct_input(computer_player, ["yes", "no"]):
                break
            else:
                print("You didn't enter \"yes\", or \"no\"")
                print(" ")
                continue
        print(" ")
        player_1_name = input("Enter your name. You will be player one. If no name is given, your name will be \"player one\": ")
        if not player_1_name.strip():
            player_1_name = "player one"
        if computer_player == "no":
            player_2_name = input("Enter your name. You will be player two. If no name is given, your name will be \"player two\": ")
            if not player_2_name.strip():
                player_2_name = "player two"
            player_1_move = get_and_clear_input("Enter \"rock\", \"paper\", or \"scissors\": ")
        else:
            player_1_move = input(f"{player_1_name}'s turn. Enter \"rock\", \"paper\", or \"scissors\": ")

        if computer_player == "yes":
            computer_move = random.choice(["rock", "paper", "scissors"])
            print(f"Computer move: {computer_move}")
        else:
            player_2_move = get_and_clear_input(f"{player_2_name}'s turn. Enter \"rock\", \"paper\", or \"scissors\": ")
        print(" ")
        print_winner()
        break_loop = ask_play_again()
        if break_loop.lower() == "no":
            break
    except KeyboardInterrupt:
        print("Keyboard Interrupt. Game Over")
        break_loop = ask_play_again()
        if break_loop.lower() == "no":
            break
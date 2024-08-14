import random
import sys

message_add = False

def get_and_clear_input(text: str, correct_inputs = ["rock", "paper", "scissors"]) -> str:
    global message_add
    while True:
        if not message_add:
            user_input = input(text)
        else:
            user_input = input(f"{message}. {text}")
            message_add = False
        if correct_inputs != None:
            if check_if_correct_input(user_input, correct_inputs):
                break
            else:
                sys.stdout.write('\033[F')
                sys.stdout.write('\033[K')
                sys.stdout.flush()
                message = 'You didn\'t enter '
                for correct_input in correct_inputs:
                    message += f'"{correct_input}" '
                message_add = True
                continue
        else:
            break
    sys.stdout.write('\033[F')
    sys.stdout.write('\033[K')
    sys.stdout.flush()
    return user_input

def check_winner(player_1_move: str, player_2_move: str, player_1_name: str, player_2_name: str) -> str:
    if player_1_move == player_2_move:
        return "Tie"
    elif (player_1_move == "rock" and player_2_move == "scissors") or (player_1_move == "scissors" and player_2_move == "paper") or (player_1_move == "paper" and player_2_move == "rock"):
        return f"{player_1_name} won. {player_2_name} lost"
    else:
        return f"{player_2_name} won. {player_1_name} lost"

def print_winner() -> None:
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

def ask_play_again() -> str:
    while True:
        try:
            play_again = get_and_clear_input("Would you like to play again? Enter \"yes\" or \"no\": ", ["yes", "no"])
            print(" ")
            return play_again
        except KeyboardInterrupt:
            print("Keyboard Interrupt. Game Over")
            print(" ")
            continue

def check_if_correct_input(input: str, correct_inputs: list = ["rock", "paper", "scissors"]) -> bool:
    for correct_input in correct_inputs:
        if input.lower() == correct_input:
            return True
    else:
        return False

def run_game():
    global player_1_move, player_2_move, computer_player
    while True:
        try:
            print("rock, paper, scissors!")
            print(" ")
            computer_player = get_and_clear_input("Would you like to play with a computer? Enter \"yes\" or \"no\": ", ["yes", "no"])
            player_1_name = get_and_clear_input("Enter your name. You will be player one. If no name is given, your name will be \"player one\": ", None)
            if not player_1_name.strip():
                player_1_name = "player one"
            if computer_player == "no":
                player_2_name = get_and_clear_input("Enter your name. You will be player two. If no name is given, your name will be \"player two\": ", None)
                if not player_2_name.strip():
                    player_2_name = "player two"
                player_1_move = get_and_clear_input("Enter \"rock\", \"paper\", or \"scissors\": ")
            else:
                player_1_move = get_and_clear_input(f"{player_1_name}'s turn. Enter \"rock\", \"paper\", or \"scissors\": ")

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

run_game()
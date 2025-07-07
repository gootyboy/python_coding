import random

def roll_dice():
    return random.randint(1, 6)

def play_dice_game():
    print("Welcome to the Dice Game!")
    player_score = 0
    computer_score = 0

    for round_num in range(1, 6):  # Play 5 rounds
        input(f"Round {round_num}: Press Enter to roll the dice...")
        player_roll = roll_dice()
        computer_roll = roll_dice()
        print(f"You rolled: {player_roll}")
        print(f"Computer rolled: {computer_roll}")

        if player_roll > computer_roll:
            print("You win this round!")
            player_score += 1
        elif player_roll < computer_roll:
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Score -> You: {player_score}, Computer: {computer_score}\n")

    print("Game Over!")
    if player_score > computer_score:
        print("Congratulations! You win the game!")
    elif player_score < computer_score:
        print("Sorry, the computer wins the game!")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
    play_dice_game()
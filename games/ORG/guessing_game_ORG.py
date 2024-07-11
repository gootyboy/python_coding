import random


player_number = int(input("type the amount of players    "))
print(" ")

def how_close(diff, mess, guessing_times):
    if diff<5:
        print(f"{mess} and you are super super close! you have already tried {guessing_times} times")
    elif diff<9:
        print(f"{mess} and you are very close. you have already tried {guessing_times} times")
    elif diff<15:
        print(f"{mess} and you are close. you have already tried {guessing_times} times")
    else:
        print(f"{mess}. you have already tries {guessing_times} times.")
    print(" ")
    
player_names = []
player_guesses = []

lower_limit = -1000
higher_limit = 1000


player = 1

while player<player_number+1:
    player_name = input(f"hi player {player}! what is your name?    ")
    print(" ")
    guess = input (f"guess a number from {lower_limit} to {higher_limit}:   ")
    print(" ")
    player_names.append(player_name)
    
    guess_loop = True
    amount_guesses = 0
    guessed_number = int(guess)
    number_to_guess = random.randint(lower_limit, higher_limit)
    
    while guess_loop:
        guess_diff =abs(guessed_number-number_to_guess)
        amount_guesses += 1
        
        if guessed_number == number_to_guess:
           print(f"correct!!!!! You tried {amount_guesses} times to guess {number_to_guess}")
           print(" ")
           player_guesses.append(amount_guesses)
           guess_loop = False
        else:
            if guessed_number<number_to_guess:
                how_close(guess_diff, "wrong. try higher.", amount_guesses)
                guessed_number = int(input(f"guess a number from {lower_limit} to {higher_limit}:   "))
            else:
                how_close(guess_diff, "wrong, try lower", amount_guesses)
                guessed_number = int(input(f"guess a number from {lower_limit} to {higher_limit}:   "))
                
    player += 1

for i in range(0, player_number):
    print(f"{player_names[i]} ---> {player_guesses[i]}")

winner = min(player_guesses)
counter = 0
winner_index = []

for i in player_guesses:
    if winner == i:
        winner_index.append(counter)
    counter += 1

print(" ")

for i in winner_index:
    print(f"{player_names[i]} WINS THE GAME!!!!!!!!!!!!!!!!!!!!!!!")
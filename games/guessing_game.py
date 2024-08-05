import random

game_loop = True
lower_limit = 200
higher_limit = -200
player_count = 1
computer_player = 1
player_name = 0
player_names = []
player_guesses = []
computer_guess_close = 0
no_answer = True
game_replay_mess_1 = "do you want to play this game agian? Type \"no\" if you don't want to play agian. Type \"yes\" if you want to."
game_replay_mess_2 = "you didn't type \"yes\" or \"no\". please type \"yes\" or \"no\" if you want to play agian    "
player_question = "type the amount of players    "

def play_game_agian(no_answer, game_loop):
    global player_names, player_guesses
    try:
        game_replay_mess_1 = "do you want to play this game agian? Type \"no\" if you don't want to play agian. Type \"yes\" if you want to."
        game_replay = input(game_replay_mess_1)
        print(" ")

        while no_answer == True:
            if game_replay == "yes": 
                game_loop = True
                player_names = []
                player_guesses = []
                no_answer = False
            if game_replay == "no":
                game_loop = False
                no_answer = False
            if game_replay != "no" and game_replay != "yes":
                no_answer = True
    except KeyboardInterrupt:
        print(" ")
        print("Keyboard Interupt")
        print(" ")
        play_game_agian(no_answer, game_loop)
    return game_loop

def how_close(diff, mess, guessing_times):
    global computer_guess_close
    if diff<5:
        print(f"{mess} and you are super super close! you have already tried {guessing_times} times")
        computer_guess_close = "super super close"
    elif diff<9:
        print(f"{mess} and you are very close. you have already tried {guessing_times} times")
        computer_guess_close = "very close"
    elif diff<15:
        print(f"{mess} and you are close. you have already tried {guessing_times} times")
        computer_guess_close = "close"
    else:
        print(f"{mess}. you have already tries {guessing_times} times.")
        computer_guess_close = 0
    print(" ")

def if_not_number(player_input, mess):
    is_number = player_input.lstrip("-").isdigit()
    while is_number == False:
        print("you did not enter a number. please enter a number")
        player_input = input(mess)
        is_number = player_input.lstrip("-").isdigit()
    return player_input

def guess_check(player_type: str, player_type_variable, amount_player_type, lower_limit: int, higher_limit: int):
    global player_names
    while player_type_variable<amount_player_type+1:
        number_to_guess = random.randint(-200, 200)
        if player_type == "player":
            player_name = input(f"hi player {player_count}, what is your name?")
            player_names.append(player_name)
            guess_mess = f"guess a number from {lower_limit} to {higher_limit}:"
            guess = input (guess_mess)
            if_not_number(guess, guess_mess)
  
        print(" ")
        guess_loop = True
        amount_guesses = 0
        guessed_number = int(guess)
                
        while guess_loop:
            guess_diff =abs(guessed_number-number_to_guess)
            amount_guesses += 1
                    
            if guessed_number == number_to_guess:
                if player_type == "player":
                    print(f"correct!!!!! you tried {amount_guesses} times to guess {number_to_guess}")
                else:
                    print(f"correct!!!!! {player_type} {player_type_variable} tried {amount_guesses} times to guess {number_to_guess}")
                print(" ")
                player_guesses.append(amount_guesses)
                guess_loop = False
            else:
                if guessed_number<number_to_guess:
                    how_close(guess_diff, "wrong. try higher.", amount_guesses)
                    if player_type == "player":
                        guessed_number = input(guess_mess)
                        guessed_number = int(if_not_number(guessed_number, guess_mess))
                elif guessed_number>number_to_guess:
                    how_close(guess_diff, "wrong, try lower", amount_guesses)
                    if player_type == "player":
                        guessed_number = input(guess_mess)
                        guessed_number = int(if_not_number(guessed_number, guess_mess))
        player_type_variable += 1

while game_loop:
    try:
        keyboard_interrupt = False
        player_question = "type the amount of players    "
        if keyboard_interrupt == True:
            game_loop_bool = play_game_agian(no_answer, game_loop)
        else:
            amount_of_players = input(player_question)
            if_not_number(amount_of_players, player_question)

        player_number = int(amount_of_players)
        if player_number>0:
            guess_check("player", player_count, player_number, -200, 200)
        for i in range(0, player_number - 1):
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

        print(" ")
        play_game_agian(no_answer, game_loop)
    except KeyboardInterrupt:
        print(" ")
        print("Keyboard Interupt")
        print(" ")
        play_game_agian(no_answer, game_loop)
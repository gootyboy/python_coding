import math

after_number = ["thousand", "million", "trillion", "quadrillion (10 ^ 12)", "quintillion (10 ^ 15)", "sextillion (10 ^ 18)", "septillion (10 ^ 21)", 
                "octillion (10 ^ 24)", "nonillion (10 ^ 27)", "dectillion (10 ^ 30)", "undectillion (10 ^ 33)", "dodectillion (10 ^ 36)", "tridectillion (10 ^ 39)",
                "quattuordecillion (10 ^ 42)", "quindecillion (10 ^ 45)", "sexdecillion (10 ^ 48)", "septendecillion (10 ^ 51)", "octodecillion (10 ^ 54)", 
                "novemdecillion (10 ^ 57)", "vigintillion (10 ^ 60)"]

after_number_less = ["thousandth", "millionth", "trillionth", "quadrillionth (10 ^ -12)", "quintillionth (10 ^ -15)", "sextillionth (10 ^ -18)", "septillionth (10 ^ -21)", 
                "octillionth (10 ^ -24)", "nonillionth (10 ^ -27)", "dectillionth (10 ^ -30)", "undectillionth (10 ^ -33)", "dodectillionth (10 ^ -36)", "tridectillionth (10 ^ -39)",
                "quattuordecillionth (10 ^ -42)", "quindecillionth (10 ^ -45)", "sexdecillionth (10 ^ -48)", "septendecillionth (10 ^ -51)", "octodecillionth (10 ^ -54)", 
                "novemdecillionth (10 ^ -57)", "vigintillionth (10 ^ -60)"]

def print_answer(answer, first_number, symbol, second_number):
    global printed, after_number, after_number_less
    printed = False
    if answer >= 1:
        for i in reversed(range(0, (len(after_number)) * 3, 3)):
            if answer >= 10**i:
                if not printed:
                    answer /= 10**i
                    print(f"{first_number} {symbol} {second_number} = {answer} {after_number[i // 3]}")
                    printed = True
                    break
        else:
            if not printed:
                print(f"{first_number} {symbol} {second_number} = {answer}")
    else:
        for i in reversed(range(0, (len(after_number_less)) * 3, 3)):
            if answer < 10**-i:
                if not printed:
                    answer *= 10**(i + 3)
                    print(f"{first_number} {symbol} {second_number} = {answer} {after_number_less[i // 3]}")
                    printed = True
                    break
        else:
            if not printed:
                print(f"{first_number} {symbol} {second_number} = {answer}")

while True:
    try:
        trig = input("Would you like to do trigonometry? Enter 'no' or 'yes': ")
        if trig not in ["yes", "no"]:
            print("You didn't enter 'yes' or 'no'")
            continue
        if trig == "no":
            first_number = input("Enter first number: ")
        else:
            first_number = input("Enter number (number is in degrees): ")
        try:
            first_number_int = int(first_number)
        except ValueError:
            print("You didn't enter a number. Please enter a number")
            continue
        if trig == "no":
            second_number = input("Enter second number: ")
            try:
                second_number_int = int(second_number)
            except ValueError:
                print("You didn't enter a number. Please enter a number")
                continue
        symbol_correct = False
        while not symbol_correct:
            if trig == "no":
                symbol = input("Enter symbol. SYMBOL MUST BE ONE OF THESE: '+', '-', 'x', '/', or '^': ")
                if symbol not in ["+", "-", "x", "/", "^"]:
                    print("You didn't enter the correct math symbol. Please enter the correct symbol")
                else:
                    symbol_correct = True
            else:
                symbol = input("Enter symbol. SYMBOL MUST BE ONE OF THESE: 'sin', 'cos', or 'tan': ")
                if symbol not in ["sin", "cos", "tan"]:
                    print("You didn't enter the correct math symbol. Please enter the correct symbol")
                else:
                    symbol_correct = True
                    break
        if trig == "no":
            equation_correct = input(f"Is this your math equation: {first_number} {symbol} {second_number}? Enter 'yes' or 'no': ")
        else:
            equation_correct = input(f"Is this your math equation: {symbol}({first_number})? Enter 'yes' or 'no': ")
        if equation_correct == "yes":
            break
        else:
            print("Let's try again.")
    except KeyboardInterrupt:
        print(" ")
        print("Keyboard interrupt")
        continue

if symbol == "+":
    answer = int(first_number) + int(second_number)
    print(f"{first_number} {symbol} {second_number} = {int(first_number) + int(second_number)}")
elif symbol == "-":
    answer =int(first_number) - int(second_number)
    print(f"{first_number} {symbol} {second_number} = {int(first_number) - int(second_number)}")
elif symbol == "x":
    answer = int(first_number) * int(second_number)
    print_answer(answer, first_number, symbol, second_number)
elif symbol == "/":
    if second_number_int != 0:
        answer = int(first_number) / int(second_number)
        print_answer(answer, first_number, symbol, second_number)
    else:
        print(f"{first_number} {symbol} {second_number} is undefined")
elif symbol == "^":
    answer = int(first_number) ** int(second_number)
    print(answer)
    print_answer(answer, first_number, symbol, second_number)
elif symbol == "sin":
    print(f"{symbol}({first_number}) = {math.sin(math.radians(int(first_number)))}")
elif symbol == "cos":
    print(f"{symbol}({first_number}) = {math.cos(math.radians(int(first_number)))}")
elif symbol == "tan":
    if first_number_int % 180 == 90:
        print(f"{symbol}({first_number}) is undefined")
    else:
        print(f"{symbol}({first_number}) = {math.tan(math.radians(int(first_number)))}")
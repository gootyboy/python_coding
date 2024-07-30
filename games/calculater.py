import math

equation_correct = "no"
symbol_correct = False
while equation_correct == "no":
    try:
        trig = input("Would you like to do trigonometry? Enter \"no\" or \"yes\"")
        if trig != "yes" and trig != "no":
            print("You didn't enter \"yes\" or \"no\"")
            continue
        first_number = input("Enter first number")
        try:
            first_number_int = int(first_number)
        except ValueError:
            print("You didn't enter a number. PLease enter a number")
            continue
        if trig == "no":
            secound_number = input("Enter second number")
            try:
                secound_number_int = int(secound_number)
            except ValueError:
                print("You didn't enter a number. PLease enter a number")
                continue
        while not symbol_correct:
            if trig == "no":
                symbol = input("Enter symbol. SYMBOL MUST BE ONE OF THESE: \"+\", \"-\", \"x\", \"/\", or \"^\"")
                if symbol != "+" and symbol != "-" and symbol != "x" and symbol != "/" and symbol != "^":
                    print("You didn't enter the correct math symbol. Please enter the correct symbol")
                else:
                    symbol_correct = True
            else:
                symbol = input("Enter symbol. SYMBOL MUST BE ONE OF THESE: \"sin\", \"cos\", or \"tan\"")
                if symbol != "sin" and symbol != "cos" and symbol != "tan":
                    print("You didn't enter the correct math symbol. Please enter the correct symbol")
                else:
                    symbol_correct = True
        if trig == "no":
            equation_correct = input(f"is these your math equation: {first_number} {symbol} {secound_number}? Enter \"yes\" or \"no\"")
        else:
            equation_correct = input(f"is these your math equation: {symbol}({first_number})? Enter \"yes\" or \"no\"")
    except KeyboardInterrupt:
        print(" ")
        print("Keyboard interupt")
        continue

if symbol == "+":
    print(f"{first_number} {symbol} {secound_number} = {int(first_number) + int(secound_number)}")
elif symbol == "-":
    print(f"{first_number} {symbol} {secound_number} = {int(first_number) - int(secound_number)}")
elif symbol == "x":
    print(f"{first_number} {symbol} {secound_number} = {int(first_number) * int(secound_number)}")
elif symbol == "/":
    print(f"{first_number} {symbol} {secound_number} = {int(first_number) / int(secound_number)}")
elif symbol == "^":
    print(f"{first_number} {symbol} {secound_number} = {int(first_number) ** int(secound_number)}")
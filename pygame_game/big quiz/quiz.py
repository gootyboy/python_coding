import os
import pgzrun
import random
from pgzero import clock
from pgzero.rect import Rect
from pgzero.constants import keys
from pgzero import ptext

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 1280
HEIGHT = 720
TITLE = "Big Quiz"

main_box = Rect(50, 85, 820, 240)
timer_box = Rect(990, 85, 240, 240)
score_box = Rect(50, 0, 535, 75)
questions_finished_box = Rect(600, 0, 635, 75)
answer_box1 = Rect(50, 358, 495, 165)
answer_box2 = Rect(735, 358, 495, 165)
answer_box3 = Rect(50, 538, 495, 165)
answer_box4 = Rect(735, 538, 495, 165)

amount_of_questions = 0
enter_key_pressed = False
loading_run = False

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
question_generated = False

score = 0
time_left = 2
game_start = False

number_digits = []
number = 0
questions = []

def get_divisors(number):
    divisors = []
    if number != 0:
        for i in range(1, int(number**0.5) + 1):
            if number % i == 0:
                divisors.append(i)
                if i != number // i:
                    divisors.append(number // i)
    else:
        divisors = [0]
    return sorted(divisors)

def generate_question(symbol):
    first_number = random.randint(0, 100 if symbol != "x" else 20)
    if symbol != "÷":
        if symbol != "-":
            second_number = random.randint(0, 100 if symbol != "x" else 20)
        else:
            second_number = random.randint(0, first_number)
    else:
        if first_number != 0:
            second_number = random.choice(get_divisors(first_number))
        else:
            second_number = random.randint(1, 100)
    if symbol == "+":
        answer = first_number + second_number
    elif symbol == "-":
        answer = first_number - second_number
    elif symbol == "x":
        answer = first_number * second_number
    elif symbol == "÷":
        answer = int(first_number / second_number)
    
    wrong_answers = []
    for _ in range(3):
        high_low = random.choice(["high", "low"])
        if high_low == "high":
            wrong_answers.append(random.randint(answer + 1, answer + 10))
        else:
            wrong_answers.append(random.randint(0, max(answer - 1, 0)))

    answer_number = random.randint(1, 4)
    options = wrong_answers[:]
    options.insert(answer_number - 1, answer)
    return [f"What is {first_number} {symbol} {second_number}?", *map(str, options), answer_number]

def generate_random_questions():
    symbols = ["+", "-", "x", "÷"]
    return generate_question(random.choice(symbols))

def draw():
    global game_start, question_generated, question, questions, enter_key_pressed
    screen.fill("dim gray")
    
    if game_start and question_generated:
        screen.draw.filled_rect(main_box, "sky blue")
        screen.draw.filled_rect(timer_box, "sky blue")
        screen.draw.filled_rect(score_box, "sky blue")
        screen.draw.filled_rect(questions_finished_box, "sky blue")

        index = 1
        for box in answer_boxes:
            screen.draw.filled_rect(box, "orange")
            screen.draw.textbox(question[index], box, color="black")
            index += 1
        
        screen.draw.textbox(str(time_left), timer_box, color="black")
        screen.draw.textbox(question[0], main_box, color="black")
        screen.draw.textbox(f"Score: {score}/{amount_of_questions}", score_box, color="black")
        screen.draw.textbox(f"Question: {amount_of_questions - len(questions)}/{amount_of_questions}", questions_finished_box, color="black")
    else:
        if not enter_key_pressed:
            screen.draw.text("Enter the number of questions you want to answer:", center=(WIDTH / 2, HEIGHT / 2), color="black")
            screen.draw.textbox(f"{number}", Rect(0, HEIGHT / 2, WIDTH, 100), color="black")
        else:
            if not question_generated:
                screen.draw.text("Loading questions...", center=(WIDTH / 2, HEIGHT / 2), color="blue", fontsize=200)

def on_key_down(key):
    global game_start, time_left, number, number_digits, amount_of_questions, question, questions, enter_key_pressed, question_generated
    if key.name.removeprefix("K_").isdigit():
        number_digits.append(key.name.removeprefix("K_"))
        number = int("".join(number_digits))
    elif key == keys.BACKSPACE:
        if number_digits:
            number_digits.pop()
            number = int("".join(number_digits)) if number_digits else 0
        else:
            number = 0
    elif key == keys.RETURN:
        if number > 0:
            enter_key_pressed = True
            amount_of_questions = number
            screen.draw.text("Loading questions...", center=(WIDTH / 2, HEIGHT / 2), color="blue", fontsize=200)  # Display loading message
            questions = [generate_random_questions() for _ in range(amount_of_questions)]
            random.shuffle(questions)
            question = questions.pop(0)
            question_generated = True
            game_start = True

def game_over():
    global question, time_left
    message = f"Game Over! You got {score} out of {amount_of_questions} questions right."
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

def correct_answer():
    global question, score, time_left
    score += 1
    time_left += 10
    if questions:
        question = questions.pop(0)
    else:
        game_over()

def on_mouse_down(pos):
    global score, time_left, game_start
    index = 1
    if game_start:
        for box in answer_boxes:
            if box.collidepoint(pos):
                if index == question[5]:
                    correct_answer()
                else:
                    score -= 1
                    time_left -= 10
                    correct_answer()
            index += 1

def update_time_left():
    global time_left, game_start
    if game_start:
        if time_left:
            time_left -= 1
        else:
            game_over()

def on_key_down(key):
    global game_start, time_left, number, number_digits, amount_of_questions, question, questions, enter_key_pressed, question_generated
    if key.name.removeprefix("K_").isdigit():
        number_digits.append(key.name.removeprefix("K_"))
        number = int("".join(number_digits))
    elif key == keys.BACKSPACE:
        if number_digits:
            number_digits.pop()
            number = int("".join(number_digits)) if number_digits else 0
        else:
            number = 0
    elif key == keys.RETURN:
        if number > 0:
            enter_key_pressed = True
            amount_of_questions = number
            questions = [generate_random_questions() for _ in range(amount_of_questions)]
            random.shuffle(questions)
            question = questions.pop(0)
            question_generated = True
            game_start = True

clock.schedule_interval(update_time_left, 1)

pgzrun.go()
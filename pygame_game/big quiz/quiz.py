import pygame
import pgzrun
import random

WIDTH = 1280
HEIGHT = 720

lower_range_answer = 20
higher_range_answer = 20

q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20]
amount_of_questions = len(questions)
question_number = 1

def generate_math_equation():
    global wrong_answer1, wrong_answer2, wrong_answer3, answer, math_symbol, answer_place, first_number, secound_number
    math_symbol = random.choice(["+", "-", "x", "/", "^"])

    first_number = random.randint(0, 100)
    secound_number = random.randint(0, 100)
    if math_symbol == "+":
        answer = first_number + secound_number
    elif math_symbol == "-":
        answer = first_number - secound_number
    elif math_symbol == "x":
        answer = first_number * secound_number
    elif math_symbol == "/":
        if secound_number == 0:
            first_number = random.randint(0, 100)
            secound_number = random.randint(0, 100)
        answer = first_number / secound_number
    elif math_symbol == "^":
        first_number = random.randint(1, 5)
        secound_number = random.randint(2, 3)
        answer = first_number ** secound_number
    wrong_answer1 = random.randint(int(answer -lower_range_answer), int(answer + higher_range_answer))
    wrong_answer2 = random.randint(int(answer -lower_range_answer), int(answer + higher_range_answer))
    wrong_answer3 = random.randint(int(answer -lower_range_answer), int(answer + higher_range_answer))
    answer_place = random.randint(1, 4)

answer_box1 = pygame.Rect(50, 358, 495, 165)
answer_box2 = pygame.Rect(735, 358, 495, 165)
answer_box3 = pygame.Rect(50, 538, 495, 165)
answer_box4 = pygame.Rect(735, 538, 495, 165)
main_box = pygame.Rect(50, 80, 820, 240)
timer_box = pygame.Rect(990, 80, 240, 240)
question_number_box = pygame.Rect(735, 0, 495, 80)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 30

for question in questions:
    generate_math_equation()
    question.extend([f"{first_number} {math_symbol} {secound_number}", str(answer), str(wrong_answer1), str(wrong_answer2), str(wrong_answer3), answer_place])
question = questions.pop(0)

def draw():
    screen.clear()
    screen.fill((128, 128, 128))
    screen.draw.filled_rect(question_number_box, "light blue")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")
    screen.draw.textbox(str(time_left), timer_box, color=("Black"))
    screen.draw.textbox(question[0], main_box, color= ("Black"))
    screen.draw.textbox(f"question {question_number}", question_number_box, color=("Black"))

    index = 1
    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")
        screen.draw.textbox(question[index], box, color= ("Black"))
        index += 1

def game_over():
    global question, time_left, question_number
    message = f"Game Over. you got {str(score)} out of {amount_of_questions} questions correct"
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0
    question_number = 20

def correct_answer():
    global question, score, time_left
    score += 1
    if questions:
        question = questions.pop(0)
        time_left += 10
    else:
        game_over()

def on_mouse_down(pos):
    global question, question_number
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            question_number += 1
            if index == question[5]:
                correct_answer()
            else:
                if len(questions)> 0:
                    question = questions.pop(0)
                else:
                    question_number = 20
                    game_over()
        index += 1

def update_time_left():
    global time_left
    if time_left:
        time_left -= 1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1.0)

pgzrun.go()
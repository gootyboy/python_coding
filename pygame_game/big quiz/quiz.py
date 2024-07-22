import pygame
import pgzrun
import random

WIDTH = 1280
HEIGHT = 720

lower_range_answer = 20
higher_range_answer = 20

if_correct_answer = 1

q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20]
amount_of_questions = len(questions)
question_number = 1

def generate_math_equation():
    global wrong_answer1, wrong_answer2, wrong_answer3, answer, math_symbol, answer_place, first_number, secound_number
    add_sub_mult_or_div = random.randint(1, 5)

    if add_sub_mult_or_div == 1:
        math_symbol = "+"
        first_number = random.randint(0, 100)
        secound_number = random.randint(0, 100)
        answer = first_number + secound_number
        wrong_answer1 = random.randint(answer -lower_range_answer, answer + higher_range_answer)
        wrong_answer2 = random.randint(answer -lower_range_answer, answer + higher_range_answer)
        wrong_answer3 = random.randint(answer -lower_range_answer, answer + higher_range_answer)
    elif add_sub_mult_or_div == 2:
        math_symbol = "-"
        first_number = random.randint(0, 100)
        secound_number = random.randint(0, 100)
        answer = first_number - secound_number
        wrong_answer1 = random.randint(answer -lower_range_answer, answer + higher_range_answer)
        wrong_answer2 = random.randint(answer -lower_range_answer, answer + higher_range_answer)
        wrong_answer3 = random.randint(answer -lower_range_answer, answer + higher_range_answer)
    elif add_sub_mult_or_div == 3:
        math_symbol = "x"
        first_number = random.randint(0, 100)
        secound_number = random.randint(0, 100)
        answer = first_number * secound_number
        wrong_answer1 = random.randint(answer -lower_range_answer, answer + higher_range_answer)
        wrong_answer2 = random.randint(answer -lower_range_answer, answer + higher_range_answer)
        wrong_answer3 = random.randint(answer -lower_range_answer, answer + higher_range_answer)
    elif add_sub_mult_or_div == 4:
        math_symbol = "/"
        first_number = random.randint(0, 100)
        secound_number = random.randint(0, 100)
        if secound_number == 0:
            first_number = random.randint(0, 100)
            secound_number = random.randint(0, 100)
        answer = first_number / secound_number
        wrong_answer1 = random.randint(int(answer -lower_range_answer), int(answer + higher_range_answer))
        wrong_answer2 = random.randint(int(answer -lower_range_answer), int(answer + higher_range_answer))
        wrong_answer3 = random.randint(int(answer -lower_range_answer), int(answer + higher_range_answer))
    elif add_sub_mult_or_div == 5:
        math_symbol = "^"
        first_number = random.randint(1, 5)
        secound_number = random.randint(2, 3)
        answer = first_number ** secound_number
        wrong_answer1 = random.randint(answer -lower_range_answer, answer + higher_range_answer)
        wrong_answer2 = random.randint(answer -lower_range_answer, answer + higher_range_answer)
        wrong_answer3 = random.randint(answer -lower_range_answer, answer + higher_range_answer)
    answer_place = random.randint(1, 4)

main_box = pygame.Rect(0, 0, 820, 240)
timer_box = pygame.Rect(0, 0, 240, 240)
answer_box1 = pygame.Rect(0, 0, 495, 165)
answer_box2 = pygame.Rect(0, 0, 495, 165)
answer_box3 = pygame.Rect(0, 0, 495, 165)
answer_box4 = pygame.Rect(0, 0, 495, 165)
question_number_box = pygame.Rect(0, 0, 495, 80)
correct_or_wrong_box = pygame.Rect(0, 0, 435, 80)

main_box.move_ip(50, 80)
timer_box.move_ip(990, 80)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)
question_number_box.move_ip(735, 0)
correct_or_wrong_box.move_ip(50, 0)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 30

def ask_question(question_number):
    if answer_place == 1:
        question_number.append(f"{first_number} {math_symbol} {secound_number}")
        question_number.append(f"{answer}")
        question_number.append(f"{wrong_answer1}")
        question_number.append(f"{wrong_answer2}")
        question_number.append(f"{wrong_answer3}")
        question_number.append(1)
    if answer_place == 2:
        question_number.append(f"{first_number} {math_symbol} {secound_number}")
        question_number.append(f"{wrong_answer1}")
        question_number.append(f"{answer}")
        question_number.append(f"{wrong_answer2}")
        question_number.append(f"{wrong_answer3}")
        question_number.append(2)
    if answer_place == 3:
        question_number.append(f"{first_number} {math_symbol} {secound_number}")
        question_number.append(f"{wrong_answer1}")
        question_number.append(f"{wrong_answer2}")
        question_number.append(f"{answer}")
        question_number.append(f"{wrong_answer3}")
        question_number.append(3)
    if answer_place == 4:
        question_number.append(f"{first_number} {math_symbol} {secound_number}")
        question_number.append(f"{wrong_answer1}")
        question_number.append(f"{wrong_answer2}")
        question_number.append(f"{wrong_answer3}")
        question_number.append(f"{answer}")
        question_number.append(4)

for i in questions:
    generate_math_equation()
    ask_question(i)
question = questions.pop(0)

def draw():
    screen.clear()
    screen.fill((128, 128, 128))
    screen.draw.filled_rect(question_number_box, "light blue")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")
    screen.draw.filled_rect(correct_or_wrong_box, "light blue")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")

    screen.draw.textbox(str(time_left), timer_box, color=("Black"))
    screen.draw.textbox(question[0], main_box, color= ("Black"))
    screen.draw.textbox(f"question {question_number}", question_number_box, color=("Black"))

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color= ("Black"))
        index += 1
    
    if if_correct_answer == True:
        screen.draw.textbox("Correct" , correct_or_wrong_box, color= ("Black"))
    if if_correct_answer == False:
        screen.draw.textbox("Wrong" , correct_or_wrong_box, color= ("Black"))

def game_over():
    global question, time_left, question_number

    message = f"Game Over. you got %s out of {amount_of_questions} questions correct" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0
    question_number = 20

def correct_answer():
    global question, score, time_left, if_correct_answer

    if_correct_answer = True
    score += 1
    if questions:
        question = questions.pop(0)
        time_left += 10
    else:
        game_over()

def on_mouse_down(pos):
    global question, question_number, if_correct_answer

    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            question_number += 1
            if index == question[5]:
                correct_answer()
            else:
                if_correct_answer = False
                if len(questions)> 0:
                    question = questions.pop(0)
                else:
                    question_number = 20
                    game_over()
        index += 1

def update_time_left():
    global time_left, if_correct_answer

    if time_left:
        time_left -= 1
        if_correct_answer = 1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1.0)

pgzrun.go()
import turtle
import datetime

wn = turtle.Screen()
wn.bgcolor("white")

on_home_screen = True

lowercase_letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
uppercase_letters = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
amount_lower_or_upper_letters = len(lowercase_letters)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

time = turtle.Turtle()
time.hideturtle()
time.penup()
time_and_date = datetime.datetime.now()
time_hour = time_and_date.hour
time_minute = time_and_date.minute

letter_pen = turtle.Turtle()
letter_pen.hideturtle()
letter_pen.teleport(-150, -85)

def write_time(time_hour, time_minute):
    if time_hour > 12:
        time_hour -= 12
    if time_minute < 10:
        time.write(f"{time_hour}:0{time_minute}", font= ("comic Sans MS", 60, "normal"))
    elif time_minute >= 10:
        time.write(f"{time_hour}:{time_minute}", font= ("comic Sans MS", 60, "normal"))

def create_box(password_box, amount_password_digits):
    for i in range(1, amount_password_digits + 1):
        password_box.pendown()
        for i in range(1, 5):
            password_box.forward(30)
            password_box.left(90)
        password_box.penup()
        password_box.forward(50)

def ask_password(x, y):
    print("ask_password")
    time.clear()
    password_pen.write("password:", font= ("Comic Sans MS", 40, "normal"))
    create_box(password_box, amount_password_digits)

    for i in lowercase_letters:
        wn.onkeypress(lambda i=i: on_letter_press(i,0), key= i)
        
    wn.listen()   

def draw_letter(letter : str, amount_of_times_ran, return_bool: bool = False):
    if amount_of_times_ran + 1 == 1:
        letter_1 = letter
        if return_bool == False:
            letter_pen.write(letter, font= ("Comic Sans MS", 15, "bold"))
        if return_bool == True:
            return letter_1
    elif amount_of_times_ran + 1 == 2:
        letter_2 = letter
        if return_bool == False:
            letter_pen.write(letter, font= ("Comic Sans MS", 15, "bold"))
        if return_bool == True:
            return letter_2
    elif amount_of_times_ran + 1 == 3:
        letter_3 = letter
        if return_bool == False:
            letter_pen.write(letter, font= ("Comic Sans MS", 15, "bold"))
        if return_bool == True:
            return letter_3
    elif amount_of_times_ran + 1 == 4:
        letter_4 = letter
        if return_bool == False:
            letter_pen.write(letter, font= ("Comic Sans MS", 15, "bold"))
        if return_bool == True:
            return letter_4
    elif amount_of_times_ran + 1 == 5:
        letter_5 = letter
        if return_bool == False:
            letter_pen.write(letter, font= ("Comic Sans MS", 15, "bold"))
        if return_bool == True:
            return letter_5
    elif amount_of_times_ran + 1 == 6:
        letter_6 = letter
        if return_bool == False:
            letter_pen.write(letter, font= ("Comic Sans MS", 15, "bold"))
        if return_bool == True:
            return letter_6
    elif amount_of_times_ran + 1 == 7:
        letter_7 = letter
        if return_bool == False:
            letter_pen.write(letter, font= ("Comic Sans MS", 15, "bold"))
        if return_bool == True:
            return letter_7
    elif amount_of_times_ran + 1 == 8:
        letter_8 = letter
        if return_bool == False:
            letter_pen.write(letter, font= ("Comic Sans MS", 15, "bold"))
        if return_bool == True:
            return letter_8

def on_letter_press(letter,amount_of_times_ran):
    print(letter)
    for i in range(0, amount_lower_or_upper_letters):
        if letter == lowercase_letters[i]:
            draw_letter(letter, amount_of_times_ran)
    for i in range(0, amount_lower_or_upper_letters):
        if letter == uppercase_letters[i]:
            draw_letter(letter, amount_of_times_ran)

write_time(time_hour, time_minute)


password_pen = turtle.Turtle()
password_pen.hideturtle()
password_pen.penup()
password_pen.teleport(-100, 0)

password_box = turtle.Turtle()
password_box.speed(0)
password_box.penup()
password_box.teleport(-150, -100)
password_box.hideturtle()
password_digits = ["p", "a", "s", "s", "w", "o", "r", "d"]
amount_password_digits = len(password_digits)

wn.onclick(fun= ask_password)
# wn.listen()
wn.mainloop()
import pgzrun
import random
from pgzero.keyboard import keyboard

WIDTH = 800
HEIGHT = 600
TITLE = "Hangman Game"

words = ["monkey", "dog", "banana", "water", "baby"]
word = random.choice(words)
word_length = len(word)
guesses = 0
guessed_letters = []

def draw():
    global word_length
    screen.fill("white")
    screen.draw.text(" _ " * 5 , color="black", center = (WIDTH / 2, HEIGHT / 2 + 100), fontsize = 50)
    screen.draw.text("Guess a letter" , color="black", center = (WIDTH / 2, HEIGHT / 2 - 100), fontsize = 50)
    if guesses > 0:
        screen.draw.text(', '.join(guessed_letters), color="black", center = (WIDTH / 2, HEIGHT / 2), fontsize = 50)
        
def on_key_up(key):
    global guessed_letters, guesses
    letters = {
        keys.Q: "q",
        keys.W: "w",
        keys.E: "e",
        keys.R: "r",
        keys.T: "t",
        keys.Y: "y",
        keys.U: "u",
        keys.I: "i",
        keys.O: "o",
        keys.P: "p",
        keys.A: "a",
        keys.S: "s",
        keys.D: "d",
        keys.F: "f",
        keys.G: "g",
        keys.H: "h",
        keys.J: "j",
        keys.K: "k",
        keys.L: "l",
        keys.Z: "z",
        keys.X: "x",
        keys.C: "c",
        keys.V: "v",
        keys.B: "b",
        keys.N: "n",
        keys.M: "m"
    }
    guessed_letters.append(letters[key])
    guesses += 1

pgzrun.go()
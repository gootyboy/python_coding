from random import randint
from pgzero.actor import Actor

WIDTH = 800
HEIGHT = 600

balloon = Actor("balloon.png")
balloon.pos = 400, 300

bird = Actor("bird-up")
bird.pos = randint(800, 1600), randint(10, 200)

house = Actor("house")

tree = Actor("tree")

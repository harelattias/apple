import pgzrun
import random

def draw():
    screen.fill((0, 170, 0))
    apple.draw()


def place_apple():
    apple.x = random.randint(1, 800)
    apple.y = random.randint(1, 540)


apple = Actor("apple")
place_apple()

pgzrun.go()

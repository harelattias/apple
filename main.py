import pgzrun
import random
import pygame

def on_mouse_down(pos):
    global number_good_shots
    global number_of_attempts

    number_of_attempts = number_of_attempts +1
    if number_of_attempts ==  11:
        quit()

    if apple.collidepoint(pos):
        number_good_shots = number_good_shots + 1
        place_apple()


def draw():
    screen.fill((0, 170, 0))
    apple.draw()
    global number_good_shots
    global number_of_attempts
    #pygame.display.set_caption("Number of good shots : " + str(number_good_shots))
    screen.draw.text("number of hits -> " + str(number_good_shots) + " / " + str(number_of_attempts), (20, 20), owidth=1, ocolor="blue")


def place_apple():
    apple.x = random.randint(1, 800)
    apple.y = random.randint(1, 540)


number_good_shots = 0
number_of_attempts = 0
apple = Actor("apple")
place_apple()

pgzrun.go()

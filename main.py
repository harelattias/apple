import pgzrun
import random
import pygame


def on_mouse_down(pos):
    global number_good_shots
    if apple.collidepoint(pos):
        number_good_shots = number_good_shots + 1
        print("good shot!", number_good_shots)
        place_apple()
    else:
        print("you missed!")

def draw():
    screen.fill((0, 170, 0))
    apple.draw()
    global number_good_shots
    pygame.display.set_caption("Number of good shots : " + str(number_good_shots))


# def draw_number_of_hits():
#     global number_good_shots
#     font = pygame.font.SysFont(None, 48)
#     img = font.render(number_good_shots, True, RED)
#     screen.draw.text("hello world", (20, 20), owidth=1, ocolor="blue")

def place_apple():
    apple.x = random.randint(1, 800)
    apple.y = random.randint(1, 540)


global number_good_shots
number_good_shots = 0
apple = Actor("apple")
place_apple()

pgzrun.go()

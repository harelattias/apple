import pgzrun


def draw():
    screen.fill((0, 0, 0))
    apple.draw()


def place_apple():
    apple.x = 300
    apple.y = 200


apple = Actor("apple")
place_apple()

pgzrun.go()

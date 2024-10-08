from pico2d import *
from random import *


class Ball:
    def __init__(self):
        self.x = randint(0, 799)
        self.y = 599
        self.speed = randint(3, 6)

        size = randint(0, 1)

        if size == 0:
            self.image = load_image("ball21x21.png")

        else:
            self.image = load_image("ball41x41.png")

    def update(self):
        self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def update_worlds():
    for w in worlds:
        w.update()


def render_worlds():
    clear_canvas()

    for w in worlds:
        w.draw()

    update_canvas()


def reset_worlds():
    global running, worlds

    running = True
    worlds = []

    balls = [Ball() for i in range(20)]
    worlds += balls


open_canvas()

reset_worlds()

while running:
    handle_events()
    update_worlds()
    render_worlds()
    delay(0.016)


close_canvas()

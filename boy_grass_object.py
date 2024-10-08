from pico2d import *


# Game object class here
class Grass:
    #   생성자를 이용해 객체의 초기 상태를 정의
    def __init__(self):
        self.image = load_image("grass.png")

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image("run_animation.png")

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def update_worlds():
    boy.update()
    grass.update()


def render_worlds():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()


def reset_worlds():
    global running, grass, boy

    running = True
    grass = Grass()  #   Grass 클래스로 grass 객체 생성
    boy = Boy()


open_canvas()

# initialization code
reset_worlds()

# game main loop code
while running:
    handle_events()
    update_worlds()
    render_worlds()
    delay(0.016)


# finalization code

close_canvas()

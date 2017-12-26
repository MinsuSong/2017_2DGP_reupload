import GameFramework
import State_Title
from pico2d import *


name = "State_Logo"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas()
    image = load_image('Images\\Scene\\TestImage_Logo.png')


def exit():
    global image
    del(image)
    close_canvas()


def update(frame_time):
    global logo_time
    logo_time += frame_time

    if (logo_time > 1.0):
        logo_time = 0
        GameFramework.push_state(State_Title)



def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: # Window X botton
            GameFramework.quit()

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE): # ESC pressed
            GameFramework.quit()


def pause():
    pass

def resume():
    pass
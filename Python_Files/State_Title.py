import GameFramework
import State_Main
from pico2d import*

name = "State_Title"
image = None

def enter():
    global image
    image = load_image('TestImage_Title.png')

def exit():
    global image
    del(image)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFramework.quit()
        else:
            if (event.type, event.key) ==  (SDL_KEYDOWN, SDLK_ESCAPE):
                GameFramework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                GameFramework.change_state(State_Main)

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update(frame_time):
    pass

def pause():
    pass

def resume():
    pass
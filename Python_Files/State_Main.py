import GameFramework
import State_Title
import Difficulty_normal
from pico2d import*

name = "State_Main"
image = None

''' 
Main 추가 버튼 요소 (제작 안했음 아직)

1.    *점수화면
2.    *난이도
3.    *나가기
'''

def enter():
    global image

    image = load_image('TestImage_Main.png')

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
                GameFramework.change_state(State_Title)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                GameFramework.change_state(Difficulty_normal)

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
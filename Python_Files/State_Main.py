import GameFramework
import State_Title
import Difficulty_normal
import Difficulty_hard
from UI_Button_Normal import ButtonNormal
from UI_Button_Hard import ButtonHard
from UI_Mouse import Mouse
from pico2d import*


name = "State_Main"
image = None
mouse_X = 0
mouse_Y = 0
mouse = None

class BGM:
    def __init__(self):
        self.bgm = load_music('sound\\Main.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

def handle_events(frame_time):
    global mouse_X, mouse_Y, mouse, button_normal, button_hard
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFramework.quit()
        else:
            if (event.type, event.key) ==  (SDL_KEYDOWN, SDLK_ESCAPE):
                GameFramework.push_state(State_Title)

        if (collide(button_normal, mouse)):
            if event.type == SDL_MOUSEBUTTONDOWN:
                if event.button == SDL_BUTTON_LEFT:
                    GameFramework.change_state(Difficulty_normal)
        if (collide(button_hard, mouse)):
            if event.type == SDL_MOUSEBUTTONDOWN:
                if event.button == SDL_BUTTON_LEFT:
                    GameFramework.change_state(Difficulty_hard)

        ### 버튼과 마우스 좌표 ###
        if event.type == SDL_MOUSEMOTION:
            mouse_X = event.x
            mouse_Y = 600 - event.y
            mouse.get_mouse_position(mouse_X,mouse_Y)

def enter():
    global image, mouse, button_normal, button_hard, bgm
    image = load_image('Images\Scene\TestImage_Main.png')
    mouse = Mouse()
    button_normal = ButtonNormal()
    button_hard = ButtonHard()
    bgm = BGM()


def exit():
    global image



def draw(frame_time):
    global image, mouse, button_normal, button_hard
    clear_canvas()
    image.draw(400, 300)
    button_hard.draw(collide(button_hard, mouse))
    button_normal.draw(collide(button_normal, mouse))

    update_canvas()


def update(frame_time):
    pass

def pause():
    pass

def resume():
    pass

#### 마우스 vs 버튼 충돌처리 #####

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
    pass
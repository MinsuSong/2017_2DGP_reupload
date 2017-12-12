import GameFramework
import State_Main
import State_GameOver
import State_Clear
from pico2d import*

# 1500 X 750 Size Map


from Object_Cupid import Cupid
from Background import Background_Forest
from Object_ObstacleHill import ObstacleHill
from Object_Target import Target
from Object_Arrow import Arrow
from UI_PowerGage import Gage
from UI_life import Life

def enter():
    close_canvas()
    GameFramework.reset_time()
    open_canvas(1500,750)
    create_world()

class BGM:
    def __init__(self):
        self.bgm = load_music('sound\\background.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

def create_world(): #세계 생성
    global cupid, background, target, obstaclehill, arrowlist,gagelist, life, bgm
    cupid = Cupid()
    background = Background_Forest()
    target = Target()
    obstaclehill = ObstacleHill()
    arrowlist = []
    gagelist = []
    life = Life()
    bgm = BGM()

def destory_world(): #세계 파괴
    global cupid, background, target, obstaclehill, arrowlist, gagelist, life
    del(cupid)
    del(background)
    del(target)
    del(obstaclehill)
    for arrow in arrowlist:
        del(arrow)
    arrowlist = []
    gagelist = []
    del(life)

def exit():
    destory_world()


def update(frame_time):
    global cupid, arrowlist, gagelist, power
    cupid.update(frame_time)
    for arrow in arrowlist:
        arrow.update(frame_time)
    for gage in gagelist:
        gage.update(frame_time)



def draw(frame_time):
    global cupid, background, obstaclehill, target, arrowlist, gagelist, life

    clear_canvas()
    background.draw()

    for gage in gagelist:
        gage.draw(frame_time)

    target.draw()
    target.draw_bb()

    obstaclehill.draw()
    obstaclehill.draw_bb()

    cupid.draw()
    cupid.draw_bb()
    life.draw()
    for arrow in arrowlist:
        arrow.draw(frame_time)
        arrow.draw_bb()


        if collide(arrow, obstaclehill):
            arrowlist.remove(arrow)
            arrow.hit()
            life.decrease()

            if life.lifepoint == 0:
                GameFramework.change_state(State_GameOver)

        elif collide(arrow, target):
            GameFramework.change_state(State_Clear)

        elif (arrow.position_Y < 0 ):
            arrowlist.remove(arrow)

    update_canvas()



def handle_events(frame_time):
    global arrowlist, gagelist, mouse_x,mouse_y, power, gage
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFramework.quit()
        elif event.type != SDL_QUIT:
            if (event.type, event.key) ==  (SDL_KEYDOWN, SDLK_ESCAPE):
                close_canvas()
                open_canvas()
                GameFramework.change_state(State_Main)

            elif (event.type) == SDL_MOUSEMOTION:
                mouse_x = event.x
                mouse_y = 750 - event.y

            elif event.type == SDL_MOUSEBUTTONDOWN:
                if event.button == SDL_BUTTON_LEFT:
                    gage = Gage(mouse_x, mouse_y)

                    gagelist.append(gage)

            elif event.type == SDL_MOUSEBUTTONUP:
                if event.button == SDL_BUTTON_LEFT:

                    power = gage.level
                    arrow = Arrow(None, gage.level)
                    arrowlist.append(arrow)
                    arrow.firearrow()
                    gagelist.remove(gagelist[-1])

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    #충돌이 없는 경우를 비교하는 것은?
    #충돌이 일어나지 않는 경우가 더 많기 때문에.


    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
    pass

def resume():
    pass

def pause():
    pass

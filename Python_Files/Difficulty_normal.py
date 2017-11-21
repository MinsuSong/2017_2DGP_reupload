import GameFramework
import State_Main
from pico2d import*

# 1500 X 750 Size Map


from Object_Cupid import Cupid
from Background import Background_Forest
from Object_ObstacleHill import ObstacleHill
from Object_Target import Target
from Object_Arrow import Arrow

def create_world(): #세계 생성
    global cupid, background, target, obstaclehill, arrow_number, arrows
    cupid = Cupid()
    background = Background_Forest()
    target = Target()
    obstaclehill = ObstacleHill()
    arrow_number = 0
    arrows = 0

def destory_world(): #세계 파괴
    global cupid, background, target, obstaclehill
    del(cupid)
    del(background)
    del(obstaclehill)
    del(target)

def enter():
    close_canvas()
    GameFramework.reset_time()
    open_canvas(1500,750)
    create_world()

def exit():
    destory_world()

def update(frame_time):
    global cupid, arrows, arrow_number
    cupid.update(frame_time)



def draw(frame_time):
    global cupid, background, obstaclehill, target

    clear_canvas()
    background.draw()

    cupid.draw()
    cupid.draw_bb()
    target.draw()
    target.draw_bb()
    obstaclehill.draw()
    obstaclehill.draw_bb()


    update_canvas()



def handle_events(frame_time):
    global arrows
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFramework.quit()
        else:
            if (event.type, event.key) ==  (SDL_KEYDOWN, SDLK_ESCAPE):
                close_canvas()
                open_canvas()
                GameFramework.change_state(State_Main)
            elif event.type == SDL_MOUSEBUTTONDOWN:
                if event.key ==  SDL_BUTTON_LEFT:
                    pass

def resume():
    pass

def pause():
    pass

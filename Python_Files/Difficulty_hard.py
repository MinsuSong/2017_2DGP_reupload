import GameFramework
import State_Main
import State_GameOver
import State_Clear
from pico2d import*

# 4500 X 1500 Size Map

from Camera import Camera                       # 카메라

from Object_CupidHard import Cupid              # 큐피드

from BackgroundBig import BackgroundBig         # 4500 x 1500 배경

from Object_ObstacleHillHard import ObstacleHill    # 장애물

from Object_TargetHard import Target            # 타겟

from Object_ArrowHard import Arrow              # 화살객체

from UI_PowerGage import Gage                   # 파워게이지

from UI_lifeHard import Life                    # 라이프

from Object_Cloud import Cloud                  # 구름



def enter():
    close_canvas()
    GameFramework.reset_time()
    open_canvas(1500,750)
    create_world()

### 음악 ###################################################

class BGM:
    def __init__(self):
        self.bgm = load_music('sound\\Hard.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

###########################################################




def create_world(): #세계 생성
    global cupid, target, obstaclehills, arrowlist,gagelist, life, bgm # 수정요함
    global camera, backgroundbig, fire_possible_flag, cloudlist

    camera = Camera()
    backgroundbig = BackgroundBig()

    cupid = Cupid()
    target = Target()
    fire_possible_flag = True

    cloudlist = [Cloud() for i in range(5)]

    ### 장애물 위치 ###

    obstaclehills = []
    obstaclehills.append(ObstacleHill(1400))
    obstaclehills.append(ObstacleHill(750))
    obstaclehills.append(ObstacleHill(1100))
    obstaclehills.append(ObstacleHill(1700))
    obstaclehills.append(ObstacleHill(3200))
    obstaclehills.append(ObstacleHill(2700))
    obstaclehills.append(ObstacleHill(4300))
    ##################

    set_scrolling()

    arrowlist = []
    gagelist = []
    life = Life()
    bgm = BGM()



def destory_world(): #세계 파괴
    global cupid, backgroundbig, target, obstaclehills, arrowlist, gagelist, life #수정요함
    del(cupid)
    del(backgroundbig)
    del(target)
    for obstaclehill in obstaclehills:
        del(obstaclehill)
    for arrow in arrowlist:
        del(arrow)
    arrowlist = []
    gagelist = []
    del(life)

def exit():
    destory_world()


def update(frame_time):
    global cupid, obstaclehills, life, target
    global arrowlist, gagelist, fire_possible_flag, camera, backgroundbig, cloudlist

    backgroundbig.update(frame_time)
    cupid.update(frame_time)


    for arrow in arrowlist:
        arrow.update(frame_time)

        camera.get_arrowposition(arrow)
        backgroundbig.set_camera(camera)

        if (arrow.position_Y < 100):
            arrowlist.remove(arrow)
            camera.mapcamera_flag = True
            fire_possible_flag = True

    for cloud in cloudlist:
        cloud.update(frame_time)



    if life.lifepoint == 0:
        GameFramework.change_state(State_GameOver)

    for obstaclehill in obstaclehills:
        for arrow in arrowlist:

            if collide(arrow, obstaclehill):
                arrow.hit()
                arrowlist.remove(arrow)
                camera.mapcamera_flag = True
                fire_possible_flag = True
                life.decrease()

            elif collide(target, arrow):
                GameFramework.change_state(State_Clear)

            elif (arrow.position_Y < 0):
                arrowlist.remove(arrow)

    for cloud in cloudlist:
        for arrow in arrowlist:

            if collide(arrow, cloud):
                arrow.hit()
                arrowlist.remove(arrow)
                camera.mapcamera_flag = True
                fire_possible_flag = True
                life.decrease()

    for gage in gagelist:
        gage.update(frame_time)




def draw(frame_time):
    global cupid, background, obstaclehills, target, arrowlist, gagelist, life #수정요함

    global backgroundbig, camera
    global cloud
    clear_canvas()

    camera.update(frame_time)
    backgroundbig.draw()

    target.draw()

    for obstaclehill in obstaclehills:
        obstaclehill.draw()

    cupid.draw()

    #########################################################
    for cloud in cloudlist:
        cloud.draw()

    life.draw()

    for gage in gagelist:
        gage.draw(frame_time)

    for arrow in arrowlist:
        arrow.draw(frame_time)


    update_canvas()



def handle_events(frame_time):
    global arrowlist, gagelist, mouse_x, mouse_y, gage
    global camera, fire_possible_flag

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:                                          # 종 료
            GameFramework.quit()


        if (event.type, event.key) ==  (SDL_KEYDOWN, SDLK_ESCAPE):      # 메인화면으로
            close_canvas()
            open_canvas()
            GameFramework.change_state(State_Main)

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT or event.key == SDLK_RIGHT:
                camera.handle_event_camera(event)

        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT or event.key == SDLK_RIGHT:
                camera.handle_event_camera(event)

        if (event.type) == SDL_MOUSEMOTION:  # 마우스 좌표 취득
            mouse_x = event.x
            mouse_y = 750 - event.y

        ################ 마우스 핸들 이벤트 #############################
        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                camera.move_stop()
                camera.mapcamera_flag = False
                if camera.ballcamera_flag == True and fire_possible_flag == True:
                    # 볼 카메라 활성화 준비되었고, 공이 발사 중이 아니면
                    gage = Gage(mouse_x, mouse_y)
                    gagelist.append(gage)

        elif event.type == SDL_MOUSEBUTTONUP:
            if event.button == SDL_BUTTON_LEFT:
                if camera.ballcamera_flag == True and fire_possible_flag == True:
                    camera.reset_camera()
                    arrow = Arrow(gage.level)
                    arrow.set_background(backgroundbig)
                    arrowlist.append(arrow)
                    arrow.firearrow()
                    if gagelist != []:
                        gagelist.remove(gagelist[-1])
                    fire_possible_flag = False

#충돌처리 함수#

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
    pass


def set_scrolling():
    global camera, backgroundbig, target, cupid, obstaclehills
    global cloudlist
    camera.set_background(backgroundbig)  # 카메라 고정
    backgroundbig.set_camera(camera)  # 맵에 카메라 고정
    target.set_background(backgroundbig)  # 타겟 고정
    cupid.set_background(backgroundbig)  # 큐피드 고정
    for obstaclehill in obstaclehills:
        obstaclehill.set_background(backgroundbig)

    for cloud in cloudlist:
        cloud.set_background(backgroundbig)

def resume():
    pass


def pause():
    pass

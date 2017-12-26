from pico2d import*

LEFT , RIGHT = 0,1

class Camera:

    def __init__(self):
        self.x = 1500  / 2
        self.y = 750 / 2
        self.direction = 0
        self.camera_velocity = 0
        self.ballcamera_flag = True    # 볼 카메라 진입 플래그
        self.mapcamera_flag = True      # 맵 카메라 진입 플래그


    ### 키입력 카메라 움직임 ###

    def move_left(self):
        self.direction = LEFT
        self.camera_velocity = -5
        print("test activated")##############################################

    def move_right(self):
        self.direction = RIGHT
        self.camera_velocity = 5
        print("test activated2")#############################################
    def move_stop(self):
        self.camera_velocity = 0
        self.ballcamera_flag = True #### 멈추면 화살을 쏠 수 있다. ####
        print("test activated3")

    def set_background(self, background):
        self.background = background


    def update(self,frame_time):
        if self.mapcamera_flag is True:
            if self.x < 1500 / 2:
                self.x = 1500 / 2
            elif self.x > 4500 - 1500 / 2:
                self.x = 4500 - 1500 / 2
            self.x += self.camera_velocity



    def reset_camera(self):
        self.x = 1500 / 2
        self.y = 750 / 2



    def get_arrowposition(self, arrow):
        self.x = arrow.position_X
        self.y = arrow.position_Y


    ### 카메라 화살표 이동 정의 함수 ###
    def handle_event_camera(self, event):
        if self. mapcamera_flag is True: #### 맵 카메라 플래그가 켜져있으면 ####

            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.move_right()
                    self.ballcamera_flag = False #### 움직이는 중에는 화살을 발사할 수 없게 ####

                if event.key == SDLK_LEFT:
                    self.move_left()
                    self.ballcamera_flag = False #### 움직이는 중에는 화살을 발사할 수 없게 ####

            if event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    if self.direction == RIGHT:
                        self.move_stop()

                elif event.key == SDLK_LEFT:
                    if self.direction == LEFT:
                        self.move_stop()






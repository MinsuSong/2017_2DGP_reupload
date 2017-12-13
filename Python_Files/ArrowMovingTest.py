from pico2d import *
import time

class Arrow:
    image = None
    gravity_accelation = 100 # m/s^2

    meters_per_pixel = 0.01 / 1 # 1pixel 당 1cm



    def __init__(self):

        self.position_x = 0
        self.position_y = 0
        self.velocity_x = 250 # m/s
        self.velocity_y = 200
        self.accelation_x = 0
        self.accelation_y = -Arrow.gravity_accelation
        if Arrow.image == None:
            Arrow.image = load_image('Images\Object\Arrow\Arrow_TEMP.png')

    def draw(self, frame_time):
        self.image.draw(self.position_x, self.position_y)

    def update(self, frame_time):
        self.velocity_x = self.velocity_x + self.accelation_x * frame_time
        self.velocity_y = self.velocity_y + self.accelation_y * frame_time

        self.position_x = self.position_x + frame_time * self.velocity_x
        self.position_y = self.position_y + frame_time * self.velocity_y


    def destroy(self):
        pass


    def handle_events(self, frame_time):
        pass


####### Initiation #######

open_canvas(1500, 700)

running = True

arrowlist = []


def handle_events(frame_time):
    global running,arrowlist

    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_MOUSEBUTTONUP:
            if event.button == SDL_BUTTON_LEFT:
                arrowTEMP = Arrow()
                arrowlist.append(arrowTEMP)


        elif event.type == SDL_QUIT:
            running = False



current_time = get_time()

while (running):
    frame_time = get_time() - current_time
    current_time += frame_time

    clear_canvas()

    for arrow in arrowlist:
        arrow.draw(frame_time)

    handle_events(frame_time)

    for arrow in arrowlist:
        arrow.update(frame_time)



    update_canvas()


close_canvas()

######## Termination ########


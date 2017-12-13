from pico2d import*
import time
open_canvas()

gage = None

class Gage:
    direction_UP = 1
    direction_DOWN = -1
    image = None

    def __init__(self,mouse_x,mouse_y):
        self.position_x = mouse_x
        self.position_y = mouse_y
        self.level = 0
        self.direction = 1
        #if (Gage.image == None):
        Gage.image = load_image('Images\\Interface\\PowerGage\\PowerGage.png')


    def update(self,frame_time):

        if (self.direction == Gage.direction_UP):
            self.level += 50 * frame_time
            if (self.level > 100):
                self.level = 100
                self.direction = Gage.direction_DOWN

        elif (self.direction == Gage.direction_DOWN):
            self.level -= 50 * frame_time
            if (self.level < 0):
                self.level = 0
                self.direction = Gage.direction_UP

    def draw(self, frame_time):
        self.image.draw(self.position_x,self.position_y+self.level/2, 10, self.level)

    def give_powergage(self):
        return self.level

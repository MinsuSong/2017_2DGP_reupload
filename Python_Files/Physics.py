from pico2d import*
import math


def get_mouse_position(event):
    if (event.type == SDL_MOUSEMOTION):
        mouse_x = event.x
        mouse_y = 750-event.y

    return mouse_x, mouse_y


#1 rad = 57.k degree
radian = 180 / math.pi



def get_angle_radian(mouse_x,mouse_y):
    global radian

    angle = math.atan(mouse_y/mouse_x) * radian
    return angle

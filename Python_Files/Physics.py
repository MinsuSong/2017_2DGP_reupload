from pico2d import*

Pixel_Per_Meter = 10 / 0.1

'''
1 픽셀 10cm
10 픽셀 1m
100 픽셀 10m

정사각형 하나 = 100 x 100
중력가속도 G = 4.9 m/s^2 (지구 중력의 1/2)

'''

class Vector_Gravity:

    global Pixel_Per_Meter

    def __init__(self):
        self.x = 0
        self.y = 0


def Vector_DotProduct(vector_a, vector_b): #내적
    pass

def Vector_Plus(vector_a, vector_b): #벡터합
    pass

def Vector_Product(vector_a, vector_b): #벡터곱
    pass

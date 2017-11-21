from pico2d import*


'''
1 픽셀 10cm
10 픽셀 100cm = 1m

정사각형 하나 = 100 x 100
중력가속도 G = 4.9 m/s^2 (지구 중력의 1/2)


2차원 벡터 필요?

x,y 축에서의 이동정의

포물선 운동(외부 물리력 없을 때)
x = v(0) * cos@ * T
y = v(0) * sin@ * T - 1/2 * G * T * T

화살의 처음 속도 
마우스 클릭 유지 시간 == POWER == accelation

속도는 시간 /  거리

v(0)' = v(0) * 


'''


class Arrow:
    image = None

    width = 20 / 2
    height = 20 / 2
    Pixel_Per_Meter = 10 / 0.1 #픽셀 당 미터 10pixel 당 10cm

    gravity_meter_per_secondSquare = -1 # 4.9m/s^2
    gravity_pixel_per_secondSquare = gravity_meter_per_secondSquare * Pixel_Per_Meter


    velocity_meter_per_second = 1 #초속
    velocity_pixel_per_second = Pixel_Per_Meter * velocity_meter_per_second

    def __init__(self):
        self.x = 50
        self.y = 100 + 25/2
        self.velocity = self.velocity_pixel_per_second
        self.image = load_image('Arrow_TEMP.png')


    def update(self, frame_time):
        self.x = self.x + self.velocity * frame_time # 가로방향 등가속도 운동
        self.y = self.y + self.velocity * frame_time + (1/2 * self.gravity_pixel_per_secondSquare * frame_time)  #포물선

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def stop(self):
        self.velocity = 0




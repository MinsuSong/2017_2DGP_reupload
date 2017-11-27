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

    def __init__(self, angle, power):
        #위치
        self.position_X = 50
        self.position_Y = 100
        #힘
        self.power = power
        #속도
        self.velocity_X = self.power * 10
        self.velocity_Y = self.power * 10
        #가속도
        self.accelation_X = 0
        self.accelation_Y = -50
        #발사각
        self.angle = angle
        #파괴용 변수
        self.destroyflag = False
        if Arrow.image == None:
            Arrow.image = load_image('Images\\Object\\Arrow\\Arrow_TEMP.png')

        pass

    def draw(self,frame_time):
        self.image.draw(self.position_X, self.position_Y)

    def update(self,frame_time):
        self.velocity_X= self.velocity_X + self.accelation_X * frame_time
        self.velocity_Y = self.velocity_Y + self.accelation_Y * frame_time

        self.position_X = self.position_X + frame_time * self.velocity_X
        self.position_Y = self.position_Y + frame_time * self.velocity_Y


    def destroy(self):
        pass

    def get_bb(self):
        return self.position_X - Arrow.width, self.position_Y - Arrow.height, self.position_X + Arrow.width, self.position_Y + Arrow.height

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

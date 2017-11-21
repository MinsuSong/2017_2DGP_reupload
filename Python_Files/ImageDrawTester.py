from pico2d import*
import time

import Object_Cupid
import Background

'''
이 py파일은 필기용 / 점검용의 용도를 가지고 있음.


**게임의 정의
가상 세계(게임 세계) 안에서 존재하는 여러 객체들 간의 상호작용을 시뮬레이션 한 것.

**구성 요소

**객체의 정의
객체의 속성

**게임 기본 구조
초기화(initialization)

<게임 루프(반복)>
게임 로직(Logic) 검사 = 게임 세계의 논리/법칙 적용
렌더링(Rendering, Drawing) = 게임 세계 구현(

종료(Termination)

'''



running = True

def enter(): #Scene 진입
    pass
def exit(): #Scene 탈출
    pass
def draw(): #Scene Draw
    pass
def update(): #Scene Update
    pass
def pause(): #Scene Pause
    pass
def resume(): #Scene Resume
    pass
def handle_events():
    pass

def Create_World(): #게임세계 창조 :: 객체 정의
    pass

def Destroy_World(): #게임세계 파괴 :: 컴퓨터 자원 해제
    pass

######################게임 루프###########################

while (running):

    handle_events()

    clear_canvas()
    update_canvas()



import platform
import os


if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"


import GameFramework
from pico2d import*
import State_Logo


GameFramework.run(State_Logo)

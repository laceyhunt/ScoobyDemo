##########
#
# playing with colors
#
##########

from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT
import time

def color(mc):
    time.sleep(2)
    mc.set_color(255,0,0)
    print('red')
    time.sleep(2)
    mc.set_color(0,255,0)
    print('green')
    time.sleep(2)
    mc.set_color(0,0,255)
    print('blue')
    time.sleep(2)
    mc.set_color(0,0,0)
    print('off')

if __name__ == "__main__":
    mc = MyCobot(PI_PORT, 115200)
    try:
        while True:
            color(mc)
    except KeyboardInterrupt:
        print("Program interrupted.")
    finally:
        print("Program is done now.")
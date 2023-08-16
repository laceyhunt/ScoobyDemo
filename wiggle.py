##########
#
# Lacey makes cobot move
#
##########

from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT
import time

speed = 40

def wiggle(mc):
    mc.set_color(0,255,0)
    mc.send_angles([2.54,107.13,-119.09,-55.28,-9.31,180.0], speed)
    #print('1/3 coords sent')

    time.sleep(2)

    mc.send_angles([41.57,-2.98,-27.77,-51.94,-66.0,180.0], speed)
    #print('2/3 coords sent')

    time.sleep(2)

    mc.send_angles([37.96,-129.19,119.09,46.93,62.57,180.0], speed)
    #print('3/3 coords sent')

    time.sleep(2)

    mc.send_angles([0, 0, 0, 0, 0, 0], speed)
    #print('Back to home...')

def bow(mc):
    mc.set_color(0,0,255)
    mc.send_angles([53.43,-17.05,112.06,0,0,180.0], speed)
    #print('Taking a left bow...')
    time.sleep(3)

    mc.send_angles([50.71,-3.42,2.02,0,0,180.0], speed)
    #print('Coming back up...')
    time.sleep(1)

    mc.send_angles([111.7,0,2.02,0,0,180.0], speed)
    #print('Moving to the right...')
    time.sleep(1)

    mc.send_angles([111.7,-28.47, 102.12,11.68,0,180.0], speed)
    #print('Taking a right bow...')
    time.sleep(3)

    mc.send_angles([0, 0, 0, 0, 0, 0], speed)
    #print('Back to home...')


if __name__ == "__main__":
    mc = MyCobot(PI_PORT, 115200)
    mc.set_color(255,0,0)

    try:
        while True:
            # Zero out position 
            mc.send_radians([0, 0, 0, 0, 0, 0], speed)
            #print('Finding home first')
            
            time.sleep(2)

            wiggle(mc)
            bow(mc)
            mc.set_color(255,0,0)
            #print('Done')
    except KeyboardInterrupt:
        print("Program interrupted.")
    finally:
        print("Program is done now.")
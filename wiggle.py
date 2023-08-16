##########
#
# Lacey makes cobot move
#
##########

from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT
import time

def wiggle(mc):
    mc.send_angles([2.54,107.13,-119.09,-55.28,-9.31,180.0], 50)
    print('1/3 coords sent')

    time.sleep(2)

    mc.send_angles([41.57,-2.98,-27.77,-51.94,-66.0,180.0], 50)
    print('2/3 coords sent')

    time.sleep(2)

    mc.send_angles([37.96,-129.19,119.09,46.93,62.57,180.0], 50)
    print('3/3 coords sent')

    # Back to home
    mc.send_angles([0, 0, 0, 0, 0, 0], 50)
    print('Back to home...')



if __name__ == "__main__":
    mc = MyCobot(PI_PORT, 115200)

    # Zero out position 
    mc.send_radians([0, 0, 0, 0, 0, 0], 50)
    print('Finding home first')
    
    time.sleep(2)
    wiggle(mc)
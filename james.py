##########################################################################
#
# James Playes with cobots assignment
#
# Radian coords are cool
#
##########################################################################

from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT
import time

PI = 3.14

def grabby_claw(mc):
    mc.send_radians([-PI/2, PI/2, 0, 0, 0, PI/2], 50)
    print('Coords sent')

    time.sleep(2)

    # Close Gripper
    mc.set_gripper_state(1, 50)

    time.sleep(2)

    mc.send_radians([-PI/2, PI/4, 0, 0, 0, PI/2], 50)
    print('Coords sent')

    time.sleep(2)

    mc.send_radians([-PI/4, PI/4, 0, 0, 0, PI/2], 50)
    print('Coords sent')

    time.sleep(2)

    mc.send_radians([-PI/4, PI/2, 0, 0, 0, PI/2], 50)

    time.sleep(2)

    # Open Gripper
    mc.set_gripper_state(0, 50)

    time.sleep(2)

    # Back to home
    mc.send_radians([0, 0, 0, 0, 0, 0], 50)


if __name__ == "__main__":
    mc = MyCobot(PI_PORT, 115200)

    # Zero out position 
    mc.send_radians([0, 0, 0, 0, 0, 0], 50)

    # Open Gripper
    mc.set_gripper_state(0, 50)
    
    time.sleep(3)
    grabby_claw(mc)


from pymycobot.mycobot import MyCobot

from pymycobot import PI_PORT, PI_BAUD
from pymycobot.genre import  Angle
import time

#mc = MyCobot(PI_PORT, PI_BAUD)
mc = MyCobot(PI_PORT, 115200)

if mc.is_controller_connected() != 1:
	print("Please connect the robot arm correctly for program writing")
	exit(0)

mc.send_angles([0,0,0,0,0,0], 50)
time.sleep(10)

mc.send_angles([90,45,-90,90,-90,90], 50)
time.sleep(3)

mc.send_angles([0,0,0,0,0,0], 50)
time.sleep(3)

mc.send_angles([-90,-45,90,-90,90,-90], 50)
time.sleep(3)

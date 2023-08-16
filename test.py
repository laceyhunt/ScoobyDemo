from pymycobot.mycobot import MyCobot

from pymycobot import PI_PORT, PI_BAUD
from pymycobot.genre import  Angle
import time

#mc = MyCobot(PI_PORT, PI_BAUD)
mc = MyCobot(PI_PORT, 115200)

if mc.is_controller_connected() != 1:
	print("Please connect the robot arm correctly for program writing")
	exit(0)

mc.send_angles([0,0,0,0,0,0], 40)
time.sleep(3)

mc.send_angle(Angle.J3.value, 70, 40)
time.sleep(3)
mc.send_angle(Angle.J4.value, -70, 40)
time.sleep(3)

mc.send_angle(Angle.J1.value, 90, 40)
time.sleep(3)

mc.send_angle(Angle.J5.value, -90, 40)
time.sleep(3)

mc.send_angle(Angle.J5.value, 90, 40)
time.sleep(3)


#i = 7
#while i > 0:
#	mc.set_color(0,0,255)
#	time.sleep(2)
#	mc.set_color(255,0,0)
#	time.sleep(2)
#	mc.set_color(0,255,0)
#	time.sleep(2)
#	i -= 1

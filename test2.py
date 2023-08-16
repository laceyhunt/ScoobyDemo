from pymycobot.mycobot import MyCobot

from pymycobot import PI_PORT, PI_BAUD
from pymycobot.genre import  Angle
import time

#mc = MyCobot(PI_PORT, PI_BAUD)
mc = MyCobot(PI_PORT, 115200)

if mc.is_controller_connected() != 1:
	print("Please connect the robot arm correctly for program writing")
	exit(0)


angle_data = mc.get_angles()
print("Angle Data:", angle_data)

mc.send_angles([0,0,0,0,0,0], 50)
print(mc.is_paused())
time.sleep(2.5)

mc.send_angle(Angle.J1.value, 90, 50)
time.sleep(2)

num = 5
while num > 0:
	mc.send_angle(Angle.J2.value, 50, 50)
	time.sleep(1.5)
	mc.send_angle(Angle.J2.value, -50, 50)
	time.sleep(1.5)
	num -=1 


mc.send_angles([88.68, -138.51, 155.65, -128.05, -9.93, -15.29], 50)
time.sleep(2.5)

mc.release_all_servos()
time.sleep(10)

from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT

mc = MyCobot(PI_PORT, 115200)
mc.send_radians([0, 0, 0, 0, 0, 0], 50)
print('Coords sent')


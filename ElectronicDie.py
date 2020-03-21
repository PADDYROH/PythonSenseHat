#ElectronicDie
from sense_hat import SenseHat
import time
import random
sense = SenseHat()

class die:
    def __init__(self,sense):
        self.sense = sense
    
    def roll(self):
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x=round(x,0)
        y=round(y,0)
        z=round(z,0)
        print("x=%s, y=%s, z=%s" %(x,y,z))
        return x,y,z
    
    def shake(self,x,y,z):
        if x !=0 or y!=0 or z!=1:
                num = random.randint(1,7)
                return print(num)


d1 = die(sense)

while True:
    x,y,z = d1.roll()
    time.sleep(1)
    d1.shake(x,y,z)
    time.sleep(1)

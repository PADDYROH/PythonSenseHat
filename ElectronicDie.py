#ElectronicDie
from sense_hat import SenseHat
import time
import random
sense = SenseHat()

class die:
    def __init__(self,sense):
        self.sense = sense
    
    def accel(self):
        acceleration = self.sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        
        x = abs(x)
        y = abs(y)
        z = abs(z)
        
        print("x=%s, y=%s, z=%s" %(x,y,z))
        return x,y,z
    
    def shake(self):
        x,y,z = self.accel()
        if x >1 or y>1 or z>1:
                num = random.randint(1,6)
                self.sense.show_message(str(num))
                return num


d1 = die(sense)

while True:
    d1.shake()

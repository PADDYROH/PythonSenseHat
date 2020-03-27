#ElectronicDie
from sense_hat import SenseHat
import time
import random

class die:
    def __init__(self,sense,total):
        self.sense = SenseHat()
        self.total = total
    
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
            return print(num)

    def check(self):
        if x >1 or y>1 or z>1:
            return True
        else:
            return False

    def score(self):
        total = self.shake()
        return total 

total = 0
d1 = die(sense)
while d1.check() = False:
    d1.shake()
    
d1.total()



#ElectronicDie
from sense_hat import SenseHat
import time
import random
from datetime import datetime
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
                num1 = random.uniform(3,6)
                num2 = random.uniform(1,3)
                num = random.randint(int(num2),int(num1))
                self.sense.show_message(str(num))
                time.sleep(2)
                return num


d1 = die(sense)

while True:
    d1.shake()

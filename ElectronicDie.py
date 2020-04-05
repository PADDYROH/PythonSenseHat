from sense_hat import SenseHat
import time
import random
from datetime import datetime


class die:
    def __init__(self):
        self.sense_hat = SenseHat()
        self.__score = None
    
    def accel(self):
        acceleration = self.sense_hat.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        
        x = abs(x)
        y = abs(y)
        z = abs(z)
        #return values of acceleration from raspberry pi
        return x,y,z
    
    def shake(self):
        x,y,z = self.accel()
        #once pi reaches an acceleration, it will return die roll value 
        if x >2 or y>2 or z>2:
                self.__dieRoll = random.randrange(1,6)
                self.sense_hat.show_message(str(self.__dieRoll), text_colour =(0,255,0))
                return self.__dieRoll

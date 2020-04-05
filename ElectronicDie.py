#ElectronicDie
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
        
        return x,y,z
    
    def shake(self):
        x,y,z = self.accel()
        if x >2 or y>2 or z>2:
                self.__scorescore = random.randrange(1,6)
                self.sense_hat.show_message(str(self.__scorescore))
                print ("dice rolled : " + str(self.__scorescore))
                return self.__scorescore
            




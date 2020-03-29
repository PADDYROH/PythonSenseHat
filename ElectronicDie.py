#ElectronicDie
from sense_hat import SenseHat
import time
import random
from datetime import datetime
sense = SenseHat()

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
        if x >1 or y>1 or z>1:
                num1 = random.uniform(3,6)
                num2 = random.uniform(1,3)
                self.__scorescore = random.randint(int(num2),int(num1))
                self.sense_hat.show_message(str(self.__scorescore))
                print ("dice rolled : " + str(self.__scorescore))
                return self.__scorescore
            
die()



#animatedEmoji
from sense_hat import SenseHat
import time

class main:
    sense=SenseHat()

    w = (255,255,255)
    y = (255,255,0)
    b = (0,0,255)
    r = (255,0,0)
    o = (0,0,0)

    happy=[
        o,o,o,o,o,o,o,o,
        o,w,w,o,o,w,w,o,
        o,w,r,o,o,w,r,o,
        o,o,o,o,o,o,o,o,
        o,y,o,o,o,o,y,o,
        o,y,o,o,o,o,y,o,
        o,o,y,y,y,y,o,o,
        o,o,o,o,o,o,o,o,
        ]
        
    
    sad=[
        o,o,o,o,o,o,o,o,
        o,w,b,o,o,w,b,o,
        o,w,w,o,o,w,w,o,
        o,o,o,o,o,o,o,o,
        o,o,y,y,y,y,o,o,
        o,y,o,o,o,o,y,o,
        o,y,o,o,o,o,y,o,
        o,o,o,o,o,o,o,o,
        ]
                
    meh=[
        o,o,o,o,o,o,o,o,
        o,w,w,o,o,w,w,o,
        o,w,r,o,o,r,w,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,y,y,y,y,y,y,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        ]

    e1 = EmojiFace(sense,happy)
    e2 = EmojiFace(sense,meh)
    e3 = EmojiFace(sense,sad) 

while True:
    e1.displayFace()
    e2.displayFace()
    e3.displayFace()


class EmojiFace:

    #initialize attributes
    def __init__(self,sense,emoji):
        self.sense = sense
        self.emoji = emoji
    
    def displayFace(self):
        self.sense.set_pixels(self.emoji)

            

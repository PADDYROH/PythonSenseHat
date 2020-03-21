#animatedEmoji
from sense_hat import SenseHat
import time



sense=SenseHat()
class EmojiFace:

    #initialize attributes
    def __init__(self,sense,emoji):
        self.sense = sense
        self.emoji = emoji
    
    def displayFace(self):
        self.sense.set_pixels(self.emoji)
            
y = (255,255,0)
b = (0,0,255)
r = (255,0,0)
o = (0,0,0)
happy=[
    o,o,o,o,o,o,o,o,
    o,y,y,o,o,y,y,o,
    o,y,y,o,o,y,y,o,
    o,o,o,o,o,o,o,o,
    o,y,o,o,o,o,y,o,
    o,y,o,o,o,o,y,o,
    o,o,y,y,y,y,o,o,
    o,o,o,o,o,o,o,o,
    ]
        
    
sad=[
    o,o,o,o,o,o,o,o,
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o,
    o,o,o,o,o,o,o,o,
    o,o,b,b,b,b,o,o,
    o,b,o,o,o,o,b,o,
    o,b,o,o,o,o,b,o,
    o,o,o,o,o,o,o,o,
    ]
            
meh=[
    o,o,o,o,o,o,o,o,
    o,r,r,o,o,r,r,o,
    o,r,r,o,o,r,r,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,r,r,r,r,r,r,o,
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

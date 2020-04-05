#animatedEmoji
from sense_hat import SenseHat
import time

class Emoji:
    #initialize attributes
    def __init__(self,sense,emoji):
        self.sense = SenseHat()
        self.emoji = emoji
    
    #display on sense hat 
    def displayFace(self):
        self.sense.set_pixels(self.emoji)

    #inherit Face methods
class Face(Emoji):
    #colours
    w = (255,255,255)
    y = (255,255,0)
    r = (255,0,0)
    g = (0,255,0)
    b = (0,0,255)
    o = (0,0,0)

#faces
    happy=[
        o,o,o,o,o,o,o,o,
        o,g,w,o,o,g,w,o,
        o,w,w,o,o,w,w,o,
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
                   
    neutral=[
        o,o,o,o,o,o,o,o,
        o,w,w,o,o,w,w,o,
        o,w,r,o,o,r,w,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,y,y,y,y,y,y,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        ]
            
        # emojiface objects
    emoji1 = Emoji(sense,happy)
    emoji2 = Emoji(sense,sad)
    emoji3 = Emoji(sense,neutral) 

        # display objects
    while True:
        emoji1.displayFace()
        time.sleep(3)
        emoji2.displayFace()
        time.sleep(3)
        emoji3.displayFace()
        time.sleep(3)

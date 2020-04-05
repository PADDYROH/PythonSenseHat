#animatedEmoji
from sense_hat import SenseHat
import time

class Emoji:
    #initialize attributes
    def __init__(self,emoji):
        self.sense = SenseHat()
        self.emoji = emoji
    
    #display on sense hat 
    def set_new_emoji(self):
        self.sense.set_pixels(self.emoji)

class Face:

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
          
    def display_emojis(self):
    
        emoji1 = Emoji(self.happy)
        emoji2 = Emoji(self.sad)
        emoji3 = Emoji(self.neutral) 

            # display objects
        while True:
            emoji1.set_new_emoji()
            time.sleep(3)
            emoji2.set_new_emoji()
            time.sleep(3)
            emoji3.set_new_emoji()
            time.sleep(3)

Face().display_emojis()

#animatedEmoji
from sense_hat import SenseHat
import time

sense=SenseHat()
class EmojiFace:

    #initialize attributes
    def init(self,emoji):
        self.emoji = emoji

    def change(self,emoji):
        y = (255,255,0)
        b = (0,0,255)
        r = (255,0,0)
        o = (0,0,0)
        if emoji == "happyface":
            Img=[
                o,o,o,o,o,o,o,o,
                o,y,y,o,o,y,y,o,
                o,y,y,o,o,y,y,o,
                o,o,o,o,o,o,o,o,
                o,y,o,o,o,o,y,o,
                o,y,o,o,o,o,y,o,
                o,o,y,y,y,y,o,o,
                o,o,o,o,o,o,o,o,
                ]
            return Img
        elif emoji == "sadface":
            Img=[
                o,o,o,o,o,o,o,o,
                o,b,b,o,o,b,b,o,
                o,b,b,o,o,b,b,o,
                o,o,o,o,o,o,o,o,
                o,o,b,b,b,b,o,o,
                o,b,o,o,o,o,b,o,
                o,b,o,o,o,o,b,o,
                o,o,o,o,o,o,o,o,
                ]
            return Img
        elif emoji == "mehface":
            Img=[
                o,o,o,o,o,o,o,o,
                o,r,r,o,o,r,r,o,
                o,r,r,o,o,r,r,o,
                o,o,o,o,o,o,o,o,
                o,o,o,o,o,o,o,o,
                o,r,r,r,r,r,r,o,
                o,o,o,o,o,o,o,o,
                o,o,o,o,o,o,o,o,
                ]
            return Img

e1 = EmojiFace()
sense.set_pixels(e1.change("sadface"))
#sense.set_pixels(e1.change("happyface"))
#sense.set_pixels(e1.change("mehface"))

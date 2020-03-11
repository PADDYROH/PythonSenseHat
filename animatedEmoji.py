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

e1 = EmojiFace()
e1.change("sadface")
print(e1.change("sadface"))
count = 0
while True:
    sense.set_pixels(e1[count % 64]())
    count +=1

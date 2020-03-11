#animatedEmoji
from sense_hat import SenseHat
import time

sense=SenseHat()

yellow = (255,255,0)
blue = (0,0,255)
off = (0,0,0)

def happyFace():
    y=yellow
    o=off
    emoji=[
        o,o,o,o,o,o,o,o
        o,y,y,o,o,y,y,o
        o,y,y,o,o,y,y,o
        o,o,o,o,o,o,o,o
        o,y,o,o,o,o,y,o
        o,y,o,o,o,o,y,o
        o,o,y,y,y,y,o,o
        o,o,o,o,o,o,o,o
    ]
    return emoji

def sadFace():
    b=blue
    o=off
    emoji=[
        o,o,o,o,o,o,o,o
        o,b,b,o,o,b,b,o
        o,b,b,o,o,b,b,o
        o,o,o,o,o,o,o,o
        o,o,b,b,b,b,o,o
        o,b,o,o,o,o,b,o
        o,b,o,o,o,o,b,o
        o,o,o,o,o,o,o,o
    ]
    return emoji

emojis=[happyFace, sadFace]
count=0
while true:
    sense.set_pixels(emojis[count % len(emojis)]())
    time.sleep(3)
    count+=1 
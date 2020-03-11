import Emoji
import time


from sense_hat import SenseHat

sense = SenseHat()

emoji = Emoji.Emoji(sense)


while 1 :
	emoji.display_emoji("penis")
	time.sleep(3)
	emoji.display_emoji("invader")
	time.sleep(3)
	emoji.display_emoji("frown")
	time.sleep(3)



class Emoji: 
	def __init__(self,sense_hat):
		self.sense_hat = sense_hat
	

	def display_emoji(self,emoji):
		
		if emoji == "frown":
			self.sense_hat.set_pixels(self.frown)
		elif emoji == "smiley":
			self.sense_hat.set_pixels(self.smiley)
		elif emoji == "invader":
			self.sense_hat.set_pixels(self.invader)
		else:
			self.sense_hat.display_message("Emoji does not exist")




	X = [255, 0, 0]  # Red
	O = [255, 255, 255]  # White

	o = [255, 102, 178]  # Red
	x = [76, 153, 0]  # White


	smiley = [
	O, O, O, O, O, O, O, O,
	O, O, X, O, O, X, O, O,
	O, O, X, O, O, X, O, O,
	O, O, O, O, O, O, O, O,
	O, X, O, O, O, O, X, O,
	O, O, X, X, X, X, O, O,
	O, O, O, O, O, O, O, O,
	O, O, O, O, O, O, O, O
	]

	frown = [
	O, O, O, O, O, O, O, O,
	O, X, O, O, O, O, X, O,
	O, O, X, O, O, X, O, O,
	O, O, O, O, O, O, O, O,
	O, O, O, O, O, O, O, O,
	O, X, X, X, X, X, X, O,
	O, X, O, O, O, O, X, O,
	O, O, O, O, O, O, O, O
	]

	invader = [
	o,o,x,x,x,x,o,o,
    o,o,x,x,x,x,o,o,
    o,o,x,x,x,x,o,o,
    o,o,x,x,x,x,o,o,
    o,x,x,x,x,x,x,o,
    o,x,o,o,o,o,x,o,
    o,x,o,o,o,o,x,o,
    o,x,x,o,o,x,x,o,
	]


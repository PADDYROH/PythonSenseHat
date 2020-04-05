from Player import *
import ElectronicDie
import time
from datetime import datetime
import csv
from sense_hat import SenseHat


class Game:

	NUM_PLAYERS = 2
	WINING_SCORE = 30
	SCROLL_SPEED = 0.05



	def __init__(self):
		self.__game_running = True
		self.__players = []
		self.winning_player = None
		self.sense = SenseHat()


	def __add_players(self):
		x = 1
		while x <= Game.NUM_PLAYERS:
			self.__players.append(Player(x))
			x += 1	

	def check_for_winner(self):
		winner = False
		for player in self.__players:
			if player.get_score() >= Game.WINING_SCORE:
				winner = True
				self.winning_player = player
		if winner:
			self.sense.show_message("Player " + str(self.winning_player.get_name()) + " has won the game !!!", scroll_speed= Game.SCROLL_SPEED)
			self.__game_running = False

		return winner

	def write_to_file(self):
	    csvWinner = open('winner.csv', 'r')
	    file_content = csvWinner.read()
	    csvWinner.close()
	    if file_content == "":
            #Writing fields (player, score, time) to csv file
	        csvWinner = open('winner.csv', 'a')
	        fieldnames = ['player','score','time']
	        writeHeader= csv.DictWriter(csvWinner,fieldnames=fieldnames)
	        writeHeader.writeheader()
	        csvWinner.close()
	    
	    #Writing new game winner to csv file
	    csvWinner = open('winner.csv', 'a')
	    with csvWinner:
	        writer= csv.writer(csvWinner)
	        now = datetime.now()
	        date = now.strftime("%m/%d/%y, %H:%M:%S")
	        game = [str(self.winning_player.get_name()),str(self.winning_player.get_score()), date]
	        writer.writerow(game)
	        csvWinner.close()

	def play_game(self):	

		self.sense.show_message(" Welcome to the die game first to "+ str(Game.WINING_SCORE) +" wins ", scroll_speed= Game.SCROLL_SPEED)

		time.sleep(2)

		game_dice = ElectronicDie.die()

		self.__add_players()

		dice_value = None

		while self.__game_running:
			for player in self.__players:
				self.sense.show_message("Player " + str(player.get_name()) + " : " + " shake the die", scroll_speed= Game.SCROLL_SPEED)
				
				#Player shakes die
				while dice_value is None:
					dice_value = game_dice.shake()

				player.add_to_score(dice_value)

				self.sense.show_message("player "+ str(player.get_name()) +" score : " + str(player.get_score()), scroll_speed= Game.SCROLL_SPEED)

				if self.check_for_winner():
					self.write_to_file()
					break

				time.sleep(2)

				
				dice_value = None

Game().play_game()

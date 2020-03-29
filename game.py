from Player import *
import ElectronicDie
import time
from datetime import datetime
import csv


class Game:

	NUM_PLAYERS = 2
	WINING_SCORE = 4



	def __init__(self):
		self.__game_running = True
		self.__players = []
		self.winning_player = None


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
			print("Player " + str(self.winning_player.get_name()) + " has won the game !!!")
			self.__game_running = False

		return winner

	def write_to_file(self):
	    csvWinner = open('winner.csv', 'r')
	    file_content = csvWinner.read()
	    csvWinner.close()
	    if file_content == "":
	        csvWinner = open('winner.csv', 'a')
	        #Writing fileds (player, score, time) to csv file
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

		print(" Welcome to the die game first to "+ str(Game.WINING_SCORE) +" wins ")

		time.sleep(2)

		game_dice = ElectronicDie.die()

		self.__add_players()

		dice_value = None

		while self.__game_running:
			for player in self.__players:
				print("Player " + str(player.get_name()) + " : " + " it's your turn to shake the die")
				while dice_value is None:
					dice_value = game_dice.shake()

				player.add_to_score(dice_value)

				print("player "+ str(player.get_name()) +" score is now " + str(player.get_score()))

				if self.check_for_winner():
					self.write_to_file()
					break

				time.sleep(2)

				
				dice_value = None






Game().play_game()




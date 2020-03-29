from Player import *
import ElectronicDie
import csv

class Game:

	NUM_PLAYERS = 2
	WINING_SCORE = 30



	def __init__(self):
		self.__game_running = True
		self.__players = []

	def __add_players(self):
		for x in range(0, Game.NUM_PLAYERS):
			self.__players.append(Player(x))	

	def check_for_winner(self):
		winner = False
		for player in self.__players:
			if player.get_score() >= Game.WINING_SCORE:
				winner = True
		return winner

	def play_game(self):	
		game_dice = die()
		self.__add_players()
		dice_value = None

		while self.__game_running:
			for player in self.__players:
				die().shake()
				# add point to score
				player.add_to_score(dice_value)
				# check total
				self.check_for_winner()
					# if player wins
					# display winning message
					# add player to csv (time, winning score)
					a = 1
					if a = 2:
						myFile = open('winner.csv', 'w')
						with myFile:
							writer= csv.writer(myFile)
							writer.writerows(player)
				# change player
				dice_value = None

Game().play_game()
from Player import *
import ElectronicDie
import time

class Game:

	NUM_PLAYERS = 2
	WINING_SCORE = 10



	def __init__(self):
		self.__game_running = True
		self.__players = []

	def __add_players(self):
		x = 1
		while x <= Game.NUM_PLAYERS:
			self.__players.append(Player(x))
			x += 1	

	def check_for_winner(self):
		winning_player = None
		winner = False
		for player in self.__players:
			if player.get_score() >= Game.WINING_SCORE:
				winner = True
				winning_player = player
		if winner:
			print("Player " + str(winning_player.get_name()) + " has won the game !!!")
			self.__game_running = False

		return winner

	def play_game(self):	

		print(" Welcome to the die game first to 30 wins ")

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
					break

				time.sleep(2)

				
				dice_value = None



Game().play_game()




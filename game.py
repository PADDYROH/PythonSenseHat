from Player import *
import ElectronicDie

class Game:

	NUM_PLAYERS = 2
	WINING_SCORE = 10



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
		if winner:
			self.__game_running = False

	def play_game(self):	

		game_dice = ElectronicDie.die()

		self.__add_players()

		dice_value = None


		while self.__game_running:
			for player in self.__players:
				print("Player : " + str(player.get_name()) + " turn")
				print("shake die")
				while dice_value is None:
					dice_value = game_dice.shake()

				player.add_to_score(dice_value)

				print("players score" + str(player.get_score()))

				self.check_for_winner()
				
				dice_value = None



Game().play_game()




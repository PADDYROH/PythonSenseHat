#game
from Player import *

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

	def __shake(self,Player):
		print("not finsihed")
		# call electronicDie.shake()
		# add points to player


	def play_game(self):
		self.__add_players()

		while self.__game_running:
			for player in self.__players:
				self.__shake(player)

game = Game()

game.play_game()
game.check_for_winner()
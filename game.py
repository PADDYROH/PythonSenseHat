from Player import *
import ElectronicDie
import time
import datetime
import csv

class Game:

    NUM_PLAYERS = 2
    WINING_SCORE = 10



    def __init__(self):
        self.__game_running = True
        self.__players = []
        self.winning_player =None

    def __add_players(self):
        x = 1
        while x <= Game.NUM_PLAYERS:
            self.__players.append(Player(x))
            x += 1  

    def write_to_file(self,player):
        csvWinner = open('winner.csv', 'a')
        with csvWinner:
            #write header
            #fieldnames = ['player','score','time']
            #writeHeader= csv.DictWriter(csvWinner,fieldnames=fieldnames)
            #writeHeader.writeheader()
            #write winner
            writer= csv.writer(csvWinner)
            #player, score, time
            date = datetime.date.today()
            game = [str(self.winning_player.get_name()),str(self.winning_player.get_score()), str(date)]
            writer.writerow(game)
            

    def check_for_winner(self):
        winner = False
        for player in self.__players:
            if player.get_score() >= Game.WINING_SCORE:
                winner = True
                self.winning_player = player
        if winner:
            print(str(self.winning_player.get_name()) + " has won the game !!!")
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
                    self.write_to_file(player)
                    break

                time.sleep(2)

                
                dice_value = None
        



Game().play_game()
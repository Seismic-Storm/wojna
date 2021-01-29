# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 00:23:35 2021
@author: Helena Ciechowska
"""
from Deck import Deck

class Player:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def play(self, player1, player2):
        return player1.pop(0), player2.pop(0)


    def take(self, karty, winner):
        winner += karty

    def winner(self, final_player1, final_player2):
        if len(final_player1) == 0:
            print('The winner is Player 2! \nCongratulations!')
            return True
        elif len(final_player2) == 0:
            print('The winnwe is Player 1! \nCongratulations!')
            return True
        else:
            return False

# self.final_player1 =
# self.final_player2 =




if __name__ == '__main__':
    dek = Deck()
    print(len(dek.deck))
    p1, p2 = dek.Deal()
    player = Player()
    player.play(p1, p2)

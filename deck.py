import random
from random import randint
from random import shuffle

class Deck:

    def __innit__(self):
        self.deck = deck
            

    def Create_Deck():
        deck = [i for i in range(52)]
        return deck
    
    def __str__(self):
        result = ""
        for i in len(deck):
            result += deck[i]
        print(result)


    def Deal(self):
        player1= []
        player2 = []
        while len(player1) < 27:
            r = randint(0,51)
            if not(r in player1):
                player1.append(r)
        for i in range(0,51):
            if not(i in player1):
                player2.append(i)
        random.shuffle(player2)
        return player1, player2




#print(Deck.Deal())
deck= Deck.Create_Deck()
Deck.Deal(deck)
print(deck)
print(Deck.Deal(deck))
#print(deck)


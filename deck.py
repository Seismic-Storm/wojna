import random
from random import randint, shuffle

class Deck:

    def __init__(self):
        self.deck = [i for i in range(52)]
        random.shuffle(self.deck)
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "WALET", "DAMA", "KROl", "AS"]
        signs = ["♥", "♦", "♣", "♠"]
        self.allcards = []
        for i in range(len(values)):
            for j in range(len(signs)):
                self.allcards.append(str(values[i]) + str(signs[j]))


   
    def Deal(self):
        player1 = []
        player2 = []
        for i in range(26):
            player1.append(self.deck[i])
        player2 = []
        for j in range(26,52):
            player2.append(self.deck[j])
        self.deck =(player1, player2)
        return self.deck


    def slowo(self):

        cards1 = self.deck[0]
        cards2 = self.deck[1]
        result = []
        result.append("gracz1:")
        for i in range(len(cards1)):
            result.append(self.Karta(int(cards1[i])))

        result.append("gracz2:")
        for j in range(len(cards2)):
            result.append(self.Karta(int(cards2[j])))

        return result


    def Karta(self, num):
        karta = ""
        karta += self.allcards[num]
        return karta



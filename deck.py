#Creating the Cards

import random
#Deck class

import random
from card import Card

class buildDeck:
    def __init__(self):
        self.deck = []
        self.generate()

    def generate(self):
        for suit in ["S", "C", "D", "H"]:
            for face in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.deck.append(Card(suit, face))

    def shuffle(self):
        for i in range(len(self.deck)-1, 0, -1):
            r = random.randint(0, i)
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]

    def show(self):
        for card in self.deck:
            card.show()

    def draw(self, times=1):
        for i in range(times):
            return self.deck.pop()


#test = buildDeck()
#test.shuffle()
#test.show()
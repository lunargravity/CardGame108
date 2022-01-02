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
        return self.deck

    def show(self):
        for card in self.deck:
            card.show()

    def draw(self, times=1):
        for i in range(times):
            return self.deck.pop()

    def remove(self, card):
        for c in self.deck:
            if card.show() == c.show():
                self.deck.remove(c)

    def __len__(self):
        return len(self.deck)



#test = buildDeck()
#test.shuffle()
#print(len(test))
#testcard = Card("S", "2")
#test.remove(testcard)
#print(len(test))
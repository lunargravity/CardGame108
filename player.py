#Player Class

from deck import buildDeck
from card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, times=1):
        for i in range(times):
            self.hand.append(deck.draw())
        return self

    def show(self):
        for card in self.hand:
            card.show()

#deck = buildDeck()
#deck.shuffle()
#tester = Player("dummy")
#tester.draw(deck)
#tester.show()



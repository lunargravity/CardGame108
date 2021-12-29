#Player Class

from deck import buildDeck
from card import Card

class Player:
    def __init__(self, name):
        self.name = name.title()
        self.hand = []

    def draw(self, deck, times=1):
        for i in range(times):
            self.hand.append(deck.draw())
        return self

    def show(self):
        hand = ""
        print("{name}'s cards:".format(name=self.name))
        for card in self.hand:
            hand += "|" + str(card.show()) + "|"
        print(hand)

deck = buildDeck()
deck.shuffle()
tester = Player("dummy")
tester.draw(deck, 5)
tester.show()



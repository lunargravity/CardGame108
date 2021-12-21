#Player Class

from deck import buildDeck
from card import Card

class Player:
    def __init__(self, name = "Player", isPlayer = True, deck = None):
        player = name.title()
        self.name = player
        self.hand = []
        self.isPlayer = isPlayer
        self.deck = deck
        self.points = 0

    def draw_card(self, times = 1):
        self.hand.extend(self.deck.draw(times))

    def check_points(self):
        counter = 0
        self.points = 0
        for card in self.hand:
            self.points += card.points
        return self.points

    def play_card(self):
        pass

    def show(self):
        hand = ""
        if self.isPlayer:
            print("{name}'s cards: ").format(name=self.name)
            for card in self.hand:
                hand += "|" + str(display_card(card))
        else:
            print("Computer's cards: ")
            print(str(len(self.hand)) + " cards")




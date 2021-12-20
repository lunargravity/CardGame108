from deck import buildDeck
from player import Player

class Game:
    def __init__(self):
        self.deck = buildDeck()
        self.deck.generate()
        self.player = Player()
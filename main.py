from deck import buildDeck
from player import Player

class Game:
    def __init__(self):
        self.deck = buildDeck()
        self.deck.generate()
        player = input("What's your name?")
        self.player = Player(player, True, self.deck)
        self.computer = Player("Computer", False, self.deck)

    def start(self):
        p_status = self.player.draw(5)
        d_status = self.computer.draw(5)

        self.player.show()
        self.computer.show()

newgame = Game()
newgame.start
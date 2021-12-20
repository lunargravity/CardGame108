#Player Class

from deck import buildDeck

class Player:
    def __init__(self, name, isPlayer, deck):
        player = name.upper()
        self.name = player
        self.hand = []
        self.isPlayer = isPlayer
        self.deck = deck
        self.points = 0

    def draw(self, times):
        self.hand.extend(self.deck.draw(times))

    def check_points(self):
        counter = 0
        self.points = 0
        for card in self.hand:
            self.points += card.points
        return self.points

    def show(self):
        if self.isPlayer:
            print("{name}'s cards: ").format(name=self.name)
        else:
            print("Computer's cards:")

        for cards in self.hand:
            cards.show()

        print("Score: " + str(self.points))
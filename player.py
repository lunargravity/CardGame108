#Player Class

from deck import buildDeck
from card import Card
from main import *

class Player:
    def __init__(self, name, brain = "CPU"):
        self.name = name
        self.hand = []
        self.brain = brain
        self.score = 0

    def draw(self, deck, times=1):
        for i in range(times):
            self.hand.append(deck.draw())
        return self

    def add_points(self):
        counter = 0
        for card in self.hand:
            self.score += card.points
        return self.score
    
    def check_score(self):
        return self.score
        print(self.score)

    def show(self):
        hand = ""
        print("{name}'s cards:".format(name=self.name))
        for card in self.hand:
            hand += "|" + str(card.show()) + "|"
        print(hand)

    def cpu_show(self):
        print("{name}'s cards: {num}".format(name=self.name, num=int(len(self.hand))))

    
        


#deck = buildDeck()
#deck.shuffle()
#tester = Player("bob", True)
#tester.draw(deck, 5)
#tester.show() 
#tester.add_points
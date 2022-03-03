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
        for card in self.hand:
            self.score += card.points
        if self.score == 108:
            self.score = int(self.score / 2)
            return self.score
        else:
            return self.score
    
    def check_score(self):
        print(self.score)
        return self.score

    def show(self):
        print("{}'s cards:".format(self.name))
        a = ""
        b = ""
        c = ""

        for card in self.hand:
            if card.suit == "S":
                symbol = "♠"
            elif card.suit == "H":
                symbol = "♥"
            elif card.suit == "D":
                symbol = "♦"
            else:
                symbol = "♣"

            a += "┌────┐"
            b += ("|{:<2} {}|").format(card.face, symbol)
            c += "└────┘"

        print(a)
        print(b)
        print(c)

    def cpu_show(self):
        print("{name}'s cards: {num}".format(name=self.name, num=int(len(self.hand))))


#When testing, comment out import main, otherwise it will run the program twice

#deck = buildDeck()
#deck.shuffle()
#tester = Player("bob", "Human")
#tester.score = 108
#print(tester.score)
#tester.add_points()
#tester.check_score()
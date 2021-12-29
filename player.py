#Player Class

from deck import buildDeck
from card import Card

class Player:
    def __init__(self, name, isPlayer = True):
        self.name = name.title()
        self.isPlayer = isPlayer
        self.hand = []
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
        print(self.score)

    def clear_hand(self):
        self.hand = []

    def action(self):
        action = input("Action: ").upper()
        for card in self.hand:
            if card.show() == action:
                self.hand.remove(card)
                self.show()
                break
            else:
                if action == "D":
                    self.draw(deck, 1)
                    self.show()
                    break
                elif action == "P":
                    #Make it the next player's turn
                    print("passes to next player")
                    break
                elif action == "S":
                    #Make it show stats
                    print("stats something")
                    break
                else:
                    print("Invalid action")
                    self.action()
                    break

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
tester.action()
#tester.add_points()
#tester.check_score()
#tester.clear_hand()
#tester.draw(deck, 2)
#tester.show()
#tester.add_points()
#tester.check_score()





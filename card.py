#Card Class

class Card:
    def __init__(self, suit, face, ability=None):
        self.suit = ["S", "D", "C", "H"][suit]
        #S for spades, D for diamonds, C for clubs, H for hearts
        self.face = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"][face-1]
        self.ability = ability

    def points(self):
        if self.face == "2" or self.face == "3":
            self.points = 0
        elif self.face == "Q":
            self.points = 31
        elif self.face == "J" or self.face == "K":
            self.points = 10
        elif self.face == "A":
            self.points = 11
        else:
            self.points = int(self.face)

    if self.face == "Q":
        self.ability = "add any card"
    elif self.face == "7":
        self.ability = "+7"
    elif self.face == "A":
        self.ability = "skip"
    else:
        self.ability = None

    def check_suit():
        return self.suit

    def check_face():
        return self.face

    def display_card(self):
        print("{self.suit}{self.face}")


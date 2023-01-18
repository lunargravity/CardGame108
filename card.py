#Card Class

class Card:
    def __init__(self, suit, face, points = None, ability = None):
        self.suit = suit
        self.face = face

        #Special Ability Assigner
        if self.face == "Q":
            self.ability = "add"
            #Can add any card additionally
        elif self.face == "7":
            self.ability = "+3"
            #Draw 7 additional cards
        elif self.face == "A":
            self.ability = "skip"
            #Skip the next player
        else:
            self.ability = None

        #Points Assigner required for end of a round
        if self.face == "2" or self.face == "3" or self.face == "4" or self.face == "5" or self.face == "6":
            self.points = 0
        elif self.face == "Q":
            self.points = 30
        elif self.face == "J":
            self.points = 2
        elif self.face == "K":
            self.points = 4
        elif self.face == "A":
            self.points = 11
        else:
            self.points = int(self.face)

    def check_points(self):
        return self.points

    def check_ability(self):
        return self.ability

    def show(self):
        return "{}{}".format(self.suit, self.face)

    def current(self):
        if self.suit == "S":
            symbol = "♠"
        elif self.suit == "H":
            symbol = "♥"
        elif self.suit == "D":
            symbol = "♦"
        else:
            symbol = "♣"

        s = "              ┌────┐"
        s += ("\nCurrent Card: |{:<2}{:>2}|").format(symbol, self.face)
        s += "\n              └────┘"

        print(s)
    
    def playability(self, discard):
        if self.face == "Q" or self.face == "7" or self.face == "A":
            return True
        elif discard[-1].suit == self.suit:
            return True
        elif discard[-1].face == self.face:
            return True
        else:
            return False
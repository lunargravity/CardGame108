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
            self.ability = "+7"
            #Draw 7 additional cards
        elif self.face == "A":
            self.ability = "skip"
            #Skip the next player
        else:
            self.ability = None

        #Points Assigner required for end of a round
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

    def check_points(self):
        print(self.points)

    def check_ability(self):
        print(self.ability)

    def show(self):
        return "{}{}".format(self.suit, self.face)

#test = Card("S", "Q")
#test.show()
#test.check_ability()
#test.check_points()

#test2 = Card("D", "4")
#test2.show()
#test2.check_ability()
#test2.check_points()
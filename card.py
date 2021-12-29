#Card Class

class Card:
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

    def show(self):
        print("{}{}".format(self.suit, self.face))

#test = Card("S", 2)
#test.show()
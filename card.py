#Card Class

class Card:
    def __init__(self, suit, face, ability=None):
        self.suit = "♥♦♣♠"[suit]
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

    def show(self):
        print('┌───────┐')
        print(f'| {self.face:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.face:>2} |')
        print('└───────┘') 

        #don't forget abilities
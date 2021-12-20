#Card Class

class Card:
    def __init__(self, suit, face, ability=None):
        self.suit = ["♥♦♣♠"][suit]
        self.face = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"][face]
        self.ability = ability

    def show(self):
        print('┌───────┐')
        print(f'| {self.face:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.face:>2} |')
        print('└───────┘') 

        #don't forget abilities
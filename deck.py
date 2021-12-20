#Creating the Cards

import random
from card import Card

class buildDeck:
    def __init__(self):
        self.cards = []

    def generate(self):
        for face in range(1, 14):
            for suit in range(4):
                self.cards.append(Card(suit, face))

    def draw(self, times):
        cards = []
        for num in range(times):
            card = random.choice(self.cards)
            self.cards.remove(card)
            cards.append(card)
        return cards
    
    #what happens when there is no more cards in the deck?
#Creating the Cards

import random
#Deck class

from card import Card

class buildDeck:
    def __init__(self):
        self.deck = []

    def generate(self):
        for face in range(1, 14):
            for suit in range(4):
                self.deck.append(Card(suit, face))
    
    def draw(self, times):
        cards = []
        if times < len(self.deck):
            for num in range(times):
                card = random.choice(self.deck)
                self.deck.pop(card)
                cards.append(card)
            return cards
        else:
            new_deck = generate()
            self.deck.append(new_deck)
            self.deck = list(set(self.deck))
            for num in range(times):
                card = random.choice(self.deck)
                self.deck.pop(card)
                cards.append(card)
            return cards
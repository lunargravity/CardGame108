import pygame
import os
import random
from pygame.locals import*

#Initializing
pygame.init()

#Creating Display
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
game_display.fill((224, 251, 252))
pygame.display.flip()

pygame.display.set_caption("108")

def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

while True:
    event_handler()

pygame.display.update()

#Card Class

class Card:
    def __init__(self, suit, number, ability):
        self.suit = suit
        self.number = number
        self.ability = ability

    def cardinfo(self):
        return self.suit
        return self.number
        return self.ability

#Creating the Cards

def BuildDeck():
    deck = []
    suit = ["clubs", "spades", "hearts", "diamonds"]
    number = range(1, 10)

print(range(1, 10))

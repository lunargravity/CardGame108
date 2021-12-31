#Main file

from deck import buildDeck
from player import *
from sys import exit
from collections import deque

def help():
    """
    Prints a help message
    """
    s  = ("+---------------------------------------------------------------+\n")
    s += ("| Instructions:                                                 |\n")
    s += ("| D to draw, P to pass, S for stats, Q to quit                  |\n")
    s += ("| S for spades, D for diamonds, C for clubs, H for hearts       |\n")
    s += ("| Type the card you want to play. i.e. \"S2\" for 2 of Spades.    |\n")
    s += ("+---------------------------------------------------------------+\n")
    return s

def valid_start_card(card):
    """
    Makes sure the starting card isn't a special card, thus can be played properly.
    """
    if card.face == "Q" or card.face == "7" or card.face == "A":
        return False
    else:
        return True

def check_played(card, current):
    """
    Checks the validity of the playing card by seeing if it matches the suit or face.
    """
    if card.face == "Q" or card.face == "7" or card.face == "A":
        return True
    elif card.suit == current.suit:
        return True
    elif card.face == current.face:
        return True
    else:
        return False

def check_wild(card):
    """
    To make sure no one plays a special card after a wild one.
    """
    if card.face == "7":
        return False
    elif card.face == "A":
        return False
    else:
        return True

#When game starts
if __name__ == "__main__":

    #Player and CPU Storage
    cpus = {}
    player_name = input("Enter your name: ").title()
    user = Player(player_name, brain = "Human")
    num_cpu = input("Number of CPU players (1-4): ")
    if 1 <= int(num_cpu) <= 4:
        for i in range(1, int(num_cpu) + 1):
            cpus[i] = Player("CPU " + str(i))
    else:
        print("Please enter valid CPU number.")
        exit()
      
 
    deck = buildDeck()
    deck.shuffle()

    #Drawing inital 5 cards
    user.draw(deck, 5)
    for i in range(1, int(num_cpu) + 1):
        cpus[i].draw(deck, 5)
        cpus[i].cpu_show()

    user.show()

    #Show instructions
    print(help())

    #Flipping the first card
    discard = []
    first = deck.draw()
    while valid_start_card(first) == False:
        first = deck.draw()
    else:

        discard.append(first)
        print("Current Card: " + str(discard[-1].show()))

    #Flags
    round_over = False
    game_over = False
    skipped = False

    #Players List to keep track of turns
    player_order = [user]
    for i in range(1, int(num_cpu) + 1):
        player_order.append(cpus[i])
    
    #for player in player_order:
    #    player.add_points()
    #    print(player.score)

    user.action(deck, discard)
    user.action(deck, discard)
    user.action(deck, discard)
    user.action(deck, discard)


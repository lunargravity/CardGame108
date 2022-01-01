#Main file

from deck import buildDeck
from player import *
from sys import exit
import random

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
        return True
    elif card.face == "A":
        return True
    else:
        return False

def queen():
    """
    The special ability of a queen card to add an additional card to the pile.
    """
    wild = input("Add a card: ").upper()
    if check_wild(wild) == False:
        player.hand.remove(wild)
        discard.append(wild)
        self.show()
        print("Current card: " + str(discard[-1].show()))
        pass
    else:
        print("You cannot play a special card on top of a Queen. Play a different card.")
        queen()

def seven(card):
    """
    Makes the player draw 7 cards due to the special ability of the 7 card.
    """
    new_cards = ""
    for i in range(7):
        new = player.draw(deck)
        new_cards += "|" + str(new.show()) + "|"
    print("You have drawn 7 cards from the deck:")
    print(new_cards)
    print("Your new hand:")
    player.show()
    pass
        
def cpu_turn(player):
    """
    The logic behind the cpu's gameplay.
    """
    valid = []
    special = []

    #Organizes their hand into two piles, valid regular cards and special cards.
    for card in player.hand:
        if card.face == discard[-1].face:
            valid.append(card)
        elif card.suit == discard[-1].suit:
            valid.append(card)
        elif card.face == "Q" or card.face == "7" or card.face == "A":
            special.append(card)

    #They will initially try a regular card
    try:
        choice = random.choice(valid)
    except:
        #If they do not have a valid card, they will go for a special card
        try:
            choice = random.choice(special)
        except:
            choice = None

    if choice == None:
        print(player.name + " cannot do anything. So they draw.")
        player.draw(deck)
        pass
    else:
        if choice in valid:
            print(player.name + " plays " + str(choice.show()))
            player.hand.remove(choice)
            discard.append(choice)
        elif choice.face == "Q":
            if len(player.hand) <= 2:
                #Because a player cannot end a round on a Queen card.
                print(player.name + " cannot do anything. So they draw.")
                player.draw(deck)
            else:
                print(player.name + " plays a QUEEN.")
                player.hand.remove(choice)
                discard.append(choice)
                try:
                    suits_in_hand = {S:0, D:0, C:0, H:0}
                    for card in player.hand:
                        for suit in suits_in_hand.keys:
                            suits_in_hand[suit] = suits_in_hand.count(suit)
                    max_suit = max(suits_in_hand)
                    max = []
                    for card in player.hand:
                        if card.suit == max_suit:
                            max.append(card)
                    choice = random.choice(max)
                    print(player.name + " plays " + str(choice.show()))
                    player.hand.remove(choice)
                    discard.append(choice)
                except:
                    #During the possibility there is no max suit
                    choice = random.choice(valid)
                    print(player.name + " plays " + str(choice.show()))
                    player.hand.remove(choice)
                    discard.append(choice)
        elif choice.face == "7":
            print(player.name + "plays a +7.")
            player.hand.remove(choice)
            discard.append(choice)
        elif choice.face == "A":
            print(player.name + "plays a SKIP.")
            player.hand.remove(choice)
            discard.append(choice)
        pass

def user_turn(player):
    """
    The function behind the user's turn 
    """
    user_action = input("Action: ").upper()
    if len(user_action) > 1:
        #Checking to see if the user played a card
        for card in player.hand:
            if card.show() == user_action:
                chosen = card
        #Turns the user input into a card object
        if chosen in player.hand:
            if check_played(chosen, discard[-1]) == True:
                #Checking for special card
                if chosen.face == "Q":
                    print("You have played a QUEEN.")
                    player.hand.remove(chosen)
                    discard.append(chosen)                    
                    queen()
                elif chosen.face == "7":
                    print("You have played +7.")
                    player.hand.remove(chosen)
                    discard.append(chosen)                    
                    pass
                elif chosen.face == "A":
                    print("You have played SKIP.")
                    player.hand.remove(chosen)
                    discard.append(chosen)                    
                    pass
                else:
                    #If not a special card
                    print("You have played " + chosen.show() + ".")
                    player.hand.remove(chosen)
                    discard.append(chosen)
                    
                    pass
            else:
                print("You cannot play that. Try to match the suit or face.")
                user_turn(player)
    else:
        #If not a card, but a command
        if user_action == "P":
            pass
        elif user_action == "S":
            s  = ("+---------------------------------------------------------------+\n")
            s += ("| Stats:\n")
            s += ("| Scores:\n")
            s += ("| Your Score: {}\n").format(user.score)
            for player in player_order[1:]:
                s += ("| {}'s Score: {} \n").format(player.name, player.score)
            s += ("+---------------------------------------------------------------+\n")
            print(s)
            user_turn(player)
        elif user_action == "D":
            player.draw(deck)
            new = player.hand[-1]
            print("You have drawn " + new.show() + " from the deck.")
            pass
        else:
            print("Invalid action. Try D for Draw, P for Pass, S for Status. Or try to play one of your cards.")
            user_turn(player)

def check_previous(card):
    if discard[-1].face == "7":
        seven()
    elif discard[-1].face == "A":



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
    
    for player in player_order:
        player.add_points()
        print(player.score)

    while not game_over:
        for player in player_order:
            if player.brain == "Human":
                player.show()
                user_turn(player)
                print("Current Card: " + str(discard[-1].show()))
            elif player.brain == "CPU":
                cpu_turn(player)
                print("Current Card: " + str(discard[-1].show()))
                pass
            else:
                print("Who are you??? Go away!")
                exit()


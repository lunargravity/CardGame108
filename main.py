#Main file

from deck import buildDeck
from player import *
import sys
import os
import random
import time
import colorama
from colorama import Fore
colorama.init()

def help():
    """
    Prints a help message
    """
    s  = ("+---------------------------------------------------------------+\n")
    s += ("| Instructions:                                                 |\n")
    s += ("| Type D to draw from the deck.                                 |\n")
    s += ("| S for spades, D for diamonds, C for clubs, H for hearts       |\n")
    s += ("| Type the card you want to play. i.e. \"S2\" for 2 of Spades.    |\n")
    s += ("| At the end of the round, points will be counted accordingly.  |\n")
    s += ("| 2 and 3 don't count. J and K are worth 10 points.             |\n")
    s += ("| A is worth 11. Q is worth 13. Everything else is face value.  |\n")
    s += ("| If you reach 108 points at the end of a round, you are out.   |\n")
    s += ("| The game keeps going until there is only one player left.     |\n")
    s += ("| Disclaimer: You cannot end on a Queen card.                   |\n")
    s += ("| Queens are wild cards. 7s make next player draw 7. Aces skip. |\n")
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

def queen(player, discard):
    """
    The special ability of a queen card to add an additional card to the pile.
    """
    wild = input("Add a card: ").upper()
    for card in player.hand:
        if card.show() == wild:
            wild = card
    if check_wild(wild) == False:
        player.hand.remove(wild)
        discard.append(wild)
        pass
    else:
        print("You cannot play a special card on top of a Queen. Play a different card.")
        queen(player, discard)

def seven(player, discard, deck):
    """
    Makes the player draw 7 cards due to the special ability of the 7 card.
    """

    sevens = 0
    last = discard[-4:]
    last.reverse()
    for c in last:
        if c.face == "7":
            sevens += 1
        else:
            break
    num = sevens * 3

    if player.brain == "Human":
        if len(deck) < num:
            top = discard.pop()
            deck = buildDeck()
            deck.shuffle()
            deck.remove(top)
            discard.append(top)
            player.draw(deck, num)
        else:
            player.draw(deck, num)
        print("You have drawn " + str(num) + " cards from the deck.")
    else:
        if len(deck) < num:
            top = discard.pop()
            deck = buildDeck()
            deck.shuffle()
            deck.remove(top)
            discard.append(top)
            player.draw(deck, num)
        else:
            player.draw(deck, num)
        print(player.name + " has drawn " + str(num) + " from the deck.")
    drew_7 = True
    pass
        
def cpu_turn(player, deck, discard):
    """
    The logic behind the cpu's gameplay.
    """
    
    global drew_7
    global skipped

    valid = []
    special = []

    #Organizes their hand into two piles, valid regular cards and special cards.
    for card in player.hand:
        if card.face == "Q":
            special.append(card)
        elif card.face == "7":
            special.append(card)
        elif card.face == "A":
            special.append(card)
        elif card.face == discard[-1].face:
            valid.append(card)
        elif card.suit == discard[-1].suit:
            valid.append(card)

    #print("Valid:")
    #for card in valid:
    #    print(card.show())
    #print("Special:")
    #for card in special:
    #    print(card.show())

    #They will initially try a regular card
    try:
        choice = random.choice(valid)
    except:
        #If they do not have a valid card, they will go for a special card
        try:
            choice = random.choice(special)
        except:
            choice = None

    #print("Choice: " + choice.show())

    if choice == None:
        print(player.name + " cannot do anything. So they draw.")
        if len(deck) < 1:
            top = discard.pop()
            deck = buildDeck()
            deck.shuffle()
            deck.remove(top)
            discard.append(top)
            player.draw(deck)
        else:
            player.draw(deck)
        pass
    else:
        if choice in valid:
            print(player.name + " plays " + str(choice.show()))
            player.hand.remove(choice)
            discard.append(choice)
        elif choice.face == "Q":
            if len(player.hand) == 1:
                #The player's points will be deducted by 30 points
                player.score -= 30
            else:
                print(player.name + " plays a QUEEN.")
                player.hand.remove(choice)
                discard.append(choice)
                try:
                    #Finding the most beneficial card to change the current card to by finding the max.
                    suits_in_hand = {"S":0, "D":0, "C":0, "H":0}
                    for card in player.hand:
                        for suit in suits_in_hand.keys:
                            suits_in_hand[suit] = suits_in_hand.count(suit)
                    print("Suits in hand: " + str(suits_in_hand))
                    max_suit = max(suits_in_hand)
                    max = []  
                    for card in player.hand:
                        if card.suit == max_suit and card.face != "7" or card.face != "A":
                            max.append(card)
                    print("Max: " + str(c.show() for c in max))
                    choice = random.choice(max)
                    print(player.name + " plays " + str(choice.show()))
                    player.hand.remove(choice)
                    discard.append(choice)
                except:
                    #During the possibility there is no max suit.
                    valid = []
                    for card in player.hand:
                        if check_wild(card) == False:
                            #To make sure that the cpu doesn't put a special card on a Queen card.
                            valid.append(card)
                    choice = random.choice(valid)
                    print(player.name + " plays " + str(choice.show()))
                    player.hand.remove(choice)
                    discard.append(choice)

        elif choice.face == "7":
            print(player.name + " plays a +3.")
            player.hand.remove(choice)
            discard.append(choice)
            drew_7 = False
        elif choice.face == "A":            
            print(player.name + " plays a SKIP.")
            player.hand.remove(choice)
            discard.append(choice)
            skipped = False
        pass

def user_turn(player, deck, discard):
    """
    The function behind the user's turn 
    """
    
    global drew_7
    global skipped

    if len(player.hand) == 1:
        for card in player.hand:
            if card.face == "Q":
                print("You are ending with a Queen, so your points will be deducted by 30 points.")
                time.sleep(1)
                player.score -= 30
                player.hand.remove(card)
                discard.append(card)
            elif card.face == "7":
                print("You cannot end with a 7. You will be forced to draw a card.")
                time.sleep(1)
                player.hand.remove(card)
                discard.append(card)
                if len(deck) < 1:
                        top = discard.pop()
                        deck = buildDeck()
                        deck.shuffle()
                        deck.remove(top)
                        discard.append(top)
                        player.draw(deck)
                else:
                    player.draw(deck)
                new = player.hand[-1]
                print("You have drawn " + new.show() + " from the deck.")
            pass

    
    while True:
        try:
            user_action = input("Action: ").upper()
            if len(user_action) > 1:
                #Checking to see if the user wishes to play a card
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
                            queen(player, discard)
                        elif chosen.face == "7":
                            print("You have played +3.")
                            player.hand.remove(chosen)
                            discard.append(chosen)     
                            drew_7 = False
                        elif chosen.face == "A":
                            print("You have played SKIP.")
                            player.hand.remove(chosen)
                            discard.append(chosen)
                            skipped = False
                        else:
                            #If not a special card
                            print("You have played " + chosen.show() + ".")
                            player.hand.remove(chosen)
                            discard.append(chosen)  
                        break
                    else:
                        print("You cannot play that. Try to match the suit or face.")
                        continue
            else:
                #If not a card, but a command
                if user_action == "D":
                    if len(deck) < 1:
                        top = discard.pop()
                        deck = buildDeck()
                        deck.shuffle()
                        deck.remove(top)
                        discard.append(top)
                        player.draw(deck)
                    else:
                        player.draw(deck)
                    new = player.hand[-1]
                    print("You have drawn " + new.show() + " from the deck.")
                    break
                else:
                    print("Invalid action. Try D for Draw, P for Pass, S for Status. Or try to play one of your cards.")
                    continue
        except:
            print("Invalid action. Try D for Draw, P for Pass, S for Status. Or try to play one of your cards.")
            continue
    pass

def stats(player, player_order, deck, discard):
    s = ""
    s += ("+---------------------------------------------------------------+\n")
    s += ("| Your hand: {}\n").format(len(user.hand))
    for player in player_order[1:]:
        s += ("| {}'s hand: {} \n").format(player.name, len(player.hand))
    s += ("| Cards in the deck: {}\n").format(len(deck))
    s += ("| " + Fore.LIGHTCYAN_EX + "Current Card: " + str(discard[-1].show()) + "\n" + Fore.RESET)
    s += ("+---------------------------------------------------------------+\n")
    print(s)

def check_previous(player, card, deck, discard):
    
    global drew_7
    global skipped

    if card.face == "7":
        if drew_7 == True:
            if player.brain == "Human":
                user_turn(player, deck, discard)
            else:
                time.sleep(1)
                cpu_turn(player, deck, discard)
        else:
            seven(player, discard, deck)
            time.sleep(1)
            drew_7 = True
    elif card.face == "A":
        if skipped == False:
            if player.brain == "Human":
                print("You have been skipped.")
                skipped = True
            else:
                print(player.name + " has been skipped.")
                skipped = True
            pass
        else:
            if player.brain == "Human":
                user_turn(player, deck, discard)
            else:
                time.sleep(1)
                cpu_turn(player, deck, discard)
    else:
        if player.brain == "Human":
            user_turn(player, deck, discard)
        else:
            time.sleep(1)
            cpu_turn(player, deck, discard)

def count_points(players):
    for player in players:
        player.add_points()
    s  = ("+---------------------------------------------------------------+\n")
    s += ("| Scores:\n")
    s += ("| Your Score: {}\n").format(user.score)
    for player in player_order[1:]:
        s += ("| {}'s Score: {} \n").format(player.name, player.score)
    s += ("+---------------------------------------------------------------+\n")
    print(s)

def round():
    """
    How a round will be formatted and loop with check_round_over to allow multiple rounds.
    """
    deck = buildDeck()
    deck.shuffle()

    #Drawing inital 5 cards
    for player in player_order:
        player.draw(deck, 5)
        if player.brain == "Human":
            player.cpu_show()
        else:
            player.cpu_show()

    #Flipping the first card
    discard = []
    first = deck.draw()
    while valid_start_card(first) == False:
        first = deck.draw()
    else:
        discard.append(first)
        print(Fore.LIGHTCYAN_EX + "Current Card: " + str(discard[-1].show()) + Fore.RESET)

    #Flags
    round_over = False
    skipped = False
    drew_7 = False

    while round_over == False:
        for player in player_order:
                if player.brain == "Human":
                    player.show()
                    check_previous(player, discard[-1], deck, discard)
                    check_round_over(player, player_order)
                elif player.brain == "CPU":
                    check_previous(player, discard[-1], deck, discard)
                    check_round_over(player, player_order)
                    pass
                else:
                    print("Who are you??? Go away!")
                    exit()
        time.sleep(1)
        stats(player, player_order, deck, discard)
        time.sleep(1)

def check_round_over(player, players):
    """
    To see if the game can continue or restart.
    """
    global round_over

    if len(player.hand) < 1:
        round_over = True
    else:
        round_over = False
        pass

    if round_over == True:
        print("Round over! " + player.name + " wins this round!")
        time.sleep(1)
        count_points(player_order)
        time.sleep(1)
        for p in players:
            p.hand = []

        for p in players:
            if p.brain == "Human":
                if p.score >= 108:
                    print(p.name + ", you have 108 or over points. You are out.")
                    user_action = input("Type R to restart or E to exit.").upper()
                    if user_action == "R":
                        print("New game will begin...")
                        countdown = 5
                        while countdown > 0:
                            print("... in  " + str(countdown))
                            time.sleep(1)
                            countdown -= 1
                        os.execl(sys.executable, sys.executable, *sys.argv)
                    elif user_action == "E":
                        print("Goodbye! Thank you for playing!")
                        countdown = 5
                        while countdown > 0:
                            print("Exit in " + str(countdown))
                            time.sleep(1)
                            countdown -= 1
                        exit()
                    else:
                        print("Invalid action. Exiting anyway.")
                        print("Goodbye! Thank you for playing!")
                        countdown = 5
                        while countdown > 0:
                            print("Exit in " + str(countdown))
                            time.sleep(1)
                            countdown -= 1
                        exit()
                else:
                    pass
            else:
                if p.score >= 108:
                    print(p.name + " has 108 points or more. They are out.")
                    players.remove(p)

        print("New round will begin...")
        countdown = 3
        while countdown > 0:
            print("... in  " + str(countdown))
            time.sleep(1)
            countdown -= 1
        round_over = False
        round()
    else:
        pass

def check_game_over(players):
    if len(players) == 1:
        game_over = True
        for p in players:
            if p.brain == "Human":
                print("You have won!")
                user_action = input("Would you like to play again? Y for yes, N for no.").upper()
                if user_action == "Y":
                    print("New game will begin...")
                    countdown = 5
                    while countdown > 0:
                        print("... in  " + str(countdown))
                        time.sleep(1)
                        countdown -= 1
                    os.execl(sys.executable, sys.executable, *sys.argv)
                elif user_action == "N":
                    print("Thank you for playing! Goodbye!")
                    countdown = 5
                    while countdown > 0:
                        print("Exit in " + str(countdown))
                        time.sleep(1)
                        countdown -= 1
                    exit()
                else:
                    print("Invalid action. Exiting anyway.")
                    print("Thank you for playing! Goodbye!")
                    countdown = 5
                    while countdown > 0:
                        print("Exit in " + str(countdown))
                        time.sleep(1)
                        countdown -= 1
                    exit()
            else:
                print(player.name + "has won!")
                user_action = input("Would you like to play again? Y for yes, N for no.").upper()
                if user_action == "Y":
                    print("New game will begin...")
                    countdown = 5
                    while countdown > 0:
                        print("... in  " + str(countdown))
                        time.sleep(1)
                        countdown -= 1
                    os.execl(sys.executable, sys.executable, *sys.argv)
                elif user_action == "N":
                    exit()
                else:
                    print("Invalid action. Exiting anyway.")
                    countdown = 5
                    while countdown > 0:
                        print("Exit in " + str(countdown))
                        time.sleep(1)
                        countdown -= 1
                    exit()

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

    #Show instructions
    print(help())

    #Players List to keep track of turns
    player_order = [user]
    for i in range(1, int(num_cpu) + 1):
        player_order.append(cpus[i])

    game_over = False

    #Main game
    while not game_over:
        round()
        


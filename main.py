#Update 2.0 Main File

from deck import buildDeck
from player import *
import sys
import os
import random
import time
import colorama
from colorama import Fore
colorama.init()

"""
When the game starts
"""

if __name__ == "__main__":

    #Player and CPU Storage
    name = input("Enter your name: ").title()
    user = Player(name, brain = "Human")
    #Turn Order
    order = [user]
    num_cpu = input("Number of CPU players (1-4): ")
    if 1 <= int(num_cpu) <= 4:
        for i in range(1, int(num_cpu) + 1):
            order.append(Player("CPU " + str(i)))
    else:
        print("Please enter valid CPU number.")
        time.sleep(1)
        os.execl(sys.executable, sys.executable, *sys.argv)

    #Show Instructions
    s  = ("+---------------------------------------------------------------+\n")
    s += ("| Instructions:                                                 |\n")
    s += ("| Type D to draw from the deck. Type P to pass.                 |\n")
    s += ("| S for spades, D for diamonds, C for clubs, H for hearts       |\n")
    s += ("| Type the card you want to play. i.e. \"S2\" for 2 of Spades.    |\n")
    s += ("| At the end of the round, points will be counted accordingly.  |\n")
    s += ("| 2-6 don't count. J are worth 2 and K are worth 4 points.      |\n")
    s += ("| A is worth 11. Q is worth 30. Everything else is face value.  |\n")
    s += ("| If you reach 108 points exactly, it will be divided by 2.     |\n")
    s += ("| If you reach over 108 points, you are out. And it's game over.|\n")
    s += ("| The game keeps going until there is only one player left.     |\n")
    s += ("| Disclaimer: You can't end on a 7. Or you will draw a card.    |\n")
    s += ("| If you end on a Queen, your points will be deducted by 30.    |\n")
    s += ("| Queens are wild cards. Aces skip. 7s make next player draw 3. |\n")
    s += ("| If someone plays a 7 or A, you can play a 7 or an Ace to skip.|\n")
    s += ("+---------------------------------------------------------------+\n")
    print(s)

    #Game begins
    game = True

    #Main Game Loop
    while game:
        print("Game is running.")
        round_over = False
        print("Round starts")

        #Shuffle deck
        deck = buildDeck()
        deck.shuffle()

        #Drawing initial 5 cards
        for player in order:
            player.draw(deck, 5)

        #Flipping first card
        discard = []
        first = deck.draw()
        valid = False
        while not valid:
            if first.face == "Q" or first.face == "7" or first.face == "A":
                first = deck.draw()
                valid = False
            else:
                discard.append(first)
                print(Fore.LIGHTCYAN_EX + "Current Card: " + str(discard[-1].show()) + Fore.RESET)
                valid = True
            
        #Flags
        drew = False
        skipped = False
        
        #Round Loop
        while not round_over:
            #Player turns
            for player in order:
                if player.brain == "Human":
                    #Shows Player hand
                    player.show()
                    print("Type D for Draw, P for Pass or Input a Card(ie. S5 for 5 of Spades).")
                    while True:
                        try:
                            action = input("Action: ").upper()
                            #Checking to see if the user wishes to play a card
                            if len(action) > 1:
                                #Turns the user input into a card object
                                for card in player.hand:
                                    if card.show() == action:
                                        chosen = card
                                if chosen in player.hand:
                                    if chosen.playability(discard) == True:
                                        if chosen.face == "Q":
                                            if len(player.hand) == 1:
                                                print("You are ending on a QUEEN.")
                                                print("Your points will be deducted by 30.")
                                                time.sleep(1)
                                                player.score -= 30
                                                player.hand.remove(chosen)
                                                discard.append(chosen)
                                                break
                                            else:
                                                print("You have played a QUEEN.")
                                                suit = input("Choose a suit (S, C, D, H):")
                                                player.hand.remove(chosen)
                                                discard.append(chosen)
                                                discard.append(Card[str(suit), "Q"])
                                                break
                                        elif chosen.face == "7":
                                            if len(player.hand) == 1:
                                                print("You cannot end on a 7.")
                                                print("You will be forced to draw.")
                                                player.hand.remove(chosen)
                                                discard.append(chosen)
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
                                                print("You have played a +3.")
                                                player.hand.remove(chosen)
                                                discard.append(chosen)
                                                drew = False
                                                break
                                        elif chosen.face == "A":
                                            print("You have played a SKIP.")
                                            player.hand.remove(chosen)
                                            discard.append(chosen)
                                            skipped = False
                                            break
                                        else:
                                            #If not special card
                                            print("You have played " + chosen.show() + ".")
                                            player.hand.remove(chosen)
                                            discard.append(chosen)
                                            break
                                    else:
                                        print("You cannot play that card. Try to match the suit or the face.")
                                else:
                                    print("You do not have that card. Try again.")
                                    continue
                            #User inputs a command, not a card
                            else:
                                if action == "D" or action == "DRAW":
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
                                elif action == "P" or action == "PASS":
                                    break
                                else:
                                    print("Invalid action. Try D for Draw, P for Pass or try playing one of your cards.")
                                    continue
                        except:
                            print("Invalid. Try D for Draw, P for Pass or try playing one of your cards.")
                            continue

                #CPU Turns
                elif player.brain == "CPU":
                    time.sleep(1)
                    if discard[-1].face == "7":
                        if drew == True:
                            valid = []
                            special = []
                            
                            #Organizing hand into two piles, valid regular cards and special cards
                            for c in player.hand:
                                if c.face == "Q":
                                    special.append(c)
                                elif c.face == "7":
                                    special.append(c)
                                elif c.face == "A":
                                    special.append(c)
                                elif c.face == discard[-1].face:
                                    valid.append(c)
                                elif c.suit == discard[-1].suit:
                                    valid.append(c)

                            #First try valid regular card
                            try:
                                choice = random.choice(valid)
                            except:
                                #Then try special card
                                try:
                                    choice = random.choice(special)
                                except:
                                    choice = None

                            #CPU will play a card
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
                                        #CPU's points will be deducted by 30 points
                                        player.score -= 30
                                        print(player.name + " plays a QUEEN as their last card.")
                                        player.hand.remove(choice)
                                        discard.append(choice)
                                    else:
                                        print(player.name + " plays a QUEEN.")
                                        player.hand.remove(choice)
                                        discard.append(choice)
                                        suits_in_hand = {}
                                        for c in player.hand:
                                            if (c.suit in suits_in_hand):
                                                suits_in_hand[c.suit] += 1
                                            else:
                                                suits_in_hand[c.suit] = 1
                                        maximum = max(suits_in_hand.values())
                                        suits = list()
                                        for key, value in suits_in_hand.items():
                                            if value == maximum:
                                                suits.append(key)
                                        choice = random.choice(suits)
                                        discard.append(Card(choice, "Q"))
                                        if choice == "D":
                                            print(player.name + " has chosen Diamonds.")
                                        elif choice == "H":
                                            print(player.name + " has chosen Hearts.")
                                        elif choice == "S":
                                            print(player.name + " has chosen Spades.")
                                        elif choice == "C":
                                            print(player.name + " has chosen Clubs.")
                                        else:
                                            print("Something went wrong. They chose " + choice)
                                elif choice.face == "7":
                                    print(player.name + " plays a +3. A " + str(choice.show()))
                                    player.hand.remove(choice)
                                    discard.append(choice)
                                    drew = False
                                elif choice.face == "A":
                                    print(player.name + " plays a SKIP. A " + str(choice.show()))
                                    player.hand.remove(choice)
                                    discard.append(choice)
                                    skipped = False
                                pass
                        else:
                            print("{} draws cards.".format(player.name))
                            drew = True
                            print("Drew status is now " + str(drew))
                            #+----------------------------+
                            player.draw(deck, 3)
                            #+----------------------------+
                    elif discard[-1].face == "A":
                        if skipped == True:
                            valid = []
                            special = []

                            #Organizing hand into two piles, valid regular cards and special cards
                            for c in player.hand:
                                if c.face == "Q":
                                    special.append(c)
                                elif c.face == "7":
                                    special.append(c)
                                elif c.face == "A":
                                    special.append(c)
                                elif c.face == discard[-1].face:
                                    valid.append(c)
                                elif c.suit == discard[-1].suit:
                                    valid.append(c)

                            #First try valid regular card
                            try:
                                choice = random.choice(valid)
                            except:
                                #Then try special card
                                try:
                                    choice = random.choice(special)
                                except:
                                    choice = None

                            #CPU will play a card
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
                                        #CPU's points will be deducted by 30 points
                                        player.score -= 30
                                        print(player.name + " plays a QUEEN as their last card.")
                                        player.hand.remove(choice)
                                        discard.append(choice)
                                    else:
                                        print(player.name + " plays a QUEEN.")
                                        player.hand.remove(choice)
                                        discard.append(choice)
                                        suits_in_hand = {}
                                        for c in player.hand:
                                            if (c.suit in suits_in_hand):
                                                suits_in_hand[c.suit] += 1
                                            else:
                                                suits_in_hand[c.suit] = 1
                                        maximum = max(suits_in_hand.values())
                                        suits = list()
                                        for key, value in suits_in_hand.items():
                                            if value == maximum:
                                                suits.append(key)
                                        choice = random.choice(suits)
                                        discard.append(Card(choice, "Q"))
                                        if choice == "D":
                                            print(player.name + " has chosen Diamonds.")
                                        elif choice == "H":
                                            print(player.name + " has chosen Hearts.")
                                        elif choice == "S":
                                            print(player.name + " has chosen Spades.")
                                        elif choice == "C":
                                            print(player.name + " has chosen Clubs.")
                                        else:
                                            print("Something went wrong. They chose " + choice)
                                elif choice.face == "7":
                                    print(player.name + " plays a +3. A " + str(choice.show()))
                                    player.hand.remove(choice)
                                    discard.append(choice)
                                    drew = False
                                elif choice.face == "A":
                                    print(player.name + " plays a SKIP. A " + str(choice.show()))
                                    player.hand.remove(choice)
                                    discard.append(choice)
                                    skipped = False
                                pass
                        else:
                            print("User gets skipped.")
                            skipped = True
                            print("Skip status is now " + str(skipped))
                    else:
                        valid = []
                        special = []

                        #Organizing hand into two piles, valid regular cards and special cards
                        for c in player.hand:
                            if c.face == "Q":
                                special.append(c)
                            elif c.face == "7":
                                special.append(c)
                            elif c.face == "A":
                                special.append(c)
                            elif c.face == discard[-1].face:
                                valid.append(c)
                            elif c.suit == discard[-1].suit:
                                valid.append(c)

                        #First try valid regular card
                        try:
                            choice = random.choice(valid)
                        except:
                            #Then try special card
                            try:
                                choice = random.choice(special)
                            except:
                                choice = None

                        #CPU will play a card
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
                                    #CPU's points will be deducted by 30 points
                                    player.score -= 30
                                    print(player.name + " plays a QUEEN as their last card.")
                                    player.hand.remove(choice)
                                    discard.append(choice)
                                else:
                                    print(player.name + " plays a QUEEN.")
                                    player.hand.remove(choice)
                                    discard.append(choice)
                                    suits_in_hand = {}
                                    for c in player.hand:
                                        if (c.suit in suits_in_hand):
                                            suits_in_hand[c.suit] += 1
                                        else:
                                            suits_in_hand[c.suit] = 1
                                    maximum = max(suits_in_hand.values())
                                    suits = list()
                                    for key, value in suits_in_hand.items():
                                        if value == maximum:
                                            suits.append(key)
                                    choice = random.choice(suits)
                                    discard.append(Card(choice, "Q"))
                                    if choice == "D":
                                        print(player.name + " has chosen Diamonds.")
                                    elif choice == "H":
                                        print(player.name + " has chosen Hearts.")
                                    elif choice == "S":
                                        print(player.name + " has chosen Spades.")
                                    elif choice == "C":
                                        print(player.name + " has chosen Clubs.")
                                    else:
                                        print("Something went wrong. They chose " + choice)
                            elif choice.face == "7":
                                print(player.name + " plays a +3. A " + str(choice.show()))
                                player.hand.remove(choice)
                                discard.append(choice)
                                drew = False
                            elif choice.face == "A":
                                print(player.name + " plays a SKIP. A " + str(choice.show()))
                                player.hand.remove(choice)
                                discard.append(choice)
                                skipped = False
                            pass

                    #Checking if round over
                    if len(player.hand) < 1:
                        round_over = True
                    else:
                        round_over = False
                        pass

                    #Checking if game over
                    if len(order) == 1:
                        game = False
                    else:
                        game = True
                        
                    if round_over == True and game == True:
                        print("Round over! " + player.name + " wins this round!")
                        time.sleep(1)
                        
                        for player in order:
                            player.add_points()
                        
                        p  = ("+-------------------------------+\n")
                        p += ("| Scores:\n")
                        p += ("| Your Score: {}\n").format(user.score)
                        for player in order[1:]:
                            p += ("| {}'s Score: {} \n").format(player.name, player.score)
                        p += ("+-------------------------------+\n")
                        print(p)
                        
                        time.sleep(1)
                        for player in order:
                            if player.brain == "Human":
                                if player.score == 108:
                                    print("You have exactly 108, so your points will be divided by 2. Your new score is now 54.")
                                    player.score = 54
                                elif player.score > 108:
                                    print(player.name + ", you have over 108 points. You are out.")
                                    decision = input("Type R to restart or E to exit.").upper()
                                    if decision == "R":
                                        print("New game will begin...")
                                        countdown = 3
                                        while countdown > 0:
                                            print("...in " + str(countdown))
                                            time.sleep(1)
                                            countdown -= 1
                                        os.execl(sys.executable, sys.executable, *sys.argv)
                                    elif decision == "E":
                                        print("Goodbye! Thank you for playing!")
                                        countdown = 3
                                        print("Exiting...")
                                        while countdown > 0:
                                            print("...in " + str(countdown))
                                            time.sleep(1)
                                            countdown -= 1
                                        exit()
                                    else:
                                        print("Invalid action. Exiting anyways.")
                                        print("Goodbye! Thank you for playing!")
                                        countdown = 3
                                        print("Exiting...")
                                        while countdown > 0:
                                            print("...in " + str(countdown))
                                            time.sleep(1)
                                            countdown -= 1
                                        exit()
                                else:
                                    pass
                            else:
                                if player.score == 108:
                                    print(player.name + " has exactly 108 points, so their points will be divided by 2. Their score is now 54.")
                                    player.score = 54
                                elif player.score > 108:
                                    print(player.name + " has over 108 points. They are out.")
                                    order.remove(player)
                                else:
                                    pass
                        print("New round will begin...")
                        countdown = 3
                        
                        while countdown > 0:
                            print("...in " + str(countdown))
                            time.sleep(1)
                            countdown -= 1

                        #Shuffle deck
                        deck = buildDeck()
                        deck.shuffle()

                        #Drawing initial 5 cards
                        for player in order:
                            player.hand = []
                            player.draw(deck, 5)

                        #Flipping first card
                        discard = []
                        first = deck.draw()
                        valid = False
                        while not valid:
                            if first.face == "Q" or first.face == "7" or first.face == "A":
                                first = deck.draw()
                                valid = False
                            else:
                                discard.append(first)
                                print(Fore.LIGHTCYAN_EX + "Current Card: " + str(discard[-1].show()) + Fore.RESET)
                                valid = True
            
                        #Flags
                        drew = False
                        skipped = False
                        round_over = False
                    else:
                        pass
                        
                else:
                    print("Who are you??? Get out!")
                    exit()

            time.sleep(1)

            s = ""
            s += ("+-----------------------------+\n")
            s += ("| Your hand: {}\n").format(len(user.hand))
            for player in order[1:]:
                s += ("| {}'s hand: {} \n").format(player.name, len(player.hand))
            s += ("| Cards in the deck: {}\n").format(len(deck))
            s += ("| " + Fore.LIGHTCYAN_EX + "Current Card: " + str(discard[-1].show()) + "\n" + Fore.RESET)
            s += ("+------------------------------+\n")
            print(s)

            time.sleep(1)

    while not game:
        for player in order:
            print("{name} is the winner!".format(name=player.name))
        end = input("Would you like to play again? (Y or N)").upper()
        if end == "Y" or end == "YES":
            print("New game will begin...")
            countdown = 3
            while countdown > 0:
                print("...in " + str(countdown))
                time.sleep(1)
                countdown -= 1
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif end == "N" or end == "NO":
            print("Goodbye! Thanks for playing!")
            countdown = 3
            while countdown > 0:
                print(str(countdown))
                time.sleep(1)
                countdown -= 1
            exit()
        else:
            print("Invalid response. Try again.")
            continue
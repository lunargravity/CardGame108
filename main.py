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
    s += ("| Type D to draw from the deck.                                 |\n")
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
                    if discard[-1].face == "7":
                        if drew == True:
                            print("User doesn't draw cards.")
                            #+----------------------------+
                            ran = random.choice(player.hand)
                            print(player.name + " plays " + ran.show())
                            if ran.face == "7":
                                drew = False
                                print("Drew status is now " + str(drew))
                            elif ran.face == "A":
                                skipped = False
                                print("Skip status is now " + str(skipped))
                            player.hand.remove(ran)
                            discard.append(ran)
                            #+----------------------------+
                        else:
                            print("User draws cards.")
                            drew = True
                            print("Drew status is now " + str(drew))
                            #+----------------------------+
                            player.draw(deck, 3)
                            #+----------------------------+
                    elif discard[-1].face == "A":
                        if skipped == True:
                            print("User does not get skipped.")
                            #+----------------------------+
                            ran = random.choice(player.hand)
                            print(player.name + " plays " + ran.show())
                            if ran.face == "7":
                                drew = False
                                print("Drew status is now " + str(drew))
                            elif ran.face == "A":
                                skipped = False
                                print("Skip status is now " + str(skipped))
                            player.hand.remove(ran)
                            discard.append(ran)
                            #+----------------------------+
                        else:
                            print("User gets skipped.")
                            skipped = True
                            print("Skip status is now " + str(skipped))
                    else:
                        ran = random.choice(player.hand)
                        print(player.name + " plays " + ran.show())
                        if ran.face == "7":
                            drew = False
                            print("Drew status is now " + str(drew))
                        elif ran.face == "A":
                            skipped = False
                            print("Skip status is now " + str(skipped))
                        player.hand.remove(ran)
                        discard.append(ran)
                        
                    #Checking if round over
                    if len(player.hand) < 1:
                        round_over = True
                    else:
                        round_over = False
                        pass
                        
                    if round_over == True:
                        print("Round over! " + player.name + " wins this round!")
                        time.sleep(1)
                        
                        for player in order:
                            player.add_points()
                        
                        p  = ("+---------------------------------------------------------------+\n")
                        p += ("| Scores:\n")
                        p += ("| Your Score: {}\n").format(user.score)
                        for player in player_order[1:]:
                            p += ("| {}'s Score: {} \n").format(player.name, player.score)
                        p += ("+---------------------------------------------------------------+\n")
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
                                        print("New game will begin..."
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
                        round_over = False
                    else:
                        pass
        
                #CPU Turns
                elif player.brain == "CPU":
                    #Shows CPU Hand (delete later)
                    player.show()
                    if discard[-1].face == "7":
                        if drew == True:
                            print("User doesn't draw cards.")
                            #+----------------------------+
                            ran = random.choice(player.hand)
                            print(player.name + " plays " + ran.show())
                            if ran.face == "7":
                                drew = False
                                print("Drew status is now " + str(drew))
                            elif ran.face == "A":
                                skipped = False
                                print("Skip status is now " + str(skipped))
                            player.hand.remove(ran)
                            discard.append(ran)
                            #+----------------------------+
                        else:
                            print("User draws cards.")
                            drew = True
                            print("Drew status is now " + str(drew))
                            #+----------------------------+
                            player.draw(deck, 3)
                            #+----------------------------+
                    elif discard[-1].face == "A":
                        if skipped == True:
                            print("User does not get skipped.")
                            #+----------------------------+
                            ran = random.choice(player.hand)
                            print(player.name + " plays " + ran.show())
                            if ran.face == "7":
                                drew = False
                                print("Drew status is now " + str(drew))
                            elif ran.face == "A":
                                skipped = False
                                print("Skip status is now " + str(skipped))
                            player.hand.remove(ran)
                            discard.append(ran)
                            #+----------------------------+
                        else:
                            print("User gets skipped.")
                            skipped = True
                            print("Skip status is now " + str(skipped))
                    else:
                        ran = random.choice(player.hand)
                        print(player.name + " plays " + ran.show())
                        if ran.face == "7":
                            drew = False
                            print("Drew status is now " + str(drew))
                        elif ran.face == "A":
                            skipped = False
                            print("Skip status is now " + str(skipped))
                        player.hand.remove(ran)
                        discard.append(ran)
                    
                    #Checking if round over
                    if len(player.hand) < 1:
                        round_over = True
                    else:
                        round_over = False
                        pass
                        
                    if round_over == True:
                        print("Round over! " + player.name + " wins this round!")
                        time.sleep(1)
                        
                        for player in order:
                            player.add_points()
                        
                        p  = ("+---------------------------------------------------------------+\n")
                        p += ("| Scores:\n")
                        p += ("| Your Score: {}\n").format(user.score)
                        for player in player_order[1:]:
                            p += ("| {}'s Score: {} \n").format(player.name, player.score)
                        p += ("+---------------------------------------------------------------+\n")
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
                                        print("New game will begin..."
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
                        round_over = False
                    else:
                        pass
                        
                else:
                    print("Who are you??? Get out!")
                    exit()

            time.sleep(1)

            s = ""
            s += ("+---------------------------------------------------------------+\n")
            s += ("| Your hand: {}\n").format(len(user.hand))
            for player in order[1:]:
                s += ("| {}'s hand: {} \n").format(player.name, len(player.hand))
            s += ("| Cards in the deck: {}\n").format(len(deck))
            s += ("| " + Fore.LIGHTCYAN_EX + "Current Card: " + str(discard[-1].show()) + "\n" + Fore.RESET)
            s += ("+---------------------------------------------------------------+\n")
            print(s)

            time.sleep(1)



            #game = False
            #print("Game over.")
            #break
        #else:
        #    print("Round is over.")
        #    if total >= 50:
        #        game = False
        #        print("Game is over.")
        #    else:
        #        pass



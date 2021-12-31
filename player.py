#Player Class

from deck import buildDeck
from card import Card
from main import*

class Player:
    def __init__(self, name, brain = "CPU"):
        self.name = name
        self.hand = []
        self.brain = brain
        self.score = 0

    def draw(self, deck, times=1):
        for i in range(times):
            self.hand.append(deck.draw())
        return self

    def add_points(self):
        counter = 0
        for card in self.hand:
            self.score += card.points
        return self.score
    
    def check_score(self):
        return self.score
        print(self.score)

    def clear_hand(self):
        self.hand = []

    def queen(card):
        wild = input("Add a card: ").upper()
        if check_wild(wild) == True:
            self.hand.remove(wild)
            discard.append(wild)
            self.show()
            print("Current card: " + str(discard[-1].show()))
        else:
            print("You cannot play a special card on top of a Queen. Play a different card.")
            queen()

    def action(self, deck, discard):
        hand = ""
        for card in self.hand:
            hand += str(card.show())
        action = input("Action: ").upper()
        if len(action) > 1:
            #Checking to see if user played a card, not a command
            chosen = Card(action[0], action[1:])
            #Turning their input into a card object
            if chosen.show() in hand:
                if check_played(chosen, discard[-1]) == True:
                    #Checking if it is a queen
                    if chosen.face == "Q":
                        self.hand.remove(chosen)
                        discard.append(chosen)
                        self.show()
                        queen()
                    elif chosen.face == "7":
                        print("Next player draws 7 cards.")
                    elif chosen.face == "A":
                        print("Next player is skipped")
                    else:
                        #If it is not a special card
                        #Turning their input to match the card in self.hand
                        #Finding the matching card
                        for card in self.hand:
                            if str(card.show()) == chosen.show():
                                self.hand.remove(card)
                                discard.append(card)
                                self.show()
                                print("Current card: " + str(discard[-1].show()))              
                else:        
                    print("You cannot play that. Try again. Match the suit or face.")
                    self.action(deck, discard)
            else:
                print(chosen.show())
                print(list(self.hand))
                print("You do not have that card. Try again.")
                self.action(deck, discard)
        else:
            #If it is only one letter, it must be a command
            if action == "D":
                self.draw(deck)
                self.show()
            elif action == "P":
                #Make it the next player's turn
                print("passes to next player")
            elif action == "S":
                s  = ("+---------------------------------------------------------------+\n")
                s += ("| Stats:\n")
                s += ("| Scores:\n")
                s += ("| Your Score: {}\n").format(self.score)
                s += ("| CPU Score: \n")
                for i in range(1, 5):
                    s += ("| CPU " + str(i) + ": " + str(Player("CPU " + str(i)).score) + "\n")
                s += ("+---------------------------------------------------------------+\n")
                print(s)
            else:
                print("Invalid action. Try D for Draw, P for Pass, S for Status. Or try playing one of your cards.")
                self.action(deck, discard)   
    def show(self):
        hand = ""
        print("{name}'s cards:".format(name=self.name))
        for card in self.hand:
            hand += "|" + str(card.show()) + "|"
        print(hand)

    def cpu_play(hand, discard, status):
        """
        The logic behind the cpu when playing.
        """
        valid = []
        special = []

        for card in hand:
            if card.check_face == discard[-1].check_face:
                valid.append(card)
            elif card.check_suit == discard[-1].check_suit:
                valid.append(card)
            elif card.check_face == "Q" or card.check_face == "7" or card.check_face == "A":
                special.append(card)

        #Refine this later
        try:
            choice = random.choice(valid)
        except:
            choice = random.choice(special)

        if choice == None:
            return False
        else:
            return choice

    def cpu_action(self, deck, discard):
        try:
            cpu_play()
        except:
            self.draw(deck, 1)
            try:
                cpu_play()
            except:
                print("Passes to next player")
                #Make it pass to next player

    def cpu_show(self):
        print("{name}'s cards: {num}".format(name=self.name, num=int(len(self.hand))))

    
        


#deck = buildDeck()
#deck.shuffle()
#tester = Player("bob", True)
#tester.draw(deck, 5)
#tester.show() 
#tester.add_points
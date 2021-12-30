#Player Class

from deck import buildDeck
from card import Card
from main import *

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

    def action(self, discard):
        action = input("Action: ").upper()
        if len(action) > 1:
            #Checking to see if user played a card, not a command
            chosen = Card(action[0], action[1:])
            #Turning their input into a card object
            if chosen in self.hand:
                if check_played(chosen, discard[-1]) == True:
                    #Checking if it is a queen
                    if chosen.face == "Q":
                        pass

                    self.hand.remove(chosen)
                    discard.append(chosen)
                    self.show()
                    print("Current card: " + str(discard[-1].show()))
                else:
                    print("You cannot play that. Try again. Match the suit or face.")
                    self.action(discard)
            else:
                print("You do not have that card. Try again.")
                self.action(discard)

    def show(self):
        hand = ""
        print("{name}'s cards:".format(name=self.name))
        for card in self.hand:
            hand += "|" + str(card.show()) + "|"
        print(hand)

    def cpu_play(hand, current_card, status):
        """
        The logic behind the cpu when playing.
        """
        valid = []
        special = []

        for card in hand:
            if card.check_face == current_card.check_face:
                valid.append(card)
            elif card.check_suit == current_card.check_suit:
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

    def cpu_action(self):
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

#Status Message
def status():
    s  = ("+---------------------------------------------------------------+\n")
    s += ("| Stats:\n")
    s += ("| Scores:\n")
    s += ("| Your Score: {ysco}\n").format(ysco=user.check_score())
    s += ("| CPU Score: \n")
    for i in range(1, int(num_cpu) + 1):
        s += ("| CPU " + str(i) + ": " + str(Player("CPU " + str(i)).check_score()))
    s += ("+---------------------------------------------------------------+\n")
    print(s)


deck = buildDeck()
deck.shuffle()
tester = Player("bob", True)
tester.draw(deck, 5)
#tester.show() 
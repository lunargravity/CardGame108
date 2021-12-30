#Player Class

from deck import buildDeck
from card import Card

class Player:
    def __init__(self, name):
        self.name = name.title()
        self.hand = []
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

    def action(self):
        action = input("Action: ").upper()
        for card in self.hand:
            if card.show() == action:
                self.hand.remove(card)
                self.show()
                break
            else:
                if action == "D":
                    self.draw(deck, 1)
                    self.show()
                    break
                elif action == "P":
                    #Make it the next player's turn
                    print("passes to next player")
                    break
                elif action == "S":
                    status()
                    break
                else:
                    print("Invalid action")
                    self.action()   
                    break

    def show(self):
        hand = ""
        print("{name}'s cards:".format(name=self.name))
        for card in self.hand:
            hand += "|" + str(card.show()) + "|"
        print(hand)

class CPU(Player):
    def __init__(self, name = "CPU"):
        self.name = name
        self.hand = []
        self.score = 0

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

    def action(self):
        try:
            cpu_play()
        except:
            self.draw(deck, 1)
            try:
                cpu_play()
            except:
                self.next()

    def show(self):
        print("{name}'s cards: {num}".format(name=self.name, num=int(len(self.hand))))

#Status Message
def status():
    s  = ("+---------------------------------------------------------------+\n")
    s += ("| Stats:\n")
    s += ("| Scores:\n")
    s += ("| Your Score: {ysco}\n").format(ysco=user.check_score())
    s += ("| CPU Score: \n")
    for i in range(1, int(num_cpu) + 1):
        s += ("| CPU " + str(i) + ": " + str(CPU("CPU " + str(i)).check_score()))
    s += ("+---------------------------------------------------------------+\n")
    print(s)
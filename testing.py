from player import *

tester = Player("Anu")
deck = buildDeck()
deck.shuffle()
tester.draw(deck, 5)
tester.show()

discard = []
first = deck.draw()
valid = False
while not valid:
    if first.face == "Q" or first.face == "7" or first.face == "A":
        first = deck.draw()
        valid = False
    else:
        discard.append(first)
        print("Current Card: " + str(discard[-1].show()))
        valid = True

choice = input("Choose a card: ").upper()
chosen = Card(choice[0], choice[1])

if chosen.playability(discard) == True:
    for card in tester.hand:
        if str(card.show()) == chosen.show():
            print("Removing...{}".format(card.show()))
            tester.hand.remove(card)
else:
    print("You cannot play that.")
    
tester.show()

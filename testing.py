from player import *

tester = Player("Anu")
deck = buildDeck()
deck.shuffle()
tester.draw(deck, 5)
tester.show()
choice = input("Choose a card: ").upper()
chosen = Card(choice[0], choice[1])
for card in tester.hand:
    if str(card.show()) == chosen.show():
        print("Removing...{}".format(card.show()))
        tester.hand.remove(card)
    
tester.show()
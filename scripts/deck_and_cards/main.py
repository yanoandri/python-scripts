from deck import Deck

deck = Deck()
print(deck.shuffle())
print(deck.cards)
temp = deck.deal_hand(5)
print(temp)
temp = deck.deal_card()
print(temp)

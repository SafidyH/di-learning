import random

class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None

        return self.cards.pop()

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


deck = Deck()

deck.shuffle()

card = deck.deal()

if card is not None:
    print(f"Dealt card: {card.value} of {card.suit}")
else:
    print("No cards left in the deck.")
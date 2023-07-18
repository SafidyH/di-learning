import random

class DeckOfCards:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.deck = self._create_deck()
    
    def _create_deck(self):
        deck = []
        for suit in self.suits:
            for value in self.values:
                deck.append((suit, value))
        return deck
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        if len(self.deck) == 0:
            raise ValueError("The deck is empty.")
        return self.deck.pop()

# Example usage
deck = DeckOfCards()
deck.shuffle()

print(deck.deck)  # Print the shuffled deck
print(deck.deal())  # Deal a card from the deck
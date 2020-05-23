# This file contains the classes that represents the basic components of a card game
class Card:
    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value

    def show_card(self):
        print(f'{self.value} of {self.symbol}')


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ['Clubs', 'Hearts', 'Spades', 'Diamonds']:
            for v in range(1,14):
                self.cards.append(Card(s, v))

    def show_deck(self):
        for c in self.cards:
            c.show_card()


# To be implemented
class Player:
    def __init__(self):
        pass


# Testing the classes creation
if __name__ == "__main__":
    card = Card('Hearts', 6)
    card.show_card()

    deck = Deck()
    deck.show_deck()

import random


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
            for v in (list(range(2, 11)) + ['J', 'Q', 'K', 'A']):
                self.cards.append(Card(s, v))

    def show_deck(self):
        for c in self.cards:
            c.show_card()

    def shuffle(self):
        for i in range(len(self.cards)):
            r = random.randint(0, len(self.cards) - 1)
            self.cards[r], self.cards[i] = self.cards[i], self.cards[r]

    def draw_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_from_deck(self, deck):
        self.hand.append(deck.draw_card())

    def show_hand(self):
        for c in self.hand:
            c.show_card()


# Testing the classes creation
if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    player = Player('Henry')
    player.draw_from_deck(deck)
    player.draw_from_deck(deck)
    player.show_hand()

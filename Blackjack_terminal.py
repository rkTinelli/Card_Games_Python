from Components.classes import Deck,Player

class Dealer(Player):
    def __init__(self):
        super().__init__('Dealer')

    def show_hand_hiding_first(self):
        print('-----------')
        self.hand[1].show_card()


def hand_score(hand):
    score = 0
    checked_A_card = False
    for card in hand:
        if card.value == 'A':
            if not checked_A_card:
                score += 11
                checked_A_card = True
            else:
                score += 1
        elif card.value in ['J', 'Q', 'K']:
            score += 10
        elif int(card.value) in range(2,11):
            score += int(card.value)
    return score


if __name__ == "__main__":

    # Deck of cards creation
    deck = Deck()
    deck.shuffle()

    # Players creation
    player = Player('Henry')
    dealer = Dealer()

    # Give cards to both players
    player.draw_from_deck(deck)
    player.draw_from_deck(deck)
    dealer.draw_from_deck(deck)
    dealer.draw_from_deck(deck)

    # Show players cards
    print(f"{player.name}'s cards:")
    player.show_hand()

    print(f'{player.name} score is: ' + str(hand_score(player.hand)))

    print("Dealer cards:")
    dealer.show_hand_hiding_first()
    dealer.show_hand()
    print('Dealer score is: ' + str(hand_score(dealer.hand)))

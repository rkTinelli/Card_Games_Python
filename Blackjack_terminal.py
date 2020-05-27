from Components.classes import Deck, Player


class BJPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.score = 0

    def calc_score(self):
        score = 0
        checked_A_card = False
        for card in self.hand:
            if card.value == 'A':
                if not checked_A_card:
                    score += 11
                    checked_A_card = True
                else:
                    score += 1
            elif card.value in ['J', 'Q', 'K']:
                score += 10
            elif int(card.value) in range(2, 11):
                score += int(card.value)
        self.score = score

    def display_info(player):
        print(f"{player.name}'s cards:")
        player.show_hand()
        print(f'{player.name} score is: ' + str(player.score))


class Dealer(BJPlayer):
    def __init__(self):
        super().__init__('Dealer')

    def show_hand_hiding_first(self):
        print("Dealer's cards: - Hidden card - and ", end='')
        self.hand[1].show_card()


if __name__ == "__main__":

    # Game variable
    hitting = True
    endgame = False

    # Deck of cards creation
    deck = Deck(8)
    deck.shuffle()

    # Players creation
    player = BJPlayer('Henry')
    dealer = Dealer()

    # Give cards to players
    player.draw_from_deck(deck)
    player.draw_from_deck(deck)
    dealer.draw_from_deck(deck)
    dealer.draw_from_deck(deck)

    # Update players score
    player.calc_score()

    # Show dealer and players cards
    dealer.show_hand_hiding_first()
    player.display_info()

    while hitting:
        action = input('HIT or STAY? ( H / S ) ')
        if action.upper() == "H":
            player.draw_from_deck(deck)
            player.calc_score()
            if player.score > 21:
                hitting, endgame = False, True
                player.display_info()
                print("Busted! That's the end of the game for you, Dealer won this time")
                break
            player.display_info()
        else:
            hitting = False

from random import shuffle

SUITE = "H D S C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


class Deck:
    def __init__(self):
        print("Creating new deck")
        self.cards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("shuffling deck")
        shuffle(self.cards)

    def split_in_half(self):
        return (self.cards[:26], self.cards[26:])


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Hand contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def isEmpty(self):
        return len(self.cards) == 0

    def remove_card(self):
        return self.cards.pop()


class Player:

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for _ in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def still_has_cards(self):
        """
            return True if player has cards left
        """
        return not self.hand.isEmpty()


print("Let's begin")
deck = Deck()

deck.shuffle()
half1, half2 = deck.split_in_half()

computer = Player("computer", Hand(half1))
user = Player(input("What's your name?"), Hand(half2))


total_rounds = 0
war_count = 0

while user.still_has_cards() and computer.still_has_cards():
    total_rounds += 1
    print("Time for a new Round")
    print("{} has the count: {}".format(user.name, len(user.hand.cards)))
    print("{} has the count: {}".format(
        computer.name, len(computer.hand.cards)))
    print("Play a card")
    print("\n")

    table_cards = []

    computer_card = computer.play_card()
    player_card = user.play_card()

    table_cards.append(computer_card)
    table_cards.append(player_card)

    if computer_card[1] == player_card[1]:
        war_count += 1
        print("war!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(computer.remove_war_cards())

        if RANKS.index(computer_card[1]) < RANKS.index(player_card[1]):
            user.hand.add(table_cards)
        else:
            computer.hand.add(table_cards)

print("game over, number of rounds: {}\n war happened {} times".format(
    total_rounds, war_count))

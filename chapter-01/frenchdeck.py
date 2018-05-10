import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    # By implementing the special methods __len__ and __getitem__, deck behaves like a standard Python
    # sequence, allowing it to benefit from core language features (e.g., iteration and slicing)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()

len(deck)

deck[0]
deck[-1]

from random import choice
choice(deck)

for d in deck:
    print(d)

print(Card('Q', 'hearts') in deck)
# >>> True

print(Card('7', 'foo') in deck)
# >>> False

# Sorting

# Rank cards by suit (spades is the highest)
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    # card rank uses the index position (ace is the highest)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)

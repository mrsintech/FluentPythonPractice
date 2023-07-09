import collections
from random import choice

# in this simple project we implement collections.namedtuple, __len__,
# __getitem__

Card = collections.namedtuple("Card", ["rank", "suit"])
# collections.namedtuple is a factory function in the Python collections module
# that creates a subclass of tuple with named fields. It allows you to create
# lightweight, immutable data structures that are similar to tuples but provide
# named attributes for accessing the values.
# we use namedtuple to represent each individual cards


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    # list("JQKA") = ["J", "Q", "K", "A"]
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):  # this will overrite len() behavior of object
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]


frDeck = FrenchDeck()
print(len(frDeck))
print(frDeck[45])

# Python has a function to get a random item from a sequence
rnd = choice(frDeck)
print(rnd)

# now that we implement __getitem__ in class, our deck automatically supports
# slicing.
print(frDeck[:5])
print(frDeck[12::13])

# by implementing __getitem__ now we can use iteration
for card in frDeck:
    print(card)

for card in reversed(frDeck):
    print(card)

# use sort
print("============= sorted ==============")


def spades_high(card):
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(frDeck, key=spades_high):
    print(card)

"""
Although FrenchDeck implicitly inherits from the object class, most of its
functionality is not inherited, but comes from leveraging the data model and
composition. By implementing the special methods __len__ and __getitem__, our
FrenchDeck behaves like a standard Python sequence, allowing it to benefit from
core language features (e.g., iteration and slicing) and from the standard
library, as shown by the examples using random.choice, reversed, and sorted.
Thanks to composition, the __len__ and __getitem__ implementations can delegate
all the work to a list object, self._cards.
"""

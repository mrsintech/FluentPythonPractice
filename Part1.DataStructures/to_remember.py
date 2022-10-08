
def gtitm():
    # getitem
    # we have an object
    obj = {
        'key1' : 'value1',
        'key2' : 'value2'
    }

    # we can access key1 like this
    print(obj['key1'])

    # but in backgroud this actualy happen
    print(obj.__getitem__('key1'))
    
# lets work with collections and some for in lists
import collections
Card = collections.namedtuple('Cardd', ['rank', 'suit']) 
class FrenchDeck: 
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits    # this will act like a for in for syntax
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

def frnchdeck():
    deck = FrenchDeck()
    print(f'element1 : {deck[1]}')
    print(f'len : {len(deck)}')
    
    # select random
    from random import choice 
    rndm = choice(deck) # choice will randomly pick an item in object
    print(f'rndom: {rndm}')
    print(f'deck[:3]: {deck[:3]}') # slicing 
    print(f'deck[12::13]: {deck[12::13]}') # [start:end:skip]
    
    # for card in enumerate(deck):
    #     print(card)
    
    # for card in reversed(deck):
    #     print(card)   
    
    print(Card('K', 'diamonds') in deck)
    

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
# print(suit_values.__iter__())

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank) # .index will return position of element in list
    return rank_value * len(suit_values) + suit_values[card.suit]
    
def sortDeck():
    deck = FrenchDeck()
    for card in sorted(deck, key=spades_high, reverse=True): # Nice!
        print(card)

# sortDeck()
def experiments():
    a = 5
    b = 6
    a += b
    print(a)
    
# optional keyword argument #TODO

 


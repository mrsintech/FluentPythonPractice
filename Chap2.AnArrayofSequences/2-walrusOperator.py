# Walrus operator
from random import shuffle

chars = 'qwerty'
l = list(chars)
shuffle(l)
chars = ''.join(l)

code = [y := x for x in chars]

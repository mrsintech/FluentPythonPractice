# Walrus operator
chars = 'qwerty'
l = list(chars)
shuffle(l)
chars = ''.join(l)

code = [y := x for x in chars]

from random import shuffle

# build a list of unicode code points from a string (without listcomps)
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))


# Build a list of Unicode code points from a string, using a listcomp
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]  # listcomp

# nested list with listcomp
chars = 'ab12'
code = [
    [a, b]
    for a in chars
    for b in reversed(chars)
]

# implement listcomp with filter and map
symbols = '$¢£¥€¤'
code = [ord(s) for s in symbols if ord(s) > 127]
# print(code)

code = list(filter(lambda c: c > 127, map(ord, symbols)))  # learn in future
# print(code)
print(list(map(ord, symbols)))

# Cartesian Products for t-shirts mix with size and color
colors = ['red', 'white']
sizes = ['S', 'M', 'L']
tshirts = [  # list of tuples arranged by color, then size
    (color, size)
    for color in colors
    for size in sizes
]
print(tshirts)

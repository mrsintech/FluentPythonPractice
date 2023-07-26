from collections import ChainMap, Counter
# -=-=-=-=-=-=- OrderedDict -=-=-=-=-=-=- #
# the common reason to use OrderedDict is writing code that is backward
# compatible with earlier Python versions.
# difference between dict and ordered dict:
# • The equality operation for OrderedDict checks for matching order.

# • The popitem() method of OrderedDict has a different signature. It accepts
# an optional argument to specify which item is popped.

# • OrderedDict has a move_to_end() method to efficiently reposition an element
# to an endpoint.

# • The regular dict was designed to be very good at mapping operations.
# Tracking insertion order was secondary.

# • OrderedDict was designed to be good at reordering operations.
# Space efficiency, iteration speed, and the performance of update
# operations were secondary.

# • Algorithmically, OrderedDict can handle frequent reordering operations
# better than dict. This makes it suitable for tracking recent accesses
# (for example, in an LRU cache).

# -=-=-=-=-=-=- ChainMap -=-=-=-=-=-=- #
# A ChainMap instance holds a list of mappings that can be searched as one
# its useful when we want to search throgh multiple dicts
d1 = dict(a=1, b=2)
d2 = dict(a=3, b=4, c=6)
chain = ChainMap(d1, d2)
print(chain['a'])
print(chain['c'])

# The ChainMap instance does not copy the input mappings, but holds references
# to them. Updates or insertions to a ChainMap only affect the first input
# mapping.
chain['c'] = -3
print(d1)

# -=-=-=-=-=-=- Counter -=-=-=-=-=-=- #
# A mapping that holds an integer count for each key. Updating an existing key
# adds to its count.
ct = Counter('abracadabra')
print(ct)
ct.update('aaaaaaaazzz')
print(ct)
print(ct.most_common(3))

# -=-=-=-=-=-=- shelve.Shelf -=-=-=-=-=-=-=- #
# The shelve module in the standard library provides persistent storage for a
# mapping of string keys to Python objects serialized inthe pickle binaryformat


# Python 3.9 supports using | and |= to merge mappings

# The | operator creates a new mapping:
d1 = {
    'a': 1,
    'b': 2,
}
d2 = {
    'b': 6,
    'c': 3,
    'd': 4
}
d3 = d1 | d2  # merging 2 dict
# if duplicated keys exists the right side of | operator set to that key.

d2 |= d1  # in this case values of d1 set to duplicated key

print(d3)
print(d2)

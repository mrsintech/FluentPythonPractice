
# common mapping methods are : dict and defaultdict and OrderedDic
di = dict(a=1, b=2, c=3,)
print('a' in di)
# __contains__ method search in keys of dict

# update(m, [**kwargs]):
# The way d.update(m) handles its first argument m is a prime example of
# duck typing: it first checks whether m has a keys method and, if it does,
# assumes it is a mapping. Otherwise, update() falls back to iterating over m,
# assuming its items are (key, value) pairs. The constructor for most Python
# mappings uses the logic of update() internally, which means they can be
# initialized from other mappings or from any iterable
# object producing (key, value) pairs.

pairs = [
    ('d', 4),
    ('e', 5),
    ('f', 6)
]
di = dict(a=1, b=2, c=3)
di.update(pairs, **{'g': 7})
print(di)

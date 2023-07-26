
# we can apply ** to more than one argument in a function cal. this works when
# keys are all strings and unique across all arguments (because duplicate
# keword arguments are forbidden)

def dump(*args, **kwargs):
    print(args)
    return kwargs


print(dump(78, 2, *[1, 2, 3], **{'x': 10, 'b': 99}, r=3, **{'a': 8943}))

# so far i concluded that with *args in a func the items in args save as a
# tuple, but **kwargs items save as dict
# using * before dict only unpack its keys

# ** can be used inside a dict literal -- also multiple times
# In this case, duplicate keys are allowed. Later occurrences overwrite
# previous ones
di = {
    'a': 23,
    **{"x": 10, "b": 78},
    'y': 52,
    **{"n": 25, "o": 89}
}
print(di)

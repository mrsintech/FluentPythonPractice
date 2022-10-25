
# we can apply ** to more than one argument in a function cal. this works when
# keys are all strings and unique across all arguments (because duplicate
# keword arguments are forbidden)

def dump(args, **kwargs):
    print(args)
    return kwargs


print(dump(78, 2, *[1, 2, 3], **{'x': 10, 'b': 99}, r=3, **{'a': 8943}))

# so far i concluded that with *args in a func the items in args save as a
# tuple, but **kwargs items save as dict
# using * before dict only unpack its keys

# **

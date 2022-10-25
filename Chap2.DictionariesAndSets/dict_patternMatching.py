
# The match/case statement supports subjects that are mapping objects. Patterns
# for mappings look like dict literals, but they can match instances of any
# actual or virtual subclass of collections.abc.Mapping.

from collections import OrderedDict


# def get_creator(rec: dict) -> list:
def get_creator(rec: dict):
    match rec:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names

        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]

        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {rec!r}")

        case {'type': 'movie', 'director': name}:
            return [name]

        case _:
            raise ValueError(f"Invalid record: {rec!r}")


b1 = dict(
    api=1,
    author='cal newport',
    type='book',
    title='deep work'
)

print(get_creator(b1))

b2 = OrderedDict(
    api=2,
    type='book',
    title="Python in a nutshell",
    authors='Martelli Ravenscroft Holden'.split()
)
print(b2)
# i think orderedDict is same as dict.items()
print(get_creator(b2))

# print(get_creator({'type': 'book', 'pages': 825})) # this will throw an error
# print(get_creator('spm spm spm'))

# note that the order of keys in the patterns is irrelevant

# In contrast with sequence patterns, mapping patterns succeed on partial
# matches. In the doctests, the b1 and b2 subjects include a 'title' key that
# does not appear in any 'book' pattern, yet they match.

# There is no need to use **extra to match extra key-value pairs, but if you
# want to capture them as a dict, you can prefix one variable with **. It must
# be the last in the pattern and **_ is forbidden because it would be redundant

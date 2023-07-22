from collections import defaultdict

# Sometimes it is convenient to have mappings that return some made-up value
# when a missing key is searched. There are two main approaches to this: one is
# to use a defaultdict instead of a plain dict. The other is to subclass dict
# or any other mapping type and add a __missing__ method.

# -=-=-=-=-=-=- defaultdict -=-=-=-=-=-=-=- #
# creates items with a default value on demand whenever a missing key is
# searched using d[k] syntax.

# Here is how it works: when instantiating a defaultdict, you provide a
# callable to produce a default value whenever __getitem__ is passed
# a nonexistent key argument.

dd = defaultdict(tuple)
print(dd['abc'])  # returns ()

# The callable that produces the default values is held in an instance
# attribute named default_factory.

# -=-=-=-=-=-=- the __missing__ method -=-=-=-=-=-=- #
# Underlying the way mappings deal with missing keys is the __missing__ method.
# This method is not defined in the base dict class, but dict is aware of it:
# if you subclass dict and provide a __missing__ method, the standard
# dict.__getitem__ will call it whenever a key is not found,
# instead of raising KeyError.

# lets assume an arduino board with 13 pins
# we want use a dict to map pins and get the value of pins with both
# int and str, pin[12] pin['12']

# A better way to create a user-defined mapping type is to subclass
# collections.UserDict instead of dict. Here we subclass dict just to show
# that __missing__ is supported by the built-in dict.__getitem__ method.


class StrKeyDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]

        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

    def test(self):
        print(self.keys())

# d2 = StrKeyDict(('a', 1), ("b", 2)) # this will throw an error
# so if we want to create a dict with key value pairs, we shoud wrap them in a
# list and then send them to dict


d = StrKeyDict(
    [
        ('1', 'one'),
        ('2', 'two'),
        ('3', 'three'),
        ('4', 'four')
    ]
)

print(d['1'])
print(2 in d)

import collections
# It’s better to create a new mapping type by extending collections.UserDict
# rather than dict. The main reason why it’s better to subclass UserDict rather
# than dict is that the built-in has some implementation shortcuts that end up
# forcing us to override meth‐ ods that we can just inherit from UserDict
# with no problems.

# note that UserDict does not inherit from dict. but uses composition:
# it has an inter‐ nal dict instance, called data, which holds the actual
# items. This avoids undesired recursion when coding special methods like
# __setitem__, and simplifies the coding of __contains__


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


# We use dictionaries in all our Python programs. If not directly in our code,
# then indirectly because the dict type is a fundamental part of Python’s
# implementation. Class and instance attributes, module namespaces, and
# function keyword arguments are some of the core Python constructs represented
# by dictionaries in memory. The __builtins__.__dict__ stores all built-in
# types, objects, and functions.

# Because of their crucial role, Python dicts are highly optimized—and continue
# to get improvements. Hash tables are the engines behind Python’s
# high-performance dicts.

# To implement a custom mapping, it’s easier to extend collections.UserDict, or
# to wrap a dict by composition, instead of subclassing these ABCs. The collec
# tions.UserDict class and all concrete mapping classes in the standard library
# encap‐ sulate the basic dict in their implementation, which in turn is built
# on a hash table. Therefore, they all share the limitation that the keys must
# be hashable (the values need not be hashable, only the keys). If you need a
# refresher, the next section explains.

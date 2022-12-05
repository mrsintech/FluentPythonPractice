# Sets are not new in Python, but are still somewhat underused. The set type
# and its immutable sibling frozenset first appeared as modules in the
# Python 2.3 standard library, and were promoted to built-ins in Python 2.6

# A set is a collection of unique objects. A basic use case is removing
# duplication:

li = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
print(li)
print(set(li))
print(list(set(li)))

# the order of unique occurences is somwhat random :/ to solve this:
unique = list(dict.fromkeys(li).keys())
print(unique)

# Set elements must be hashable. The set type is not hashable, so you can’t
# build a set with nested set instances. But frozenset is hashable, so you can
# have frozenset elements inside a set.

# In addition to enforcing uniqueness, the set types implement many set
# operations as infix operators, so, given two sets a and b, a | b returns
# their union, a & b computes the intersection, a - b the difference, and a ^ b
# the symmetric difference. Smart use of set operations can reduce both the
# line count and the execution time of Python programs, at the same time making
# code easier to read and reason about—by removing loops and conditional logic.

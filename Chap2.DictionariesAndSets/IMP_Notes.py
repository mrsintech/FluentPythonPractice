# To save memory, avoid creating instance attributes outside of the __init__
# method.

# That last tip about instance attributes comes from the fact that Python’s
# default behavior is to store instance attributes in a special __dict__
# attribute, which is a dict attached to each instance.9 Since
# PEP 412—Key-Sharing Dictionary was implemented in Python 3.3, instances of a
# class can share a common hash table, stored with the class. That common
# hash table is shared by the __dict__ of each new instance that has the same
# attributes names as the first instance of that class when __init__ returns.
# Each instance __dict__ can then hold only its own attribute values as a
# simple array of pointers. Adding an instance attribute after __init__ forces
# Python to create a new hash table just for the __dict__ of that one instance
# (which was the default behavior for all instances before Python 3.3).
# According to PEP 412, this opti‐ mization reduces memory use by 10% to 20%
# for object-oriented programs.

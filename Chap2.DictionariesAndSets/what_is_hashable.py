
# what is hashable?
# from python glossary, An object is hashable if it has a hash code which never
# changes during its lifetime (it needs a __hash__() method), and can be
# compared to other objects (it needs an __eq__() method). Hashable objects
# which compare equal must have the same hash code.

# Numeric types and flat immutable types str and bytes are all hashable.
# Container types are hashable if they are immutable and all contained objects
# are also hashable. A frozenset is always hashable, because every element it
# contains must be hashable

# The hash code of an object may be different depending on the version of
# Python, the machine architecture, and because of a salt added to the hash
# computation for security reasons. The hash code of a correctly implemented
# object is guaranteed to be constant only within one Python process.

tt = (1, 2, 3, 4)
print(hash(tt))

# Userdefined types are hashable by default because their hash code
# is their id(), and the __eq__() method inherited from the object class simply
# compares the object IDs.

# If an object implements a custom __eq__() that takes into account its
# internal state, it will be hashable only if its __hash__() always returns the
# same hash code. In practice, this requires that __eq__() and __hash__() only
# take into account instance attributes that never change during the life of
# the object.

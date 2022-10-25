
# To implement a custom mapping, it’s easier to extend collections.UserDict, or
# to wrap a dict by composition, instead of subclassing these ABCs. The collec
# tions.UserDict class and all concrete mapping classes in the standard library
# encap‐ sulate the basic dict in their implementation, which in turn is built
# on a hash table. Therefore, they all share the limitation that the keys must
# be hashable (the values need not be hashable, only the keys). If you need a
# refresher, the next section explains.

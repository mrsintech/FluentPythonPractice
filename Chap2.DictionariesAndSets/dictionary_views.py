# The dict instance methods .keys(), .values(), and .items() return instances
# of classes called dict_keys, dict_values, and dict_items, respectively.

# These dictionary views are read-only projections of the internal data
# structures used in the dict implementation. They avoid the memory overhead
# of the equivalent Python 2 methods that returned lists duplicating data
# already in the target dict, and they also replace the old methods that
# returned iterators.

# Example: the .values() method returns a viiew of the values in a dict
di = dict(a=10, b=20, c=30)
vals = di.values()  # this is a dict view

print(list(vals))

# A view object is a dynamic proxy. If the source dict is updated, you can
# immediately see the changes through an existing view.
di['z'] = 40
print(vals)

# NOTE: The dict_values class is the simplest dictionary view—it implements
# only the __len__, __iter__, and __reversed__ special methods. In addition to
# these meth‐ ods, dict_keys and dict_items implement several set methods,
# almost as many as the frozenset class.

# for dict.keys, dict.items the & opertator always return a set
# set operators in dictionary views are compatible with set instances.

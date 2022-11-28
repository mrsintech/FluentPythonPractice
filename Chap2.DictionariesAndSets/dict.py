from time import perf_counter as pc
import sys
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

# -=-=-=-=-=-=- Testing dict vs array and list -=-=-=-=-=-=- #
obj_count = 10 ** 8
t0 = pc()
di = {k: k+1 for k in range(obj_count)}
t_dict = pc() - t0
size_dict = sys.getsizeof(di)
# testing list
t0 = pc()
li = [k for k in range(obj_count)]
t_list = pc() - t0
size_list = sys.getsizeof(li)

# find item in dict
t0 = pc()
item = di[obj_count-1]
t_i_dict = pc() - t0

# find item in list
t0 = pc()
item = li[obj_count-1]
t_i_list = pc() - t0

print('t_dict : ', t_dict)
print('size_dict : ', size_dict)
print('t_list : ', t_list)
print('size_list : ', size_list)
print('t_i_dict : ', t_i_dict)
print('t_i_list : ', t_i_list)

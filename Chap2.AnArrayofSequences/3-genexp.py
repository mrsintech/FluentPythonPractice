import array
import sys

# generator expression
symbols = '$¢£¥€¤'
dataset_tuple = tuple(ord(s) for s in symbols)
# print(dataset)

dataset_array = array.array('I', (ord(s) for s in symbols))
# print(dataset)

print(sys.getsizeof(dataset_tuple))
print(sys.getsizeof(dataset_array))

# genexp real use
# t-shirt cartesian product
colors = ['black', 'red']
sizes = ['S', 'M', 'L']

# it's better optimized
# (explained in summary NOTE: key difference between listcomp and genexp)
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    # print(tshirt)
    pass

# add item(s) to tuple
a = ('jf', '', None)
b = (1, 2, 3)
# print(c := a+b)

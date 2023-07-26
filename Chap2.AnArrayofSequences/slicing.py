# Slice Objects
# Slices made up of 3 parts list[start:end:step]
# casual use
# we have a string:
txt = "helloWorld"
# we want only hello
hello = txt[:5]
# print(hello)

#or maybe we only want Decussated characters 
dec = txt[::2] # 2 step
# print(dec)

# the step part can also be in reverse
rev = txt[::-1]
# print(rev)

# or -2
rev2 = txt[::-2]
# print(rev2)

# we have a slice() method that is charge for slicing sequences
# to evaluate the expression seq[start:end:step] python calls seq.__getitem__(slice(start, end, step))

# with slice() we can name slices just like spreadsheets let assign name for cell ranges
# in this example we will slice a invoice using slice() method
invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                $4.95     2    $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
"""
SKU = slice(0, 6) # we cannot use sequences for this purpose it well throw an error "string indices must be integers"
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
items = invoice.split("\n")[2:]

# OK, we have lineItems and position of its units
# now we will execute a for loop to extract units of each items

for item in items:
    # print(item[UNIT_PRICE], item[DESCRIPTION])
    ... # this is Ellipsis it can be used as pass

# Amazing.

# the [] operator can also take multiple indexes or slices seperated by commas.

# the [] operator work with 2 main magic methods, __getitem__ and __setitem__
    # they receive indices in tuple e.g seq[i, j] the python calls seq.__getitem__((i, j))
    # even it can have start and stop for both indexes seq[a:b, c:d] for slicing a 2D table
    # this syntax can be used in 2D tables in NumPy for example.
    
# NOTE: memoryview, the built-in sequence types in python are 1D, so they support
    # only one index or slice, and not a tuple of them

# TODO: what is Ellipsis Exactly??
    # sofar i understand ellipsis can be used as pass, or if x is a 4D array x[i, ...] is a shortcut for x[i, :, :, :]

# -=-=-=-=-=-=-=- ASSIGNING TO SLICES -=-=-=-=-=-=-=-=- #
# slices can be used to change mutable sequences in place __ that is, without rebuilding them from scratch.
# let's build a list
lis = list(range(10))

# slice notation in place
lis[2:5] = [60, 70] # keep in mind that 4th item is removed 
# print(lis)

# delete slice 
del lis[5:7]
# print(lis)

# even we can use steps in slice notation :/
lis[4:7:2] = [-10, -20]
# print(lis)

# NOTE: when the target of assignment is a slice, the righthand side must be an
    # iterable object, even if it has just one item
    # lis[2:4] = 100 this will throw and err






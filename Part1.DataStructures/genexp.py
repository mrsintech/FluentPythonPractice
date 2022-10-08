import array

# generator expression
symbols = '$¢£¥€¤'
dataset = tuple(ord(s) for s in symbols)
# print(dataset)

dataset = array.array('I', (ord(s) for s in symbols))
# print(dataset)

# genexp real use
# t-shirt cartesian product
colors = ['black', 'red']
sizes  = ['S', 'M', 'L']

for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    # print(tshirt)
    pass   

# add item(s) to tuple
a = ('jf', '', None)  
b = (1, 2, 3)
# print(c := a+b)    

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               








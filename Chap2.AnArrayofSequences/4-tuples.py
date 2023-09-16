"""
using tuples as records with no field names
"""
lax_coordinates = (33.9, -118.4)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)  # records
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
                ('ESP', 'XDA205856')]  # records of each passanger
for passport in traveler_ids:
    # %s is old and obselete use str.format() instead
    # print('%s/%s' % passport)
    ...

for country, _ in traveler_ids:
    # print(country)
    ...

# when a sub-item in tuple change the tuple become different
a = (123, 'foe', ['bar', 'beer'])
b = (123, 'foe', ['bar', 'beer'])
# a and b are equal
# print(a == b)

b[-1].append('python')
# a and b are different now
# print(a == b)

# determine if a tuple is completely immutable:


def fixed(data_tuple):
    try:
        hash(data_tuple)
        return True

    except TypeError:
        return False


data_immutable = ('hello', 223, ('foe', 'bar'))
data_mutable = ('hello', 223, ['foe', 'bar'])
# print(fixed(data_immutable)) # True
# print(fixed(data_mutable)) # False because of list in it.

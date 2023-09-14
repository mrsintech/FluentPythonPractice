"""
using tuples as records with no field names
"""
lax_coordinates = (33.9, -118.4)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)  # records
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
                ('ESP', 'XDA205856')]  # records of each passanger
for passport in traveler_ids:
    # %s is old and obselete use str.format() instead
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

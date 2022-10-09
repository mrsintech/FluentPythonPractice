# Match Case Basic 
status = (1, "foo")
status = (1, "foo", "bar")
# status = (2, "foo", "bar", "baz")
match status:
    case [1, anything]: # sequences type in subject and case can differ and the result dont change
        print(anything)
        
    case [1, i, a]: # the 1 in the beginning of sequence isn't effective if len of status doesn't match
        print(a)
        
    case _: # Default case if nothing match above cases this case will execute
        raise Exception("What are you doing?")

"""
Match/case is like switch/case in C lang but one improvment of match over 
switch is destructuring. a more advanced form of unpacking 
"""
# using match case destruction
metro_areas = [
    ('Tokyo',           'JP', 36.933, (35.689722,  139.691667)),
    ('Delhi NCR',       'IN', 21.935, (28.613889,  77.208889)),
    ('Mexico City',     'MX', 20.142, (19.433333,  -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611,  -74.020386)),
    ('São Paulo',       'BR', 19.649, (-23.547778, -46.635833)),
]
def metro():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for metro_area in metro_areas:
        match metro_area:
            case (name, _, _, (lat, lon) as coord) if lon <= 0: # Facinating, we can use if statements in match/case
                print(f"{name:15} | {lat:9.4f} | {lon:9.4f}")

# treat str as sequence in match/case
phone = "989135557788"
match tuple(phone):
    case ('1', *rest):
        print("American")
        
    case ('9', '8', *rest):
        print("iran")
        
    case ('3' | '4', *rest):
        print("Africa")
        
    case _:
        print("N/A")
        
# we can use "as" in pattern matching for every item in sequence
# we can use type in pattern matching for every item in sequence
def metro2():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for metro_area in metro_areas:
        match metro_area:
            case (str(name), _, _, (float(lat), float() as lon) as coord) if lon <= 0: # first item MUST be str and items in tuple MUST be float nothing else
                print(f"{name:15} | {lat:9.4f} | {lon:9.4f}")
                print(coord)

metro2()








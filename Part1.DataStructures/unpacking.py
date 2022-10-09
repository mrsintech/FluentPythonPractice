import os

# unpacking tovariable
fullname = ('joe', 'smith')
firstname, lastname = fullname
# print(lastname)

# swap values
a = 'foo'
b = 'bar'
a,b = b,a
# print(a)

# prefixing argument with * 
t = divmod(20, 8)
t = (20, 8)
# divmod(t) this will throw an error
t = divmod(*t)
# print(t)

# os.path.split usecase
path = '/user/home/.ssh/id_rsa.pub'
_, filename = os.path.split(path) # split the last item in path
# print(os.path.split(path))

# parallel assignment
a, b, *rest = range(5)
# print(a,b,rest)
# the position of * prefix isn't important
a, *rest, b = range(5)
# print(a,b,rest)

def fun(a, b, c, d, *rest):
    return a, b, c, d, rest

res = fun(*[1,2], 3, *range(4,7)) # send all 5 parameters with 3 arguments
# print(res)

# using * to define list tuple or set
a = *range(4), 4 # build a tuple
# print(a)

b = [*range(4)] # build a list
# print(b)

c = {*range(4), 4, *(5, 6, 7)}
# print(c)

# Nested Unpacking
metro_areas = [
    ('Tokyo',           'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR',       'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City',     'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo',       'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
    
if __name__ == '__main__':
    main()




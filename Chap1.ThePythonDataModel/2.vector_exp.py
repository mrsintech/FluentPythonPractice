import math

"""
A class to represent n Dimention vectors The built-in complex type can be used
to represent twodimensional vectors, but our class can be extended to represent 
n-dimensional vectors.
"""

class Vector:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __repr__(self):
    # !r to standard represention of value (e.g if val='23' it will print '23')
        return f'Vector({self.x!r}, {self.y!r})' 
    
    def __abs__(self):
        return math.hypot(self.x, self.y) # moadele fisaghores
    
    def __bool__(self):
        return bool(abs(self.x or self.y                                                                 ))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __bool__(self):
        return bool(abs(self)) 
        # or
        # return bool(self.x or self.y)          
    
v = Vector(0, 1)
v2 = Vector(2, 3)
v3 = v + v2
print(v3)
print(v2*3)
print(abs(v2*3))


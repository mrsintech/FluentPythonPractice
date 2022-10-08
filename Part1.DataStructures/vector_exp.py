import math

class Vector:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})' # !r to standard represention of value (e.g if val='23' it will print '23')
    
    def __abs__(self):
        return math.hypot(self.x, self.y) # moadele fisaghores
    
    def __bool__(self):
        return bool(abs(self))
    
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
print(bool(v))


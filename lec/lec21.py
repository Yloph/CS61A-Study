### Representation



## String Representation
"""
In python, all objects produce two string representations
str: legible to humans
repr: legible to the python interpreter

For most onjects,
the result of calling repr on a value is what Python prints
in an interactive session

The result of calling str on the value of an expression is
what python prints using the print function
"""
from fractions import Fraction
half = Fraction(1, 2)
repr(half) # Fraction(1, 2)
str(half) # '1/2'
print(half) # 1/2
eval(repr(half)) # Fraction(1, 2)
eval(str(half)) # 0.5


## F-String
"""
Generate strings out of various expressions inside of a string literal

sub-expressions are evaluated in the current environment
"""


## Polymorphic Function
"""
A function that applies many diiferent forms of data

str and repr are polymorphic

repr invokes a zero-argument method __repr__ on its argument
str invokes a zero-argument method __str__ on its argument
"""
class Ratio:

    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0} / {1}'.format(self.numer, self.denom)

half = Ratio(1, 2)
print(half) # 1 / 2
half # Ratio(1, 2)


## Special Method Names
"""
Certain names are special because they have built-in behavior
These names always start and end with two underscores

__init__: invoked automatically when an object is constructed
__repr__: invoked to display an object as a Python expression
__add__: invoked to add one object to another
__bool__: invoked to convert an object to True or False
__float__: invoked to convert an object to a float
"""
class Ratio:

    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0} / {1}'.format(self.numer, self.denom)

    def __add__(self, other):
        if isinstance(other, int):
            n = self.numer + self.denom * other
            d = self.denom
        elif isinstance(other, Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other, float):
            return float(self) + other
        g = gcd(n, d)
        return Ratio(n // g, d // g)

    __radd__ = __add__

    def __float__(self):
        return self.numer / self.denom

def gcd(x, y):
    while x != y:
        x, y = min(x, y), abs(x - y)
    
    return x
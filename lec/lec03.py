### Control


## Names can have different meanings in different environment

## A call expression and the body of the function being called are evaluated in different environment
from operator import mul
def square(square):
    return mul(square, square)

square(4)

## Division: truediv() and floordiv()
def divide_exact(n, d):
    return n // d, n % d

from operator import mod, floordiv
def divide_exact_1(n, d):
    """
    Return the quotient and remainder of dividing n by d

    >>> q, r = divide_exact_1(2013, 10)
    >>> q
    201
    >>> r
    3 
    """
    return floordiv(n, d), mod(n, d)

## A statement is executed by the interpreter to perfrom an action

## Condition statement
def absolute_value(x):
    """
    Return the absolute value of x
    """
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x
    
## while iteration

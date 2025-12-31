### Higher-Order Functions


## Iteration Example: Fibonacci Sequence
def fib(n):
    """
    Compute the n-th fibnoacci sequence, for n >= 1
    """
    pred, curr = 0, 1 # 0th and 1st fibnocci number
    k = 1 # curr is the kth fibnocci number
    while k < n:
        pred, curr = curr, pred + curr
        k += 1
    
    return curr

def fib_(n):
    """
    Compute the n-th fibnocci sequence
    """
    pred, curr = 1, 0
    k = 0
    while k < n:
        pred, curr = curr, pred + curr
        k += 1

    return curr

## Call expression don't allow to skip parts of the call expression
## Logic operator: and, or
from math import sqrt
def has_big_sqrt(x):
    return x > 0 and sqrt(x) >= 10

def reasonable(x):
    return x == 0 or 1 / x != 0

### Higher-Order Function: A func that takes a func as an argument or returns a func as return value
# Express general methods of computation
# Remove repeatition from our program
# Seperate concerns among functions -- each function has exactly one job

## Generalization
# Generalize Area
from math import pi, sqrt
def area(r, shape_cons):
    assert r > 0, "A length must be positive"
    return r * r * shape_cons

def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def hexagon(r):
    return area(r, 3 * sqrt(3) / 2)

# Generalize Computational Process
from operator import mul
def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def pi_term(k):
    return 8 / mul(4 * k - 3, 4 * k - 1)

def summation(n, term): # pass function as an argument of other function
    """
    Sum the first n terms of a sequence

    >>> summation(5, cube)
    225
    """
    tot, k = 0, 1
    while k <= n:
        tot += term(k)
        k += 1

    return tot 

def sum_naturals(n):
    return summation(n, identity)

def sum_cube(n):
    return summation(n, cube)

## Function that returns a function as value
def make_adder(n):
    """
    Return a function
    that takes one argument k and return k + n

    >>> add_three = make_adder(3) # the name add_three is bound to a function
    >>> add_three(4)
    7
    """
    def adder(k): # a local def function
        return n + k
    
    return adder

# Functions are first_class value
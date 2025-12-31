### Functional Abstraction


## Environment diaframs with lambda
a = 1
def f(g):
    a = 2
    return lambda y: a * g(y)

f(lambda y: a + y)(a)


## Return Statements
# A return statement completes the evaluation of call expression and provide its value
def end(n, d):
    """
    Print final digits of n in reverse order until d is found

    >>> end(34567, 5)
    7
    6
    5
    """
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if last == d:
            return None
        
def search(f):
    x = 0
    while not f(x):
        x += 1
    
    return x

def is_three(x):
    return x == 3

def square(x):
    return x * x

def inverse(f):
    """
    Return g(y) such that g(f(x)) -> x
    """
    return lambda y: search(lambda x: f(x) == y)


## Functioncal Abstraction


## Choosing Names
# Names should convey the meaning or purpose of values to which they are bound
# The type of value bound to the name is best documented in the function's docstring
# Function names typically convey their effect, behavior, or the value returned